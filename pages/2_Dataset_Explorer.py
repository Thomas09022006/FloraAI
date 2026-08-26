"""
FloraAI - 2_Dataset_Explorer.py (Dark Theme Edition)
Interactive Dataset Explorer page for analyzing Iris flower features.
"""

import streamlit as st
import pandas as pd
from utils.ui_helpers import (
    inject_custom_css, render_sidebar_header, render_progress_stepper,
    render_page_header, render_kpi_card, render_footer
)
from modules.dataset import get_cleaned_dataset, get_summary_metrics, get_feature_table, get_species_counts
from modules.eda import get_correlation_matrix
from modules.visualization import (
    plot_species_donut, plot_species_bar, plot_feature_histogram,
    plot_feature_boxplots, plot_correlation_heatmap, plot_scatter_matrix
)
from modules.insights import generate_dataset_insights

st.set_page_config(
    page_title="Dataset Explorer - FloraAI",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

inject_custom_css()
render_sidebar_header()

# Progress Stepper (Step 2 Active)
render_progress_stepper(2)

# Page Header
render_page_header(
    title="Iris Dataset Explorer",
    subtitle="Explore dataset characteristics, feature distributions, and species separation before training models.",
    icon="🌿"
)

# Load Dataset
try:
    df = get_cleaned_dataset()
    summary = get_summary_metrics(df)
except Exception as e:
    st.error(f"❌ Failed to load dataset: {e}")
    st.stop()

# KPI Metric Cards
st.markdown("### 📌 Dataset Key Metrics")
k1, k2, k3, k4, k5, k6 = st.columns(6)
with k1:
    render_kpi_card("Total Samples", str(summary["total_samples"]), "purple")
with k2:
    render_kpi_card("Features", str(summary["total_features"]), "emerald")
with k3:
    render_kpi_card("Species", str(summary["species_count"]), "pink")
with k4:
    render_kpi_card("Missing Values", str(summary["missing_values"]), "purple")
with k5:
    render_kpi_card("Duplicates", str(summary["duplicates"]), "emerald")
with k6:
    render_kpi_card("Memory", f"{summary['memory_kb']} KB", "pink")

st.markdown("<br>", unsafe_allow_html=True)

# Flower Species Cards
st.markdown("### 🌺 Flower Species Overview")
sc1, sc2, sc3 = st.columns(3)

with sc1:
    st.markdown(
        """
        <div class="flora-card" style="border-top: 4px solid #A78BFA;">
            <h3 style="margin-top:0; color: #A78BFA;">🌸 Iris Setosa</h3>
            <ul style="color: #CBD5E1; font-size: 13px; line-height: 1.6; padding-left: 18px;">
                <li><strong>Small petals</strong> (1.0 – 1.9 cm length)</li>
                <li><strong>Easily separable</strong> from other species</li>
                <li>Short petal width (< 0.6 cm)</li>
                <li>Adapted to cold subarctic climates</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

with sc2:
    st.markdown(
        """
        <div class="flora-card" style="border-top: 4px solid #34D399;">
            <h3 style="margin-top:0; color: #34D399;">🌺 Iris Versicolor</h3>
            <ul style="color: #CBD5E1; font-size: 13px; line-height: 1.6; padding-left: 18px;">
                <li><strong>Medium petal size</strong> (3.0 – 5.1 cm length)</li>
                <li><strong>Moderate measurements</strong> overall</li>
                <li>Versatile adaptation in wetlands</li>
                <li>Harlequin blue-flag appearance</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

with sc3:
    st.markdown(
        """
        <div class="flora-card" style="border-top: 4px solid #F472B6;">
            <h3 style="margin-top:0; color: #F472B6;">🌼 Iris Virginica</h3>
            <ul style="color: #CBD5E1; font-size: 13px; line-height: 1.6; padding-left: 18px;">
                <li><strong>Largest petals</strong> (4.5 – 6.9 cm length)</li>
                <li><strong>Largest overall flower</strong> structure</li>
                <li>Higher variation in physical traits</li>
                <li>Lush green arching foliage</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)

# Feature Summary Table
st.markdown("### 📊 Feature Statistical Summary")
feature_df = get_feature_table(df)
st.dataframe(feature_df, width="stretch", hide_index=True)

st.markdown("<br>", unsafe_allow_html=True)

# Species Distribution Charts
st.markdown("### 🍩 Species Distribution Analysis")
col_chart1, col_chart2 = st.columns(2)
with col_chart1:
    fig_donut = plot_species_donut(df)
    st.plotly_chart(fig_donut, width="stretch")

with col_chart2:
    fig_bar = plot_species_bar(df)
    st.plotly_chart(fig_bar, width="stretch")

st.markdown("<br>", unsafe_allow_html=True)

# Feature Distributions & Boxplots Tabs
st.markdown("### 📈 Feature Distribution & Species Comparison")
feature_cols = summary["feature_names"]
selected_feature = st.selectbox(
    "Select Feature to Analyze:",
    feature_cols,
    format_func=lambda x: x.replace("Cm", " (cm)")
)

col_dist1, col_dist2 = st.columns(2)
with col_dist1:
    fig_hist = plot_feature_histogram(df, selected_feature)
    st.plotly_chart(fig_hist, width="stretch")

with col_dist2:
    fig_box = plot_feature_boxplots(df, selected_feature)
    st.plotly_chart(fig_box, width="stretch")

st.markdown("<br>", unsafe_allow_html=True)

# Correlation Heatmap & Interpretation
st.markdown("### 🔥 Correlation Analysis")
corr_matrix = get_correlation_matrix(df)
col_corr1, col_corr2 = st.columns([3, 2])
with col_corr1:
    fig_heatmap = plot_correlation_heatmap(corr_matrix)
    st.plotly_chart(fig_heatmap, width="stretch")

with col_corr2:
    st.markdown(
        """
        <div class="flora-card" style="margin-top: 40px;">
            <h4 style="margin-top:0; color: #A78BFA;">💡 Heatmap Interpretation</h4>
            <ul style="color: #CBD5E1; font-size: 13px; line-height: 1.7; padding-left: 18px;">
                <li><strong>Petal Length & Petal Width:</strong> Extremely high positive correlation (+0.96). As petal length increases, petal width grows proportionally.</li>
                <li><strong>Petal Length & Sepal Length:</strong> Strong positive correlation (+0.87).</li>
                <li><strong>Sepal Width & Sepal Length:</strong> Slightly negative correlation (-0.11), indicating sepal width is mostly independent.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)

# Pairwise Scatter Matrix
st.markdown("### ✨ Pairwise Scatter Matrix")
fig_scatter = plot_scatter_matrix(df)
st.plotly_chart(fig_scatter, width="stretch")

st.markdown("<br>", unsafe_allow_html=True)

# Data Preview Section
st.markdown("### 📋 Interactive Dataset Preview")
search_term = st.text_input("🔍 Search species or filter records:", placeholder="Type 'setosa', 'versicolor', 'virginica'...")

filtered_df = df.copy()
if search_term:
    filtered_df = filtered_df[filtered_df["Species"].str.contains(search_term, case=False, na=False)]

st.dataframe(filtered_df.head(20), width="stretch")
st.caption(f"Showing top 20 of {len(filtered_df)} matching records.")

st.markdown("<br>", unsafe_allow_html=True)

# Rule-based Botanical Insights
st.markdown("### 💡 Key Botanical Insights")
insights = generate_dataset_insights(df)
for insight in insights:
    st.markdown(f"- {insight}")

st.markdown("<br>", unsafe_allow_html=True)

# Navigation Buttons
btn_col1, btn_col2, btn_spacer = st.columns([1, 1, 2])
with btn_col1:
    if st.button("⬅️ Previous: Home", width="stretch"):
        st.switch_page("pages/1_Home.py")
with btn_col2:
    if st.button("Next: Model Training ➡️", width="stretch"):
        st.switch_page("pages/3_Model_Training.py")

render_footer()
