from app.utils.gemini_client import analyze_images
from app.utils.database import load_database
from app.utils.database import save_database

PROMPT = """
Analyze the fire extinguisher label.

Extract:
1. Company/manufacturer name
2. Serial number

If either value is unreadable, return UNCERTAIN.

Return ONLY valid JSON:

{
  "company_name": "",
  "serial_number": "",
  "confidence": 0.0
}
"""
def normalize_text(text):

    return text.strip().lower().replace(" ", "_")



def run_company_serial_check(images):

    result = analyze_images(images, PROMPT)

    company_name = result.get("company_name", "")
    serial_number = result.get("serial_number", "")
    confidence = result.get("confidence", 0.0)

    if not company_name or not serial_number:

        return {
            "status": "UNCERTAIN",
            "confidence": confidence,
            "reason": "Company name or serial number unreadable"
        }

    company_name = normalize_text(company_name)
    serial_number = normalize_text(serial_number)

    db = load_database()

    # create company entry if not exists
    if company_name not in db:
        db[company_name] = []

    # duplicate inside SAME company
    if serial_number in db[company_name]:

        return {
            "status": "FAIL",
            "confidence": confidence,
            "company_name": company_name,
            "serial_number": serial_number,
            "reason": f"Duplicate serial number found for company: {company_name}"
        }

    # serial number allowed for different company
    db[company_name].append(serial_number)

    save_database(db)

    return {
        "status": "PASS",
        "confidence": confidence,
        "company_name": company_name,
        "serial_number": serial_number,
        "reason": "Serial number valid for this company"
    }