# ASD  child Gaze Tracker

A Python-based application for detecting gaze direction and visual fixation in real-time using a webcam. Built with OpenCV and MediaPipe, this tool helps analyze attention focus in individuals, especially useful in studying Autism Spectrum Disorder (ASD).

## 🔍 Overview

The tool estimates a user’s gaze vector using facial landmarks and maps it to target regions (eyes, mouth, nose). Gaze behavior is logged to CSV in real time, useful for analyzing ASD-related visual attention.

---

## 📦 Requirements

- Python 3.10 or newer  
- OpenCV (`opencv-python`)
- MediaPipe (`mediapipe`)
- NumPy (`numpy`)

Install dependencies:
```bash
pip install opencv-python mediapipe numpy
