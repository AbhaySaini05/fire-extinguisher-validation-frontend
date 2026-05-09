import streamlit as st
import tempfile
import os
import sys

# Add project root to Python path
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from app.pipeline import run_pipeline
from app.utils.preprocess import load_and_preprocess_image

st.set_page_config(
    page_title="Fire Safety Validator",
    layout="wide"
)

st.title("🔥 Fire Safety Equipment Validation")

uploaded_files = st.file_uploader(
    "Upload fire extinguisher images",
    accept_multiple_files=True,
    type=["jpg", "jpeg", "png"]
)

if uploaded_files:

    images = []

    st.subheader("Uploaded Images")

    cols = st.columns(len(uploaded_files))

    for i, file in enumerate(uploaded_files):

        cols[i].image(file, use_container_width=True)

        temp_path = os.path.join(
            tempfile.gettempdir(),
            file.name
        )

        with open(temp_path, "wb") as f:
            f.write(file.getbuffer())

        img = load_and_preprocess_image(temp_path)

        images.append(img)

    if st.button("Run Inspection"):

        with st.spinner("Analyzing images..."):

            report = run_pipeline(images)

        st.success("Inspection Complete")

        verdict = report["final_verdict"]

        st.subheader("Final Verdict")

        if verdict == "ACCEPT":
            st.success(verdict)

        elif verdict == "REJECT":
            st.error(verdict)

        else:
            st.warning(verdict)

        st.subheader("Inspection Results")

        for key, value in report.items():

            if isinstance(value, dict):

                st.write(f"### {key}")

                st.json(value)

        st.subheader("Complete JSON Report")

        st.json(report)