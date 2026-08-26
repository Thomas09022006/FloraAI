"""
FloraAI - Main Streamlit Entry Point
Redirects to pages/1_Home.py and sets up global application state.
"""

import streamlit as st

st.set_page_config(
    page_title="FloraAI - Botanical AI Assistant",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Switch to Home page
st.switch_page("pages/1_Home.py")
