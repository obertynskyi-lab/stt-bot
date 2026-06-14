import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

DEFAULT_LANGUAGE = "auto"
DEFAULT_SUMMARY_STYLE = "default"

SUPPORTED_LANGUAGES = {
    "auto": "🌍 Автоматически",
    "ru": "🇷🇺 Русский",
    "en": "🇺🇸 English",
    "de": "🇩🇪 Deutsch",
    "fr": "🇫🇷 Français",
    "es": "🇪🇸 Español",
}

SUMMARY_STYLES = {
    "default": {"name": "📝 Стандартное", "prompt": "You are a helpful assistant. Summarize the user text concisely and informatively."},
    "short": {"name": "🤏 Очень коротко (1-2 предложения)", "prompt": "You are a helpful assistant. Summarize the user text in one or two sentences."},
    "bullet_points": {"name": "🔑 Ключевые пункты", "prompt": "You are a helpful assistant. Summarize the user text as a list of key bullet points."},
    "detailed": {"name": "🧐 Подробное", "prompt": "You are a helpful assistant. Provide a detailed summary of the user text, covering all main aspects."}
}

WHISPER_MODEL_SIZE = "small"
MAX_MESSAGE_LENGTH = 4096
TRANSCRIPTION_DISPLAY_CHUNK_SIZE = 3800
SUMMARY_DISPLAY_CHUNK_SIZE = 3800