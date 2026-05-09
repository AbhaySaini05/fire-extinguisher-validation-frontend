import json
import os

from app.pipeline import run_pipeline
from app.utils.helpers import load_images_from_folder


INPUT_FOLDER = "sample_images"
OUTPUT_FOLDER = "outputs"


if __name__ == "__main__":

    print("[INFO] Loading images...")

    images = load_images_from_folder(INPUT_FOLDER)

    print(f"[INFO] Loaded {len(images)} images")

    print("[INFO] Running pipeline...")

    report = run_pipeline(images)

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    output_path = os.path.join(
        OUTPUT_FOLDER,
        "report.json"
    )

    with open(output_path, "w") as f:
        json.dump(report, f, indent=4)

    print("\n========== FINAL REPORT ==========")

    print(json.dumps(report, indent=4))

    print(f"\n[INFO] Report saved to: {output_path}")