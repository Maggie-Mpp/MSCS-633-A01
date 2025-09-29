# terminalbot/management/commands/train_bot.py
"""
Django management command: Train the bot using chatterbot_corpus (English).
Usage:
    python manage.py train_bot
"""

from django.core.management.base import BaseCommand
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
from terminalbot.bot_factory import get_chatbot


class Command(BaseCommand):
    help = "Train the ChatterBot instance with the English corpus and a few seed lines."

    def handle(self, *args, **options):
        bot = get_chatbot()

        # 1) Train from the chatterbot English corpus
        self.stdout.write(self.style.MIGRATE_HEADING("Training from chatterbot_corpus (English)..."))
        corpus_trainer = ChatterBotCorpusTrainer(bot)
        # You can narrow to 'greetings'/'conversations' for quicker training while developing:
        # corpus_trainer.train("chatterbot.corpus.english.greetings",
        #                      "chatterbot.corpus.english.conversations")
        corpus_trainer.train("chatterbot.corpus.english")

        # 2) Add a few domain-specific seed conversations (optional but nice)
        self.stdout.write(self.style.MIGRATE_HEADING("Training from custom seed conversations..."))
        seed_trainer = ListTrainer(bot)
        seed_trainer.train([
            "Good morning! How are you doing?",
            "I am doing very well, thank you for asking.",
            "You're welcome.",
            "Do you like hats?",
        ])

        self.stdout.write(self.style.SUCCESS("Training complete."))

