import streamlit as st
import pandas as pd
import json
import os

# Page Configuration
st.set_page_config(
    page_title="AuraSync AI - Wellness & Ergonomics Dashboard",
    page_icon="✨",
    layout="wide"
)

# App Title & Description
st.title("✨ AuraSync AI - Wellness & Ergonomics Dashboard")
st.markdown("Real-time telemetry, ergonomic monitoring, and session analytics for AI-powered remote work.")

# Sidebar Settings
st.sidebar.header("Session Settings")
user_name = st.sidebar.text_input("User Name", "Developer")
monitoring_mode = st.sidebar.selectbox("Monitoring Mode", ["Active - Deep Work", "Casual Mode", "Strict Focus"])

st.sidebar.markdown("---")
st.sidebar.info("AI Coach is active in the background monitoring your posture and fatigue index.")

# Top Metric Cards
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Focus Score", value="88%", delta="+4%")
with col2:
    st.metric(label="Avg EAR (Fatigue Index)", value="0.28", delta="-0.02")
with col3:
    st.metric(label="Posture Rating", value="Good", delta="Stable")
with col4:
    st.metric(label="AI Breaks Triggered", value="3", delta="+1")

st.markdown("---")

# Live Telemetry & Trends Section
st.subheader("📊 Live Telemetry & Trends")
chart_data = pd.DataFrame(
    {
        "Fatigue Index": [1.1, -0.8, -1.3, 0.3, -1.4, -0.7, -0.4, -0.7, 1.7, 0.8, -0.4, -0.3, -2.2, 0.9, -0.5, -0.5, 0.6, 0.6, -0.1, -1.7],
        "Focus Level": [-1.3, 0.3, -0.9, 1.5, -1.2, -0.7, -0.4, -0.1, 1.6, 0.1, 0.6, 0.7, -0.1, 0.6, -0.9, 0.8, -0.8, 0.2, -1.5, 0.2],
        "Posture Alignment": [-0.6, 0.4, 0.1, 0.6, 0.5, 0.5, -0.5, 2.0, -1.4, -0.3, -1.3, -1.0, -1.0, -1.0, -0.4, -0.4, 1.0, 0.8, 0.2, 0.3]
    }
)
st.line_chart(chart_data)

st.markdown("---")

# Session Analytics JSON Report Section (New Enhancement)
st.subheader("📁 Latest Session Analytics Report")

report_file = "session_report.json"
if os.path.exists(report_file):
    try:
        with open(report_file, "r") as f:
            report_data = json.load(f)
            
        # Display report in metrics & table format
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            st.metric(label="Session Date", value=report_data.get("session_date", "N/A"))
        with col_b:
            st.metric(label="Duration (Seconds)", value=report_data.get("duration_seconds", 0))
        with col_c:
            st.metric(label="Total Frames Monitored", value=report_data.get("total_frames_monitored", 0))
            
        # Display detailed JSON attributes
        st.write("**Detailed Event Logs:**")
        st.json(report_data)
    except Exception as e:
        st.warning(f"Could not load session report: {e}")
else:
    st.info("No session report found yet. Run `python main.py` and exit to generate session analytics.")