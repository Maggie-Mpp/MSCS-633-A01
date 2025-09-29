# Manifest — Django Terminal Chat Bot

Submit the following files/folders in your repository:

- `manage.py`
- `requirements.txt`
- `README.md` (this file explains setup and usage)
- `MANIFEST.md` (this file)
- `chatterproj/` (entire folder)
  - `settings.py` (includes CHATTERBOT_* config)
  - `urls.py`, `wsgi.py`, `asgi.py`, `__init__.py`
- `terminalbot/` (entire folder)
  - `bot_factory.py`
  - `management/commands/train_bot.py`
  - `management/commands/chat_bot.py`
  - `__init__.py` files in each package
- `.gitignore` (recommended)
- `bot.sqlite3` (optional — generally **exclude** from repo; regenerate via training)

### Optional artifacts
- `Screenshot.docx` — Word document containing a screenshot of terminal chat
- `screenshots/` — raw PNG of the terminal run

### Run commands (quick reference)
```
python manage.py train_bot
python manage.py chat_bot
```
