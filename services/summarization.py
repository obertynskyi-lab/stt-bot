import os
import aiohttp
from config import SUMMARY_STYLES

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

async def generate_summary(text: str, style_key: str) -> str:
    style_info = SUMMARY_STYLES.get(style_key, SUMMARY_STYLES["default"])
    system_prompt = style_info["prompt"]

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": text}
        ]
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(GROQ_API_URL, json=payload, headers=headers) as resp:
                data = await resp.json()
                result = data.get("choices", [])
                if result:
                    return result[0]["message"]["content"].strip()
                else:
                    return f"⚠️ Пустой ответ от Groq. Детали: {data}"
    except Exception as e:
        return f"⚠️ Не удалось получить ответ от LLM: {str(e)}"