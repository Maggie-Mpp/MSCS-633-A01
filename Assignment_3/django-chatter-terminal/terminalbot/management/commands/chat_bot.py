# terminalbot/management/commands/chat_bot.py
"""
Django management command: Interactive terminal chat with the ChatterBot.
Usage:
    python manage.py chat_bot
Options:
    --reset   Delete the bot storage DB (bot.sqlite3) before starting.
"""

from __future__ import annotations
import os
from pathlib import Path
from django.core.management.base import BaseCommand
from django.conf import settings
from terminalbot.bot_factory import get_chatbot


class Command(BaseCommand):
    help = "Run an interactive terminal chat session with the ChatterBot."

    def add_arguments(self, parser):
        parser.add_argument(
            "--reset",
            action="store_true",
            help="Delete the bot storage DB (bot.sqlite3) before starting.",
        )

    def handle(self, *args, **options):
        # Optional reset of the ChatterBot storage DB
        if options.get("reset"):
            db_path = Path(settings.CHATTERBOT_DB_PATH)
            if db_path.exists():
                try:
                    os.remove(db_path)
                    self.stdout.write(self.style.WARNING(f"Deleted: {db_path.name}"))
                except OSError as e:
                    self.stderr.write(f"Could not delete {db_path}: {e}")

        bot = get_chatbot()

        self.stdout.write(self.style.MIGRATE_HEADING("TerminalBot — chat session"))
        self.stdout.write("Type your message and press Enter.")
        self.stdout.write("Exit with: 'quit', 'exit', or ':q'\n")

        # Simple REPL loop
        while True:
            try:
                user_text = input("user: ").strip()
            except (EOFError, KeyboardInterrupt):
                self.stdout.write("\nGoodbye!")
                break

            if not user_text:
                continue

            if user_text.lower() in {"quit", "exit", ":q"}:
                self.stdout.write("Goodbye!")
                break

            try:
                response = bot.get_response(user_text)
                print(f"bot: {response.text}")
            except Exception as exc:
                self.stderr.write(self.style.ERROR(f"Error generating response: {exc}"))
