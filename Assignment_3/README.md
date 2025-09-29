# Django Terminal Chat Bot (ChatterBot)

This repository contains a **terminal client** that lets you chat with a bot using **Django (4.2)** and **ChatterBot**.

---

## ✨ Features
- Django project scaffold (`chatterproj`) and app (`terminalbot`)
- Management command to **train** the bot (`train_bot`)
- Management command to **chat** in the terminal (`chat_bot`)
- Lightweight config; runs locally on Apple Silicon (M‑series) with Python 3.10

---

## 🧩 Project Structure
```
chatterproj/
  settings.py               # Django settings + CHATTERBOT_* config
terminalbot/
  bot_factory.py            # Singleton ChatBot factory (ENG tagger, deterministic)
  management/commands/
    train_bot.py            # Train from custom seeds (or corpus if desired)
    chat_bot.py             # Interactive terminal chat (REPL)
manage.py
requirements.txt
```
> ChatterBot keeps its own SQLite DB at `bot.sqlite3` (configured in `settings.py`).

---

## ✅ Prerequisites
- Python 3.10 (Apple Silicon OK)
- Virtual environment (recommended)

---

## 🚀 Setup (from scratch)
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
```

### (If using spaCy tagger)
```bash
pip install "spacy==3.7.2"
pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.7.1/en_core_web_sm-3.7.1-py3-none-any.whl
python -m spacy validate
```

> We configured the bot to use `ENG` (no spaCy) **OR** spaCy can be installed as above. Either path works.

---

## 🏋️ Train the bot
```bash
# Fast, deterministic seed-only training (as included)
python manage.py train_bot

# (Optional) if you change training data and want a clean slate
python manage.py chat_bot --reset
python manage.py train_bot
```

---

## 💬 Chat in the terminal
```bash
python manage.py chat_bot
```
Example required I/O:
```
user: Good morning! How are you doing?
bot: I am doing very well, thank you for asking.
user: You're welcome.
bot: Do you like hats?
```

Exit with `quit`, `exit`, or `:q`.

---

## 📝 Coding Best Practices
- Clear module docstrings and inline comments
- Deterministic response selection for grading via `get_first_response`
- Configuration centralized in `bot_factory.py` and `settings.py`
- Virtualenv + pinned requirements for reproducibility

---

## 📸 Screenshot
A sample screenshot is included in the Word document in this folder. If you need to refresh:
1. Run `python manage.py chat_bot`
2. Capture the terminal output showing the required I/O
3. Paste into the Word doc where indicated

---

## 🔗 GitHub Instructions
```bash
git init
git add .
git commit -m "Initial commit: Django + ChatterBot terminal client"
git branch -M main
git remote add origin <YOUR_REPO_URL>
git push -u origin main
```
Include the **GitHub URL** in your Word document submission.

---

## 🧾 Manifest
See `MANIFEST.md` for the list of core files to submit.

---

_Last updated: 2025-09-29T01:36:55_
