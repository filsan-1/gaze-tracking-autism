# ASD  child Gaze Tracker

A Python-based application for detecting gaze direction and visual fixation in real-time using a webcam. Built with OpenCV and MediaPipe, this tool helps analyze attention focus in individuals, especially useful in studying Autism Spectrum Disorder (ASD).

## 🔍 Overview

The tool estimates a user’s gaze vector using facial landmarks and maps it to target regions (eyes, mouth, nose). Gaze behavior is logged to CSV in real time, useful for analyzing ASD-related visual attention.

---
## What was achieved
-Accurate real-time gaze tracking using only a webcam.
-Idenification of key behavioral risk flags:excessive eye fixation,low attentionto the mouth(speech area),high unfocused gaze,very few gaze transitions.
-Custom ML-based risk clarification integrated.
-Fully offline,low cost,privacy-preserving deployment.

## 📦 Requirements

- Python 3.10 or newer  
- OpenCV (`opencv-python`):real-time video capture and annotation
- MediaPipe (`mediapipe`):Face and iris landmark detection
- NumPy (`numpy`):Vector and geometry operations
- Pandas:Data logging and aggregation
- Matplotlib:visualisation(pie/bar charts)
- FPDF:Report generation
- Playsound:Auditory feedback system
- Scikit-learn:logistic regression classifier
- custom module:risk_flags.py for bevavioral flag detection


## Use Case Applications
-Early screening in clinics,schoools and homes
-Supplement to clinicians assessments
-Scalable,low-cost solution for early intervention



Install dependencies:
```bash
pip install opencv-python mediapipe numpy
