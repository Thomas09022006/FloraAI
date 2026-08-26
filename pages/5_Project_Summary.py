"""
FloraAI - 5_Project_Summary.py (Dark Theme Edition)
Project Summary & Final Polish module presenting the full platform documentation and results.
"""

import io
import os
import joblib
import streamlit as st
import pandas as pd
from utils.ui_helpers import (
    inject_custom_css, render_sidebar_header, render_progress_stepper,
    render_page_header, render_kpi_card, render_footer
)
from modules.summary import get_summary_kpis, get_workflow_timeline
from modules.project_info import get_tech_stack_info, get_folder_architecture_text
from modules.deployment import get_deployment_instructions
from modules.save_model import load_saved_model_artifact

st.set_page_config(
    page_title="Project Summary - FloraAI",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

inject_custom_css()
render_sidebar_header()

# Progress Stepper (Step 5 Active - Completed)
render_progress_stepper(5)

# Page Header
render_page_header(
    title="Project Summary & Final Polish",
    subtitle="Comprehensive overview, performance benchmarks, tech stack, and deployment instructions for FloraAI.",
    icon="🎯"
)

# Project Overview Card
st.markdown("### 📌 Executive Summary")
st.markdown(
    """
    <div class="flora-card">
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; font-size: 14px; color: #CBD5E1;">
            <div><strong>Project Name:</strong> 🌸 FloraAI</div>
            <div><strong>Machine Learning Task:</strong> Multiclass Classification</div>
            <div><strong>Problem Statement:</strong> Predict Iris species based on sepal and petal dimensions.</div>
            <div><strong>Target Column:</strong> Species (Setosa, Versicolor, Virginica)</div>
            <div><strong>Dataset Used:</strong> 150 Iris Botanical Specimens</div>
            <div><strong>Business Value:</strong> Automated, real-time flora classification for research & agriculture.</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# Dataset Summary KPI Cards
st.markdown("### 📊 Dataset KPI Metrics")
k1, k2, k3, k4, k5 = st.columns(5)
with k1: render_kpi_card("Samples", "150", "purple")
with k2: render_kpi_card("Features", "4", "emerald")
with k3: render_kpi_card("Classes", "3", "pink")
with k4: render_kpi_card("Missing", "0", "purple")
with k5: render_kpi_card("Duplicates", "1", "emerald")

st.markdown("<br>", unsafe_allow_html=True)

# Machine Learning Workflow Timeline
st.markdown("### 🔄 Machine Learning End-to-End Workflow")
timeline_steps = get_workflow_timeline()

cols = st.columns(len(timeline_steps))
for idx, step in enumerate(timeline_steps):
    with cols[idx]:
        st.markdown(
            f"""
            <div class="flora-card" style="padding: 14px; text-align: center; border-top: 4px solid #A78BFA; min-height: 170px;">
                <div style="font-size: 26px; margin-bottom: 5px;">{step['icon']}</div>
                <div style="font-weight: 700; color: #F8FAFC; font-size: 13px;">{step['title']}</div>
                <div style="font-size: 11px; color: #94A3B8; margin-top: 5px;">{step['desc']}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown("<br>", unsafe_allow_html=True)

# Best Model Showcase Card
artifact = load_saved_model_artifact()

st.markdown("### 🏆 Best Model Showcase")
if artifact is not None:
    st.markdown(
        f"""
        <div class="flora-card" style="background: linear-gradient(135deg, #130F30 0%, #1E1B4B 100%); border: 1px solid rgba(167, 139, 250, 0.4); padding: 28px;">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
                <div>
                    <span class="flora-badge-emerald">Deployed Algorithm</span>
                    <h2 style="color: #F8FAFC; margin: 8px 0;">{artifact['model_name']}</h2>
                    <p style="margin: 0; font-size: 14px; color: #CBD5E1;">
                        Achieved top cross-validated classification accuracy on unseen test data.
                    </p>
                </div>
                <div style="text-align: right;">
                    <div style="font-size: 40px; font-weight: 700; color: #34D399;">{artifact['accuracy']*100:.1f}%</div>
                    <div style="font-size: 12px; text-transform: uppercase; color: #CBD5E1;">Test Accuracy</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.info("ℹ️ Train a model on the Model Training page to display the Best Model card.")

st.markdown("<br>", unsafe_allow_html=True)

# Technology Stack Cards
st.markdown("### 🛠️ Technology Stack Architecture")
tech_stack = get_tech_stack_info()
t_cols = st.columns(3)
for idx, tech in enumerate(tech_stack):
    with t_cols[idx % 3]:
        st.markdown(
            f"""
            <div class="flora-card" style="padding: 16px; margin-bottom: 15px;">
                <div style="display: flex; align-items: center; gap: 12px;">
                    <div style="font-size: 30px;">{tech['icon']}</div>
                    <div>
                        <div style="font-weight: 700; color: #F8FAFC; font-size: 15px;">{tech['name']}</div>
                        <div style="font-size: 12px; color: #A78BFA; font-weight: 600;">{tech['category']}</div>
                        <div style="font-size: 12px; color: #94A3B8; margin-top: 2px;">{tech['desc']}</div>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown("<br>", unsafe_allow_html=True)

# Project Architecture Tree
st.markdown("### 📂 Project Folder Architecture")
st.code(get_folder_architecture_text(), language="text")

st.markdown("<br>", unsafe_allow_html=True)

# Downloads Section
st.markdown("### 📥 Project Artifact Downloads")
d1, d2 = st.columns(2)
with d1:
    if artifact is not None:
        buf = io.BytesIO()
        joblib.dump(artifact["model"], buf)
        buf.seek(0)
        st.download_button("💾 Download Saved Best Model (.joblib)", buf, "best_model.joblib", width="stretch")
    else:
        st.button("💾 Saved Model Unavailable", disabled=True, width="stretch")

with d2:
    if "training_results" in st.session_state:
        from modules.comparison import build_comparison_dataframe
        comp_df = build_comparison_dataframe(st.session_state["training_results"])
        csv_bytes = comp_df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download Model Benchmark CSV", csv_bytes, "model_benchmark.csv", "text/csv", width="stretch")
    else:
        st.button("📥 Benchmark CSV Unavailable", disabled=True, width="stretch")

st.markdown("<br>", unsafe_allow_html=True)

# Deployment Guide
st.markdown("### 🚀 Local Setup & Cloud Deployment Guide")
deploy_info = get_deployment_instructions()

dep_col1, dep_col2 = st.columns(2)

with dep_col1:
    st.markdown("#### 💻 Local Execution Commands")
    st.code("\n".join(deploy_info["local_run"]), language="bash")

with dep_col2:
    st.markdown("#### ☁️ Streamlit Community Cloud Deployment")
    for step in deploy_info["streamlit_cloud"]:
        st.markdown(f"- {step}")

st.markdown("<br>", unsafe_allow_html=True)

# Developer Info & License Card
st.markdown("### 👨‍💻 Developer Information")
st.markdown(
    """
    <div class="flora-card" style="border-top: 4px solid #F472B6;">
        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 15px; font-size: 14px; color: #CBD5E1;">
            <div><strong>Application:</strong> FloraAI v1.0</div>
            <div><strong>Developer:</strong> Botanical AI Engineering Team</div>
            <div><strong>License:</strong> MIT Open Source</div>
            <div><strong>Framework:</strong> Streamlit & Scikit-Learn</div>
            <div><strong>GitHub Repository:</strong> <a href="https://github.com/Thomas09022006/FloraAI" target="_blank" style="color: #A78BFA; text-decoration: underline;">github.com/Thomas09022006/FloraAI</a></div>
            <div><strong>Status:</strong> <span class="flora-badge-emerald">Production Ready</span></div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

render_footer()
