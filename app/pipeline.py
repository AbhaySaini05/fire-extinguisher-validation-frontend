from app.checks.subject_check import run_subject_check
from app.checks.refill_check import run_refill_check
from app.checks.gauge_check import run_gauge_check
from app.checks.seal_check import run_seal_check
from app.checks.serial_check import run_serial_check

from app.utils.gemini_client import usage_stats


def run_pipeline(images):

    report = {}

    print("[INFO] Running subject verification...")

    report["subject_verification"] = run_subject_check(images)

    print("[INFO] Running refill check...")

    report["refill_status"] = run_refill_check(images)

    print("[INFO] Running pressure gauge check...")

    report["pressure_gauge"] = run_gauge_check(images)

    print("[INFO] Running tamper seal check...")

    report["tamper_seal"] = run_seal_check(images)

    print("[INFO] Running serial number check...")

    report["serial_number_check"] = run_serial_check(images)

    failures = [
        v for v in report.values()
        if v.get("status") == "FAIL"
    ]

    uncertain = [
        v for v in report.values()
        if v.get("status") == "UNCERTAIN"
    ]

    if failures:
        final_verdict = "REJECT"

    elif uncertain:
        final_verdict = "REVIEW"

    else:
        final_verdict = "ACCEPT"

    report["final_verdict"] = final_verdict

    report["usage"] = usage_stats

    return report