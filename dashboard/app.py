import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="AuraSync AI Dashboard",
    page_icon="✨",
    layout="wide"
)

st.title("✨ AuraSync AI - Wellness & Ergonomics Dashboard")
st.markdown("Real-time telemetry and session analytics for AI-powered remote work and cognitive monitoring.")

# Sidebar telemetry controls
st.sidebar.header("Session Settings")
user_name = st.sidebar.text_input("User Name", "Developer")
mode = st.sidebar.selectbox("Monitoring Mode", ["Active - Deep Work", "Break Mode", "Standby"])

# Metrics columns
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

# Visual analytics section
st.subheader("📈 Live Telemetry & Trends")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["Focus Level", "Fatigue Index", "Posture Alignment"]
)
st.line_chart(chart_data)

st.markdown("---")
st.subheader("💡 Recent AI Coach Recommendations")
st.info("💡 **AI Coach:** Great posture consistency over the last 30 minutes! Keep hydrated and maintain your ergonomics.")