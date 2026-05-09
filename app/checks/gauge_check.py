from app.utils.gemini_client import analyze_images

PROMPT = """
Inspect the pressure gauge carefully.

Determine:
- whether gauge exists
- whether needle is visible
- whether needle lies inside green zone
- whether there are signs of physical damage or tampering

If visibility is poor, return UNCERTAIN.

Return ONLY valid JSON:

{
  "status": "PASS/FAIL/UNCERTAIN",
  "confidence": 0.0,
  "reason": ""
}
"""


def run_gauge_check(images):

    return analyze_images(images, PROMPT)