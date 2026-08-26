"""
FloraAI - 1_Home.py (Dark Theme Edition)
Home Dashboard for FloraAI Botanical Intelligence Platform.
"""

import streamlit as st
from utils.ui_helpers import (
    inject_custom_css, render_sidebar_header, render_progress_stepper,
    render_page_header, render_kpi_card, render_footer
)

st.set_page_config(
    page_title="FloraAI - Botanical AI Assistant",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject Custom Botanical Dark CSS
inject_custom_css()
render_sidebar_header()

# Progress Stepper (Step 1 Active)
render_progress_stepper(1)

# Header Title
render_page_header(
    title="FloraAI",
    subtitle="AI-Powered Iris Flower Species Classification Platform",
    icon="🌸"
)

# Hero Section Banner
st.markdown(
    """
    <div class="flora-card" style="background: linear-gradient(135deg, #130F30 0%, #1E1B4B 50%, #311B58 100%); border: 1px solid rgba(167, 139, 250, 0.3); padding: 40px; margin-bottom: 30px;">
        <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 20px;">
            <div style="max-width: 650px;">
                <span class="flora-badge-emerald" style="margin-bottom: 12px;">🌿 Botanical AI Assistant</span>
                <h2 style="font-size: 32px; font-weight: 700; color: #F8FAFC; margin: 10px 0;">Welcome to FloraAI Intelligence</h2>
                <p style="font-size: 15px; color: #CBD5E1; line-height: 1.6; margin-bottom: 25px;">
                    An end-to-end Machine Learning classification suite designed to analyze physical botanical traits, evaluate algorithm performances, and accurately identify Iris flower species in real-time.
                </p>
            </div>
            <div style="font-size: 110px; opacity: 0.9; text-shadow: 0 10px 30px rgba(0,0,0,0.5);">
                🌺
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# CTA Buttons
col_cta1, col_cta2, col_spacer = st.columns([1, 1, 2])
with col_cta1:
    if st.button("🌿 Explore Dataset", width="stretch"):
        st.switch_page("pages/2_Dataset_Explorer.py")
with col_cta2:
    if st.button("🌸 Predict Flower", width="stretch"):
        st.switch_page("pages/4_Flower_Predictor.py")

st.markdown("<br>", unsafe_allow_html=True)

# Project Statistics KPI Cards
st.markdown("### 📊 Project KPI Metrics")
kpi1, kpi2, kpi3, kpi4 = st.columns(4)
with kpi1:
    render_kpi_card("Total Samples", "150", "purple")
with kpi2:
    render_kpi_card("Flower Features", "4", "emerald")
with kpi3:
    render_kpi_card("Target Species", "3", "pink")
with kpi4:
    render_kpi_card("ML Algorithms", "4", "purple")

st.markdown("<br>", unsafe_allow_html=True)

# Project Overview & Applications
col_ov1, col_ov2 = st.columns(2)
with col_ov1:
    st.markdown(
        """
        <div class="flora-card">
            <h3 style="margin-top:0; color: #A78BFA;">📖 Project Overview</h3>
            <p style="color: #CBD5E1; font-size: 14px; line-height: 1.6;">
                The <strong>Iris Flower Classification</strong> problem is a benchmark dataset introduced by Ronald Fisher in 1936. 
                It consists of 150 instances of Iris flowers belonging to three distinct species: <em>Setosa</em>, <em>Versicolor</em>, and <em>Virginica</em>.
            </p>
            <p style="color: #CBD5E1; font-size: 14px; line-height: 1.6;">
                <strong>Why Machine Learning?</strong> Manual taxonomy requires specialist knowledge and can be subjective. 
                Machine Learning automates pattern recognition across sepal and petal dimensions, providing instantaneous, objective classification.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col_ov2:
    st.markdown(
        """
        <div class="flora-card">
            <h3 style="margin-top:0; color: #34D399;">🌐 Real-World Applications</h3>
            <ul style="color: #CBD5E1; font-size: 14px; line-height: 1.8; padding-left: 20px;">
                <li><strong>Botany & Plant Science:</strong> Automated specimen categorization in field studies.</li>
                <li><strong>Smart Agriculture:</strong> Crop monitoring and automated weed/crop differentiation.</li>
                <li><strong>Plant Research:</strong> Morphological feature extraction for genetic variation tracking.</li>
                <li><strong>STEM Education:</strong> Demonstrating fundamental classification ML workflows.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

# Workflow Section
st.markdown("### 🔄 Machine Learning Workflow")
st.markdown(
    """
    <div class="flora-card" style="text-align: center;">
        <div style="display: flex; justify-content: space-around; align-items: center; flex-wrap: wrap; gap: 15px;">
            <div style="flex: 1; min-width: 140px;">
                <div style="font-size: 30px;">📁</div>
                <div style="font-weight: 600; color: #F8FAFC;">Dataset</div>
                <div style="font-size: 12px; color: #94A3B8;">150 Iris Samples</div>
            </div>
            <div style="font-size: 20px; color: #64748B;">➔</div>
            <div style="flex: 1; min-width: 140px;">
                <div style="font-size: 30px;">📊</div>
                <div style="font-weight: 600; color: #F8FAFC;">EDA</div>
                <div style="font-size: 12px; color: #94A3B8;">Feature Stats</div>
            </div>
            <div style="font-size: 20px; color: #64748B;">➔</div>
            <div style="flex: 1; min-width: 140px;">
                <div style="font-size: 30px;">🤖</div>
                <div style="font-weight: 600; color: #F8FAFC;">Training</div>
                <div style="font-size: 12px; color: #94A3B8;">4 Classifiers</div>
            </div>
            <div style="font-size: 20px; color: #64748B;">➔</div>
            <div style="flex: 1; min-width: 140px;">
                <div style="font-size: 30px;">🌸</div>
                <div style="font-weight: 600; color: #F8FAFC;">Prediction</div>
                <div style="font-size: 12px; color: #94A3B8;">Live Inference</div>
            </div>
            <div style="font-size: 20px; color: #64748B;">➔</div>
            <div style="flex: 1; min-width: 140px;">
                <div style="font-size: 30px;">🎯</div>
                <div style="font-weight: 600; color: #F8FAFC;">Species ID</div>
                <div style="font-size: 12px; color: #94A3B8;">Botanical Insights</div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Supported Models Overview
st.markdown("### 🤖 Supported Classification Algorithms")
m1, m2, m3, m4 = st.columns(4)

models_data = [
    ("Logistic Regression", "Linear classifier utilizing sigmoid probabilities.", "#A78BFA", m1),
    ("Decision Tree", "Rule-based splits maximizing information gain.", "#34D399", m2),
    ("Random Forest", "Ensemble of trees voting for robust accuracy.", "#F472B6", m3),
    ("K-Nearest Neighbors", "Instance-based majority neighbor vote.", "#60A5FA", m4)
]

for name, desc, color, col in models_data:
    with col:
        st.markdown(
            f"""
            <div class="flora-card" style="border-top: 4px solid {color}; padding: 18px; min-height: 150px;">
                <div style="font-weight: 600; color: #F8FAFC; margin-bottom: 6px;">{name}</div>
                <div style="font-size: 12px; color: #94A3B8; line-height: 1.5;">{desc}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

# Tech Stack Badges
st.markdown("### 🛠️ Built With Modern Tech Stack")
st.markdown(
    """
    <div style="margin-bottom: 20px;">
        <span class="flora-badge">Python</span>
        <span class="flora-badge">Streamlit</span>
        <span class="flora-badge-emerald">Pandas</span>
        <span class="flora-badge-emerald">NumPy</span>
        <span class="flora-badge-pink">Scikit-Learn</span>
        <span class="flora-badge-pink">Plotly Express</span>
        <span class="flora-badge">Joblib</span>
        <span class="flora-badge-emerald">Git & GitHub</span>
    </div>
    """,
    unsafe_allow_html=True
)

render_footer()
