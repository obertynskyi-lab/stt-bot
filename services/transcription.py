import aiohttp
import aiofiles
import os
from config import WHISPER_MODEL_SIZE

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def load_whisper_model():
    print("Using Groq API for transcription — no local model needed.")
    return None, None

async def transcribe_audio(model, file_path: str, language: str = None) -> str:
    url = "https://api.groq.com/openai/v1/audio/transcriptions"
    
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}"
    }
    
    async with aiofiles.open(file_path, "rb") as f:
        audio_data = await f.read()
    
    data = aiohttp.FormData()
    data.add_field("file", audio_data, filename="audio.ogg", content_type="audio/ogg")
    data.add_field("model", "whisper-large-v3")
    
    if language and language != "auto":
        data.add_field("language", language)
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, data=data) as resp:
                result = await resp.json()
                return result["text"].strip()
    except Exception as e:
        return f"⚠️ Ошибка транскрибации: {str(e)}"