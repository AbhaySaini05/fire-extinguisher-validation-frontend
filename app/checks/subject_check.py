from app.utils.gemini_client import analyze_images

PROMPT = """
You are validating fire extinguisher inspection images.

Task:
Determine whether the uploaded images contain a REAL fire extinguisher.

Reject:
- screenshots
- stock photos
- unrelated objects
- AI generated images

If image quality is poor, return UNCERTAIN.

Return ONLY valid JSON:

{
  "status": "PASS/FAIL/UNCERTAIN",
  "confidence": 0.0,
  "reason": ""
}
"""


def run_subject_check(images):

    return analyze_images(images, PROMPT)