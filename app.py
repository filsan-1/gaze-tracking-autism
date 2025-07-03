import streamlit as st
import subprocess
import os
import pandas as pd
import cv2

# Configure the page
st.set_page_config(
    page_title="🧠 ASD Gaze Tracker",
    layout="centered",
    initial_sidebar_state="expanded",
)

# --- Sidebar: About the App ---
with st.sidebar:
    st.header("About")
    st.markdown(
        """
        Welcome to the **ASD Gaze Tracker**, a user-friendly tool designed to support early screening for Autism Spectrum Disorder by tracking gaze patterns through a simple webcam.

        This tool helps schools, clinics, and families monitor attention and social engagement indicators in children, using real-time gaze tracking technology powered by OpenCV and MediaPipe.

        > Fully offline • Privacy-focused • Easy to use
        """
    )
    st.markdown("---")
    st.caption("© 2025 ASD Research Initiative")

# --- Main App Title ---
st.title("🧠 ASD Gaze Tracker")
st.write(
    """
    This application provides a **simple and effective** way to record and analyze gaze behavior.
    Use it to support early identification of attention and social communication patterns in children with ASD.
    """
)

# --- Session Start Section ---
st.markdown("---")
st.header("Start a New Session")

user_id = st.text_input(
    label="Student/Patient ID",
    placeholder="Enter unique ID (e.g., STU12345)",
)

if not user_id:
    st.info("Please enter a valid Student or Patient ID to begin.")
else:
    st.success(f"Ready to start session for **{user_id}**.")

# --- Webcam Preview ---
st.markdown("---")
st.header("Preview Webcam (Optional)")

if 'preview_active' not in st.session_state:
    st.session_state.preview_active = False

def start_preview():
    st.session_state.preview_active = True

def stop_preview():
    st.session_state.preview_active = False

if not st.session_state.preview_active:
    if st.button("Start Webcam Preview"):
        start_preview()
else:
    cap = cv2.VideoCapture(0)
    stop = st.button("Stop Webcam Preview")
    if stop:
        stop_preview()
        cap.release()
        st.empty()
    else:
        if cap.isOpened():
            ret, frame = cap.read()
            if ret:
                st.image(frame, channels="BGR", caption="📷 Live Webcam Feed")
            else:
                st.error("⚠️ Unable to read from webcam.")
        else:
            st.error("⚠️ Webcam not detected or unavailable.")

# --- Start Gaze Tracking ---
st.markdown("---")
st.header("Run Gaze Tracking")

if st.button("▶️ Start Session"):
    if not user_id.strip():
        st.error("⚠️ Student/Patient ID is required before starting.")
    else:
        st.info(f"Starting gaze tracking session for **{user_id}**. Please ensure your webcam is on.")
        # Run your gaze tracking script here
        # Optionally, pass the user_id as argument if main.py supports it
        subprocess.run(["python", "main.py"])
        st.success("Session complete! Check results below.")

# --- Display Session Results ---
st.markdown("---")
st.header("Session Results")

csv_path = "gaze_fixations.csv"
pdf_path = "gaze_report.pdf"

col_left, col_right = st.columns(2)

with col_left:
    if os.path.exists(csv_path):
        st.subheader("Gaze Fixation Data")
        df = pd.read_csv(csv_path)
        st.dataframe(df, height=300)
    else:
        st.info("No gaze fixation data available yet. Run a session to generate results.")

with col_right:
    if os.path.exists(pdf_path):
        st.subheader("Download Gaze Report")
        with open(pdf_path, "rb") as pdf_file:
            st.download_button(
                label="📥 Download PDF Report",
                data=pdf_file,
                file_name=f"gaze_report_{user_id or 'latest'}.pdf",
                mime="application/pdf",
            )
    else:
        st.info("No PDF report found yet. It will be generated after running a session.")

# --- Footer ---
st.markdown("---")
st.write(
    "⚙️ This app is designed to run fully offline. Your data remains private and secure on your device.\n\n"
    "Made with ❤️ by the ASD Research Initiative."
)
