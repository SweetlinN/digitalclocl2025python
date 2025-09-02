import streamlit as st
from datetime import datetime
import time

# Set page config
st.set_page_config(page_title="Digital Clock", layout="centered")

# Styling
st.markdown(
    """
    <style>
    .clock {
        font-size: 60px;
        font-weight: bold;
        color: yellow;
        background-color: blue;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Digital Clock Display
st.markdown("<h1 style='text-align: center; color: white;'>Digital Clock</h1>", unsafe_allow_html=True)
clock_placeholder = st.empty()

# Update clock in real-time
while True:
    now = datetime.now().strftime("%H:%M:%S")
    clock_html = f"<div class='clock'>{now}</div>"
    clock_placeholder.markdown(clock_html, unsafe_allow_html=True)
    time.sleep(1)
