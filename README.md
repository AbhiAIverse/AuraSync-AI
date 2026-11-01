# ✨ AuraSync AI: Real-Time AI Ergonomic & Cognitive Wellness Monitor

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-Computer%20Vision-orange.svg)](https://google.github.io/mediapipe/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web%20Dashboard-red.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**AuraSync AI** is a cutting-edge, real-time computer vision and generative wellness monitoring system designed for remote workers, developers, and students. It tracks physical ergonomics (posture/slouching) and cognitive fatigue (Eye Aspect Ratio) using local camera feeds, delivers proactive voice alerts via an intelligent AI Coach, and provides deep telemetry through a futuristic web dashboard.

---

## 🏗️ System Architecture & Workflow

```mermaid
graph TD
    A[Webcam Feed] --> B[MediaPipe Face Mesh & Pose]
    B --> C[Core Metrics: EAR & Posture Deviation]
    C --> D{Multi-Mode Work Profile}
    D -->|Deep Work / Strict / Casual| E[AI Coach & Speech Alerts pyttsx3]
    C --> F[Session Analytics JSON / HTML]
    F --> G[Streamlit Telemetry Dashboard]