# terminalbot/bot_factory.py
from __future__ import annotations
import os
from pathlib import Path
from django.conf import settings
from chatterbot import ChatBot
from chatterbot.languages import ENG   # <-- add this
from chatterbot.response_selection import get_first_response


__CHATBOT = None

def get_chatbot():
    global __CHATBOT
    if __CHATBOT is not None:
        return __CHATBOT

    db_path: Path = Path(settings.CHATTERBOT_DB_PATH)
    os.makedirs(db_path.parent, exist_ok=True)
    db_uri = f"sqlite:///{db_path}"

    __CHATBOT = ChatBot(
        settings.CHATTERBOT_NAME,
        storage_adapter="chatterbot.storage.SQLStorageAdapter",
        database_uri=db_uri,
        # logic_adapters=[
        #     {
        #         "import_path": "chatterbot.logic.BestMatch",
        #         "default_response": "I'm not sure I understand yet.",
        #         "maximum_similarity_threshold": 0.90,
        #     },
        #     {"import_path": "chatterbot.logic.MathematicalEvaluation"},
        # ],
        logic_adapters=[
    {
        "import_path": "chatterbot.logic.BestMatch",
        "default_response": "I'm not sure I understand yet.",
        "maximum_similarity_threshold": 0.90,
        "response_selection_method": get_first_response,  # 👈 deterministic
    },
    {"import_path": "chatterbot.logic.MathematicalEvaluation"},
],
        read_only=False,
        tagger_language=ENG,     # <-- pass the object, not a string
    )
    return __CHATBOT
