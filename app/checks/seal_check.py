from app.utils.gemini_client import analyze_images

PROMPT = """
Inspect the tamper seal and safety pin.

Check:
- safety pin exists
- seal exists
- seal is unbroken

If visibility is poor, return UNCERTAIN.

Return ONLY valid JSON:

{
  "status": "PASS/FAIL/UNCERTAIN",
  "confidence": 0.0,
  "reason": ""
}
"""


def run_seal_check(images):

    return analyze_images(images, PROMPT)