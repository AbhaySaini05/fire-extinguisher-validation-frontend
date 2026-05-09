import os
import json
import time

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

MODEL_NAME = "gemini-2.5-flash"

usage_stats = {
    "model": MODEL_NAME,
    "api_calls": 0,
    "estimated_tokens": 0
}


def analyze_images(images, prompt):

    for attempt in range(3):

        try:

            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=[prompt, *images],
                config={
                    "response_mime_type": "application/json"
                }
            )

            usage_stats["api_calls"] += 1

            usage_stats["estimated_tokens"] += len(prompt) // 4

            return json.loads(response.text)

        except Exception as e:

            print(f"[ERROR] Gemini attempt {attempt + 1} failed: {e}")

            time.sleep(2)

    return {
        "status": "UNCERTAIN",
        "confidence": 0.0,
        "reason": "Gemini API failed"
    }