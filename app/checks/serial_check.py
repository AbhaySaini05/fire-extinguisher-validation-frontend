from app.utils.gemini_client import analyze_images
from app.utils.database import load_database
from app.utils.database import save_database

PROMPT = """
Extract the serial number from the fire extinguisher body label.

If serial number is unreadable, return UNCERTAIN.

Return ONLY valid JSON:

{
  "serial_number": "",
  "confidence": 0.0
}
"""


def run_serial_check(images):

    result = analyze_images(images, PROMPT)

    serial_number = result.get("serial_number", "")

    confidence = result.get("confidence", 0.0)

    if not serial_number:

        return {
            "status": "UNCERTAIN",
            "confidence": confidence,
            "reason": "Serial number not readable"
        }

    db = load_database()

    if serial_number in db:

        return {
            "status": "FAIL",
            "confidence": confidence,
            "reason": f"Duplicate serial number found: {serial_number}"
        }

    db[serial_number] = {
        "used": True
    }

    save_database(db)

    return {
        "status": "PASS",
        "confidence": confidence,
        "serial_number": serial_number,
        "reason": "Serial number is unique"
    }