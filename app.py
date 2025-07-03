import streamlit as st
import subprocess
import os
import pandas as pd
import cv2

# Page config
st.set_page_config(page_title="ASD Gaze Tracker", layout="centered")

# Title
st.title("🧠 ASD Gaze Tracker")
st.subheader("For early screening in schools and clinics")

st.markdown("""
This application helps track gaze behavior using a webcam. It's designed to support early detection of attention and social communication patterns, especially for children with ASD.
""")

# -----------------------
# 🧾 ID Input Section
# -----------------------
st.markdown("---")
st.header("📝 Start a New Session")
user_id = st.text_input("Enter Student/Patient ID", placeholder="e.g. STU12345")

# -----------------------
# 📷 Optional Webcam Preview
# -----------------------
st.markdown("### 🔍 Optional: Preview Webcam")
if st.checkbox("Enable Webcam Preview"):
    cap = cv2.VideoCapture(0)
    stframe = st.empty()
    st.info("Live webcam preview. Close this checkbox or refresh to stop.")
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            st.warning("Webcam not detected.")
            break
        stframe.image(frame, channels="BGR")
        if st.button("❌ Stop Preview"):
            break
    cap.release()
    stframe.empty()

# -----------------------
# ▶️ Launch Tracking
# -----------------------
st.markdown("### ▶️ Run Gaze Tracking")
if st.button("Start Session"):
    if not user_id.strip():
        st.error("⚠️ Please enter a valid ID before starting.")
    else:
        st.success(f"Starting gaze tracking session for: **{user_id}**")
        subprocess.run(["python", "main.py"])

# -----------------------
# 📁 View Results
# -----------------------
st.markdown("---")
st.header("📊 Session Results")

csv_file = "gaze_fixations.csv"
pdf_file = "gaze_report.pdf"

# Gaze Data Table
if os.path.exists(csv_file):
    st.subheader("📋 Gaze Fixation Data")
    df = pd.read_csv(csv_file)
    st.dataframe(df)
else:
    st.info("No gaze data available yet. Run a session first.")

# PDF Report
if os.path.exists(pdf_file):
    st.subheader("📄 Gaze Report")
    with open(pdf_file, "rb") as f:
        st.download_button("📥 Download PDF Report", f, file_name="gaze_report.pdf")
else:
    st.info("No PDF report found yet.")

# Footer
st.markdown("---")
st.caption("⚙️ This app runs fully offline. Your data stays private and secure.")
