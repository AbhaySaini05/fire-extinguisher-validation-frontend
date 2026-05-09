from app.utils.gemini_client import analyze_images

PROMPT = """
Analyze the fire extinguisher images.

Find:
1. Refilling date
2. Refilling due date

Determine whether extinguisher is still valid.

Current year is 2026.

If dates cannot be read confidently, return UNCERTAIN.

Return ONLY valid JSON:

{
  "status": "PASS/FAIL/UNCERTAIN",
  "confidence": 0.0,
  "refill_date": "",
  "due_date": "",
  "reason": ""
}
"""


def run_refill_check(images):

    return analyze_images(images, PROMPT)