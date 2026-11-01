# ✨ AuraSync AI: Real-Time AI Ergonomic & Cognitive Wellness Monitor

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-Computer%20Vision-orange.svg)](https://google.github.io/mediapipe/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web%20Dashboard-red.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**AuraSync AI** is a cutting-edge, real-time computer vision and generative wellness monitoring system designed for remote workers, developers, and students. It tracks physical ergonomics (posture/slouching) and cognitive fatigue (Eye Aspect Ratio) using local camera feeds, delivers proactive voice alerts via an intelligent AI Coach, and provides deep telemetry through a futuristic web dashboard.

---

## 🚀 Key Features

* **Real-Time Fatigue Detection (EAR):** Computes Eye Aspect Ratio using MediaPipe Face Mesh to detect drowsiness and eye strain instantly.
* **Ergonomic Posture Analysis:** Monitors shoulder and nose alignment to detect slouching or bad posture in real time.
* **Proactive Voice AI Coach (`pyttsx3`):** Speaks out personalized wellness advice and break reminders using multi-threaded text-to-speech to prevent video lag.
* **Futuristic Web Dashboard (`Streamlit`):** Visualizes live telemetry data, focus scores, and trends through an interactive web interface.
* **Automated Session Analytics:** Automatically exports comprehensive JSON logs (`session_report.json`) upon session completion for productivity tracking.

---

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **Computer Vision & ML:** OpenCV, MediaPipe (Face Mesh & Pose Solutions), NumPy
* **Voice Synthesis:** `pyttsx3` (Offline Text-to-Speech)
* **Web Framework:** Streamlit
* **Architecture:** Modular Python backend (`core/` & `dashboard/`)

---

## 📂 Project Architecture

```text
AuraSync-AI/
│
├── core/
│   ├── __init__.py
│   ├── metrics.py       # Fatigue & EAR calculation logic
│   ├── posture.py       # Ergonomic slouching detection
│   ├── ai_coach.py      # Intelligent voice advice generator
│   ├── detector.py      # MediaPipe integrated vision pipeline
│   └── analytics.py     # Session metrics & JSON logger
│
├── dashboard/
│   └── app.py           # Streamlit web telemetry interface
│
├── main.py              # Main desktop application runner
├── requirements.txt     # Project dependencies
├── session_report.json  # Exported session telemetry logs
└── README.md            # Project documentation