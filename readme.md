# Fire Safety Equipment Validation System

## Overview

This project is a full-stack AI-powered fire extinguisher inspection system built using:

- Google Gemini Vision API
- OpenCV
- Streamlit frontend
- Python backend

The system analyzes uploaded fire extinguisher images and performs automated fire safety validation checks.

Users can upload extinguisher images through a web interface and receive a detailed inspection report with confidence scores and final verdicts.

---

# Features

## AI Inspection Checks

The system performs:

1. Subject Verification
2. Refill Status Validation
3. Pressure Gauge Inspection
4. Tamper Seal Verification
5. Serial Number Extraction and Deduplication

Each check returns:

- PASS / FAIL / UNCERTAIN
- confidence score
- reasoning output

Final verdict:

- ACCEPT
- REJECT
- REVIEW

---

# Frontend Features

- Multiple image upload
- Image preview
- Live inspection execution
- PASS / FAIL visualization
- JSON inspection report
- Final verdict display
- Confidence score reporting

---

# Tech Stack

## Backend

- Python
- OpenCV
- Google Gemini API
- Pillow

## Frontend

- Streamlit

## Storage

- JSON database

---

# Project Structure

```txt
fire_safety_pipeline/
│
├── app/
│   ├── main.py
│   ├── pipeline.py
│   ├── checks/
│   └── utils/
│
├── frontend/
│   └── streamlit_app.py
│
├── sample_images/
├── outputs/
├── serial_store.json
├── requirements.txt
├── .env
└── README.md
```

---

# Model Selection

Model used:

```txt
gemini-2.5-flash
```

## Why Gemini 2.5 Flash

`gemini-2.5-flash` was selected because it provides the best balance between:

- multimodal reasoning
- OCR capability
- structured JSON generation
- inference speed
- reliability
- free-tier availability

The model demonstrated strong performance for:

- fire extinguisher recognition
- handwritten refill date extraction
- pressure gauge reasoning
- tamper seal validation
- structured safety analysis

while remaining within free-tier API limits.

---

# System Architecture

```txt
Frontend (Streamlit)
        ↓
OpenCV Preprocessing
        ↓
Gemini Vision Analysis
        ↓
Validation Engine
        ↓
Structured JSON Report
        ↓
Final Verdict
```

---

# OpenCV Usage

OpenCV is used for:

- image resizing
- grayscale conversion
- OCR enhancement
- thresholding
- blur analysis
- preprocessing optimization

before Gemini inference.

---

# Installation

## Clone Repository

```bash
git clone <repo-url>
cd fire_safety_pipeline
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Setup

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

---

# Run Backend

```bash
python -m app.main
```

---

# Run Frontend

```bash
streamlit run frontend/streamlit_app.py
```

---

# Frontend Usage

1. Upload extinguisher images
2. Click:

```txt
Run Inspection
```

3. View:
- inspection results
- confidence scores
- final verdict
- JSON report

---

# Example Output

```json
{
  "pressure_gauge": {
    "status": "PASS",
    "confidence": 0.89,
    "reason": "Needle appears inside green zone."
  },
  "final_verdict": "ACCEPT"
}
```

---

# Verdict Logic

| Condition | Verdict |
|---|---|
| Any FAIL | REJECT |
| UNCERTAIN exists | REVIEW |
| All PASS | ACCEPT |

---

# Engineering Highlights

- Full-stack AI inspection system
- OpenCV preprocessing pipeline
- Structured multimodal reasoning
- OCR-based date extraction
- Duplicate serial detection
- Confidence-aware outputs
- Conservative uncertainty handling
- Modular inspection architecture

---

# Safety Design

The system intentionally prioritizes conservative safety validation.

In ambiguous cases, the system returns:

```txt
UNCERTAIN
```

instead of overconfident PASS results to reduce false approvals.

---

# Notes

- No hardcoded extinguisher layouts are used.
- No hardcoded serial number formats are used.
- API keys are securely handled through environment variables.
- Duplicate serial detection uses persistent local storage.
- The pipeline is modular and easily extendable for future inspection checks.