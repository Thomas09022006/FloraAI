"""
FloraAI - 4_Flower_Predictor.py (Dark Theme Edition)
Interactive Flower Species Predictor module for real-time inference.
"""

import streamlit as st
import pandas as pd
from utils.ui_helpers import (
    inject_custom_css, render_sidebar_header, render_progress_stepper,
    render_page_header, render_kpi_card, render_footer
)
from modules.prediction import load_prediction_model, make_prediction
from modules.flower_information import get_species_information
from modules.recommendation import get_prediction_recommendations
from modules.visualization import (
    plot_prediction_probability, plot_confidence_gauge, plot_feature_importance
)

st.set_page_config(
    page_title="Flower Predictor - FloraAI",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded"
)

inject_custom_css()
render_sidebar_header()

# Progress Stepper (Step 4 Active)
render_progress_stepper(4)

# Page Header
render_page_header(
    title="AI Flower Species Predictor",
    subtitle="Enter physical flower measurements to instantly predict Iris species using our saved AI model.",
    icon="🌸"
)

# Load Saved Model Artifact
artifact, auto_trained = load_prediction_model()

if artifact is None:
    st.warning("⚠️ No trained model artifact found. Please train a model on the Model Training page first.")
    if st.button("Go to Model Training ➡️"):
        st.switch_page("pages/3_Model_Training.py")
    st.stop()

if auto_trained:
    st.info(f"ℹ️ Auto-loaded baseline model: **{artifact['model_name']}**.")

# Input Form & Reset
st.markdown("### 📏 Enter Flower Measurements")

col_form, col_preset = st.columns([3, 1])

# Preset selector buttons
with col_preset:
    st.markdown(
        """
        <div class="flora-card" style="padding: 16px;">
            <div style="font-weight: 600; font-size: 14px; margin-bottom: 10px; color: #A78BFA;">🧪 Preset Examples</div>
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("🌸 Setosa Specimen", width="stretch"):
        st.session_state["sl"] = 5.1
        st.session_state["sw"] = 3.5
        st.session_state["pl"] = 1.4
        st.session_state["pw"] = 0.2
    if st.button("🌺 Versicolor Specimen", width="stretch"):
        st.session_state["sl"] = 6.0
        st.session_state["sw"] = 2.7
        st.session_state["pl"] = 4.2
        st.session_state["pw"] = 1.3
    if st.button("🌼 Virginica Specimen", width="stretch"):
        st.session_state["sl"] = 6.5
        st.session_state["sw"] = 3.0
        st.session_state["pl"] = 5.8
        st.session_state["pw"] = 2.2
    if st.button("🔄 Reset Defaults", width="stretch"):
        st.session_state["sl"] = 5.4
        st.session_state["sw"] = 3.4
        st.session_state["pl"] = 1.5
        st.session_state["pw"] = 0.2

# Sliders with defaults from session state
sl = col_form.slider("Sepal Length (cm)", 4.0, 8.0, st.session_state.get("sl", 5.4), 0.1, key="sl")
sw = col_form.slider("Sepal Width (cm)", 2.0, 5.0, st.session_state.get("sw", 3.4), 0.1, key="sw")
pl = col_form.slider("Petal Length (cm)", 1.0, 7.0, st.session_state.get("pl", 1.5), 0.1, key="pl")
pw = col_form.slider("Petal Width (cm)", 0.1, 3.0, st.session_state.get("pw", 0.2), 0.1, key="pw")

btn_predict = st.button("🌸 Predict Flower Species", width="stretch")

# Run Inference
res = make_prediction(sl, sw, pl, pw, artifact)

st.markdown("<br>", unsafe_allow_html=True)

# Main Prediction Result Banner
species_title = res["species"].replace("Iris-", "Iris ").title()
st.markdown(
    f"""
    <div class="flora-card" style="background: linear-gradient(135deg, #4C1D95 0%, #1E1B4B 100%); border: 1px solid rgba(167, 139, 250, 0.4); padding: 30px;">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
            <div>
                <span class="flora-badge-emerald">Predicted Result</span>
                <h2 style="font-size: 34px; font-weight: 700; color: #F8FAFC; margin: 10px 0 5px 0;">🌸 {species_title}</h2>
                <div style="font-size: 13px; color: #CBD5E1;">
                    Model: <strong>{res['model_name']}</strong> | Timestamp: {res['timestamp']}
                </div>
            </div>
            <div style="text-align: right;">
                <div style="font-size: 42px; font-weight: 700; color: #34D399;">{res['confidence']:.1f}%</div>
                <div style="font-size: 12px; text-transform: uppercase; letter-spacing: 1px; color: #CBD5E1;">Confidence Score</div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# Probability Chart & Confidence Gauge
col_prob1, col_prob2 = st.columns([2, 1])

with col_prob1:
    fig_prob = plot_prediction_probability(res["probabilities"])
    st.plotly_chart(fig_prob, width="stretch")
    
with col_prob2:
    fig_gauge = plot_confidence_gauge(res["confidence"])
    st.plotly_chart(fig_gauge, width="stretch")

st.markdown("<br>", unsafe_allow_html=True)

# Detailed Botanical Species Information
st.markdown("### 📖 Species Botanical Profile")
info = get_species_information(res["species"])

st.markdown(
    f"""
    <div class="flora-card" style="border-left: 6px solid #34D399;">
        <h3 style="margin-top:0; color: #34D399;">{info['title']}</h3>
        <p style="color: #CBD5E1; font-size: 14px;"><strong>Color Profile:</strong> {info['color']}</p>
        <p style="color: #CBD5E1; font-size: 14px;"><strong>Key Traits:</strong> {info['characteristics']}</p>
        <p style="color: #CBD5E1; font-size: 14px;"><strong>Native Distribution:</strong> {info['distribution']}</p>
        <div style="background: rgba(16, 185, 129, 0.15); border-radius: 12px; padding: 12px; margin-top: 10px; color: #6EE7B7; font-size: 13px; border: 1px solid rgba(52, 211, 153, 0.3);">
            💡 <strong>Did You Know?</strong> {info['interesting_fact']}
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# Feature Importance & Measurement Summary
st.markdown("### 📊 Feature Contribution & Input Summary")
col_imp1, col_sum2 = st.columns([3, 2])

with col_imp1:
    if res["importance_df"] is not None:
        fig_imp = plot_feature_importance(res["importance_df"], title_prefix="Active Model Feature Weights")
        st.plotly_chart(fig_imp, width="stretch")
    else:
        st.info("Instance-based classification active.")

with col_sum2:
    st.markdown("#### 📋 Measurement Summary Table")
    st.dataframe(res["measurement_table"], width="stretch", hide_index=True)

st.markdown("<br>", unsafe_allow_html=True)

# Rule-Based Botanical Insights
st.markdown("### 💡 Botanical Rule Insights")
insights = get_prediction_recommendations(sl, sw, pl, pw, res["species"], res["confidence"])
for rule in insights:
    st.markdown(f"- {rule}")

st.markdown("<br>", unsafe_allow_html=True)

# Download Result Button
st.markdown("### 📥 Download Prediction Result")
download_df = pd.DataFrame([{
    "SepalLengthCm": sl,
    "SepalWidthCm": sw,
    "PetalLengthCm": pl,
    "PetalWidthCm": pw,
    "PredictedSpecies": res["species"],
    "ConfidencePct": round(res["confidence"], 2),
    "ModelUsed": res["model_name"],
    "Timestamp": res["timestamp"]
}])
csv_data = download_df.to_csv(index=False).encode('utf-8')
st.download_button("📥 Download Prediction CSV", csv_data, f"prediction_{res['species']}.csv", "text/csv", width="stretch")

st.markdown("<br>", unsafe_allow_html=True)

# Navigation Buttons
btn_col1, btn_col2, btn_spacer = st.columns([1, 1, 2])
with btn_col1:
    if st.button("⬅️ Previous: Model Training", width="stretch"):
        st.switch_page("pages/3_Model_Training.py")
with btn_col2:
    if st.button("Next: Project Summary ➡️", width="stretch"):
        st.switch_page("pages/5_Project_Summary.py")

render_footer()
