"""
FloraAI - UI Helpers Module (Dark Theme Edition)
Provides styling, custom CSS, progress steppers, and reusable dark-mode UI components.
"""

import streamlit as st

# Dark Color Palette Constants
PRIMARY_PURPLE = "#A78BFA"
SECONDARY_EMERALD = "#34D399"
ACCENT_PINK = "#F472B6"
DARK_SIDEBAR = "#090D16"
DARK_BG = "#0B0F19"

def inject_custom_css():
    """Injects modern botanical dark mode CSS styling into the Streamlit application."""
    css = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif !important;
        background-color: #090D16 !important;
        color: #F8FAFC !important;
    }
    
    /* Main App Dark Background */
    .stApp {
        background: linear-gradient(135deg, #090D16 0%, #0F172A 50%, #1A103C 100%) !important;
        color: #F8FAFC !important;
    }

    /* Streamlit Containers & Text Override */
    .stApp, .stApp p, .stApp span, .stApp label, .stApp div, .stApp li {
        color: #E2E8F0;
    }
    
    .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6 {
        color: #F8FAFC !important;
    }

    /* Sidebar Customization */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #080B14 0%, #0D1120 100%) !important;
        border-right: 1px solid rgba(167, 139, 250, 0.15) !important;
    }
    
    section[data-testid="stSidebar"] .stMarkdown, 
    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] span {
        color: #CBD5E1 !important;
    }

    /* Botanical Gradient Titles */
    .botanical-title {
        background: linear-gradient(135deg, #C4B5FD 0%, #F472B6 50%, #34D399 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700;
        letter-spacing: -0.5px;
    }

    /* Glassmorphism Dark Cards */
    .flora-card {
        background: rgba(26, 22, 59, 0.75);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(167, 139, 250, 0.25);
        border-radius: 22px;
        padding: 24px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4), 0 1px 3px rgba(0, 0, 0, 0.2);
        margin-bottom: 20px;
        transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
    }
    .flora-card:hover {
        transform: translateY(-2px);
        border-color: rgba(167, 139, 250, 0.45);
        box-shadow: 0 15px 35px rgba(124, 58, 237, 0.2);
    }
    
    .flora-card h1, .flora-card h2, .flora-card h3, .flora-card h4 {
        color: #F8FAFC !important;
    }
    .flora-card p, .flora-card li, .flora-card div {
        color: #CBD5E1;
    }

    /* KPI Metric Dark Cards */
    .kpi-card {
        background: rgba(23, 20, 52, 0.85);
        border-radius: 20px;
        padding: 20px;
        border-left: 5px solid #A78BFA;
        border-top: 1px solid rgba(167, 139, 250, 0.2);
        border-right: 1px solid rgba(167, 139, 250, 0.2);
        border-bottom: 1px solid rgba(167, 139, 250, 0.2);
        box-shadow: 0 8px 25px rgba(0,0,0,0.3);
        text-align: center;
    }
    .kpi-card-emerald {
        border-left-color: #34D399;
    }
    .kpi-card-pink {
        border-left-color: #F472B6;
    }
    .kpi-val {
        font-size: 28px;
        font-weight: 700;
        color: #F8FAFC !important;
    }
    .kpi-lbl {
        font-size: 12px;
        font-weight: 600;
        color: #A78BFA;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        margin-top: 4px;
    }

    /* Progress Stepper Dark */
    .stepper-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: rgba(22, 19, 48, 0.85);
        backdrop-filter: blur(10px);
        border-radius: 50px;
        padding: 12px 24px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.4);
        margin-bottom: 30px;
        border: 1px solid rgba(167, 139, 250, 0.25);
    }
    .step-item {
        display: flex;
        align-items: center;
        gap: 8px;
        font-size: 13px;
        font-weight: 600;
        color: #64748B;
    }
    .step-item.active {
        color: #C4B5FD;
    }
    .step-item.completed {
        color: #34D399;
    }
    .step-badge {
        width: 26px;
        height: 26px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 12px;
        background: #1E293B;
        color: #94A3B8;
    }
    .step-item.active .step-badge {
        background: #7C3AED;
        color: #FFFFFF;
        box-shadow: 0 0 14px rgba(124, 58, 237, 0.6);
    }
    .step-item.completed .step-badge {
        background: #059669;
        color: #FFFFFF;
    }

    /* Custom Dark Buttons & Download Buttons */
    .stButton > button,
    .stDownloadButton > button,
    div[data-testid="stDownloadButton"] > button,
    button[kind="secondary"],
    button[kind="primary"],
    button {
        background: linear-gradient(135deg, #7C3AED 0%, #6D28D9 100%) !important;
        color: #FFFFFF !important;
        border: 1px solid rgba(196, 181, 253, 0.4) !important;
        border-radius: 14px !important;
        padding: 10px 24px !important;
        font-weight: 600 !important;
        font-size: 14px !important;
        box-shadow: 0 4px 16px rgba(124, 58, 237, 0.4) !important;
        transition: all 0.3s ease !important;
    }

    .stButton > button *,
    .stDownloadButton > button *,
    div[data-testid="stDownloadButton"] > button *,
    button * {
        color: #FFFFFF !important;
        font-weight: 600 !important;
    }

    .stButton > button:hover,
    .stDownloadButton > button:hover,
    div[data-testid="stDownloadButton"] > button:hover,
    button:hover {
        background: linear-gradient(135deg, #8B5CF6 0%, #7C3AED 100%) !important;
        color: #FFFFFF !important;
        box-shadow: 0 6px 24px rgba(167, 139, 250, 0.5) !important;
        transform: translateY(-1px);
    }
    
    .stButton > button:hover *,
    .stDownloadButton > button:hover *,
    div[data-testid="stDownloadButton"] > button:hover *,
    button:hover * {
        color: #FFFFFF !important;
    }

    /* Disabled buttons styling */
    button:disabled,
    .stButton > button:disabled,
    .stDownloadButton > button:disabled {
        background: rgba(30, 27, 75, 0.6) !important;
        color: #94A3B8 !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        box-shadow: none !important;
        cursor: not-allowed !important;
    }

    button:disabled *,
    .stButton > button:disabled *,
    .stDownloadButton > button:disabled * {
        color: #94A3B8 !important;
    }

    /* Badge Tags */
    .flora-badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
        background: rgba(124, 58, 237, 0.25);
        color: #C4B5FD;
        border: 1px solid rgba(167, 139, 250, 0.3);
        margin-right: 6px;
    }
    .flora-badge-emerald {
        background: rgba(16, 185, 129, 0.2);
        color: #6EE7B7;
        border: 1px solid rgba(52, 211, 153, 0.3);
    }
    .flora-badge-pink {
        background: rgba(236, 72, 153, 0.2);
        color: #F472B6;
        border: 1px solid rgba(244, 114, 182, 0.3);
    }

    /* Streamlit Selectbox, Text Input & Dataframes Dark Styling */
    div[data-baseweb="select"] > div,
    div[data-baseweb="input"] > div,
    input {
        background-color: #131B2E !important;
        color: #F8FAFC !important;
        border-color: rgba(167, 139, 250, 0.3) !important;
    }

    /* Dataframe dark override */
    .stDataFrame {
        background-color: #111827 !important;
        border-radius: 14px;
        padding: 6px;
    }
    
    /* Code block dark styling */
    pre, code {
        background-color: #0F172A !important;
        color: #A78BFA !important;
        border-radius: 12px !important;
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def render_sidebar_header():
    """Renders customized botanical branding in the sidebar."""
    st.sidebar.markdown(
        """
        <div style="text-align: center; padding: 15px 0 25px 0;">
            <div style="font-size: 42px; margin-bottom: 5px;">🌸</div>
            <div style="font-size: 22px; font-weight: 700; color: #F8FAFC; letter-spacing: -0.5px;">FloraAI</div>
            <div style="font-size: 12px; color: #6EE7B7; font-weight: 500;">Botanical Intelligence Platform</div>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.sidebar.markdown("---")

def render_progress_stepper(current_step: int):
    """
    Renders an interactive visual progress stepper across pages.
    current_step: 1 (Home), 2 (Dataset Explorer), 3 (Model Training), 4 (Flower Predictor), 5 (Project Summary)
    """
    steps = [
        ("Home", "1"),
        ("Dataset Explorer", "2"),
        ("Model Training", "3"),
        ("Flower Predictor", "4"),
        ("Project Summary", "5")
    ]
    
    html = '<div class="stepper-container">'
    for idx, (label, num) in enumerate(steps, 1):
        if idx < current_step:
            status_class = "completed"
            icon = "✓"
        elif idx == current_step:
            status_class = "active"
            icon = num
        else:
            status_class = ""
            icon = num
            
        html += f"""
        <div class="step-item {status_class}">
            <div class="step-badge">{icon}</div>
            <span style="display: inline-block;">{label}</span>
        </div>
        """
        if idx < len(steps):
            html += '<div style="flex-grow: 1; height: 2px; background: rgba(255,255,255,0.1); margin: 0 10px;"></div>'
            
    html += '</div>'
    st.markdown(html, unsafe_allow_html=True)

def render_page_header(title: str, subtitle: str, icon: str = "🌸"):
    """Renders a standard botanical title section."""
    st.markdown(
        f"""
        <div style="margin-bottom: 25px;">
            <h1 style="margin: 0; font-size: 32px; font-weight: 700; color: #F8FAFC;">
                {icon} <span class="botanical-title">{title}</span>
            </h1>
            <p style="margin-top: 6px; font-size: 15px; color: #94A3B8; font-weight: 400;">
                {subtitle}
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

def render_kpi_card(label: str, value: str, color_type: str = "purple"):
    """Renders a single KPI metric display card."""
    card_class = "kpi-card"
    if color_type == "emerald":
        card_class += " kpi-card-emerald"
    elif color_type == "pink":
        card_class += " kpi-card-pink"

    st.markdown(
        f"""
        <div class="{card_class}">
            <div class="kpi-val">{value}</div>
            <div class="kpi-lbl">{label}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

def render_footer():
    """Renders application footer."""
    st.markdown("---")
    st.markdown(
        """
        <div style="text-align: center; color: #64748B; font-size: 13px; padding: 15px 0 30px 0;">
            🌸 <strong>FloraAI</strong> — AI-Powered Iris Flower Classification Platform | Developed with Python, Streamlit & Scikit-Learn | v1.0
        </div>
        """,
        unsafe_allow_html=True
    )
