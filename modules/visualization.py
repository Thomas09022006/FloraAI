"""
FloraAI - Visualization Module (Dark Mode Theme - Overlap Fix V2)
Generates all Plotly interactive charts adhering strictly to the FloraAI modern botanical dark design system.
"""

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Glowing Color Constants for Dark Mode
PURPLE = "#A78BFA"
EMERALD = "#34D399"
PINK = "#F472B6"
DARK_NAVY = "#0F172A"

COLOR_DISCRETE = [PURPLE, EMERALD, PINK]
SPECIES_COLOR_MAP = {
    "Iris-setosa": PURPLE,
    "Iris-versicolor": EMERALD,
    "Iris-virginica": PINK
}

def apply_custom_plotly_theme(fig, show_legend=True, legend_bottom=True):
    """Applies standard FloraAI Dark transparent layout to Plotly figures with zero overlapping elements."""
    current_title = fig.layout.title.text if (fig.layout.title and fig.layout.title.text) else ""
    
    layout_dict = dict(
        font_family="Poppins, sans-serif",
        font_color="#F8FAFC",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(15, 23, 42, 0.6)",
        margin=dict(l=35, r=35, t=75, b=60),
        showlegend=show_legend,
        title=dict(
            text=current_title,
            x=0.01,
            y=0.97,
            xanchor="left",
            yanchor="top",
            font=dict(size=15, color="#F8FAFC", family="Poppins")
        )
    )
    
    if show_legend:
        if legend_bottom:
            layout_dict["legend"] = dict(
                orientation="h",
                yanchor="top",
                y=-0.22,
                xanchor="center",
                x=0.5,
                font=dict(color="#CBD5E1", size=11),
                title=dict(text="")
            )
        else:
            layout_dict["legend"] = dict(
                orientation="h",
                yanchor="bottom",
                y=1.04,
                xanchor="right",
                x=1.0,
                font=dict(color="#CBD5E1", size=11),
                title=dict(text="")
            )
            
    fig.update_layout(**layout_dict)
    fig.update_xaxes(showgrid=True, gridcolor="rgba(255, 255, 255, 0.08)", color="#E2E8F0")
    fig.update_yaxes(showgrid=True, gridcolor="rgba(255, 255, 255, 0.08)", color="#E2E8F0")
    return fig

def plot_species_donut(df: pd.DataFrame) -> go.Figure:
    """Generates an interactive Donut Chart of species distribution."""
    counts = df["Species"].value_counts().reset_index()
    counts.columns = ["Species", "Count"]
    
    fig = px.pie(
        counts,
        names="Species",
        values="Count",
        hole=0.55,
        color="Species",
        color_discrete_map=SPECIES_COLOR_MAP,
        title="🌸 Species Distribution (Donut Chart)"
    )
    fig.update_traces(
        textposition="outside",
        textinfo="percent+label",
        marker=dict(line=dict(color='#0F172A', width=2))
    )
    return apply_custom_plotly_theme(fig, show_legend=True, legend_bottom=True)

def plot_species_bar(df: pd.DataFrame) -> go.Figure:
    """Generates an interactive Bar Chart of species counts."""
    counts = df["Species"].value_counts().reset_index()
    counts.columns = ["Species", "Count"]
    
    fig = px.bar(
        counts,
        x="Species",
        y="Count",
        color="Species",
        color_discrete_map=SPECIES_COLOR_MAP,
        text="Count",
        title="🌿 Species Sample Count"
    )
    fig.update_traces(textposition="outside", marker_line_color='#0F172A', marker_line_width=1.5)
    return apply_custom_plotly_theme(fig, show_legend=False)

def plot_feature_histogram(df: pd.DataFrame, feature_col: str) -> go.Figure:
    """Generates an interactive histogram for a given numerical feature."""
    readable_name = feature_col.replace("Cm", " (cm)")
    fig = px.histogram(
        df,
        x=feature_col,
        color="Species",
        color_discrete_map=SPECIES_COLOR_MAP,
        marginal="box",
        nbins=25,
        opacity=0.75,
        title=f"📊 Feature Distribution: {readable_name}"
    )
    fig.update_layout(barmode="overlay", xaxis_title=readable_name, yaxis_title="Count")
    return apply_custom_plotly_theme(fig, show_legend=True, legend_bottom=True)

def plot_feature_boxplots(df: pd.DataFrame, feature_col: str) -> go.Figure:
    """Generates box plots comparing species for a specific feature."""
    readable_name = feature_col.replace("Cm", " (cm)")
    fig = px.box(
        df,
        x="Species",
        y=feature_col,
        color="Species",
        color_discrete_map=SPECIES_COLOR_MAP,
        points="all",
        title=f"📦 Box Plot Comparison: {readable_name}"
    )
    fig.update_layout(yaxis_title=readable_name, xaxis_title="Species")
    return apply_custom_plotly_theme(fig, show_legend=False)

def plot_correlation_heatmap(corr_df: pd.DataFrame) -> go.Figure:
    """Generates an interactive Correlation Heatmap."""
    fig = px.imshow(
        corr_df,
        text_auto=True,
        aspect="auto",
        color_continuous_scale=[[0, "#0F172A"], [0.5, "#7C3AED"], [1, "#C4B5FD"]],
        title="🔥 Feature Correlation Matrix"
    )
    fig.update_traces(colorbar_title="Correlation")
    return apply_custom_plotly_theme(fig, show_legend=False)

def plot_scatter_matrix(df: pd.DataFrame) -> go.Figure:
    """Generates an interactive Pairwise Scatter Matrix colored by Species."""
    feature_cols = [c for c in df.columns if c != "Species"]
    fig = px.scatter_matrix(
        df,
        dimensions=feature_cols,
        color="Species",
        color_discrete_map=SPECIES_COLOR_MAP,
        title="✨ Iris Pairwise Scatter Matrix",
        height=650
    )
    fig.update_traces(diagonal_visible=False, marker=dict(size=5, opacity=0.85))
    return apply_custom_plotly_theme(fig, show_legend=True, legend_bottom=True)

def plot_confusion_matrix(cm: np.ndarray, labels: list, model_name: str) -> go.Figure:
    """Generates a styled Heatmap for Confusion Matrix."""
    fig = px.imshow(
        cm,
        x=labels,
        y=labels,
        text_auto=True,
        color_continuous_scale=[[0, "#0F172A"], [1, PURPLE]],
        labels=dict(x="Predicted Species", y="Actual Species", color="Samples"),
        title=f"🎯 Confusion Matrix — {model_name}"
    )
    return apply_custom_plotly_theme(fig, show_legend=False)

def plot_model_comparison_bar(comparison_df: pd.DataFrame) -> go.Figure:
    """Generates grouped bar chart comparing ML models across performance metrics."""
    metrics = ["Accuracy", "Precision", "Recall", "F1 Score"]
    melted = comparison_df.melt(id_vars=["Model Name"], value_vars=metrics, var_name="Metric", value_name="Score")
    
    fig = px.bar(
        melted,
        x="Model Name",
        y="Score",
        color="Metric",
        barmode="group",
        color_discrete_sequence=[PURPLE, EMERALD, PINK, "#60A5FA"],
        text="Score",
        title="⚡ ML Model Performance Comparison"
    )
    fig.update_traces(texttemplate='%{text:.3f}', textposition='outside')
    fig.update_layout(yaxis_range=[0.8, 1.05])
    return apply_custom_plotly_theme(fig, show_legend=True, legend_bottom=True)

def plot_feature_importance(importance_df: pd.DataFrame, title_prefix: str = "Feature Importance") -> go.Figure:
    """Generates horizontal bar chart for feature importance or coefficients."""
    fig = px.bar(
        importance_df,
        x="Importance",
        y="Feature",
        orientation="h",
        color="Importance",
        color_continuous_scale=[[0, "#4C1D95"], [1, PURPLE]],
        text="Importance",
        title=f"⭐ {title_prefix}"
    )
    fig.update_traces(texttemplate='%{text:.3f}', textposition='outside')
    fig.update_layout(yaxis=dict(autorange="reversed"))
    return apply_custom_plotly_theme(fig, show_legend=False)

def plot_prediction_probability(probabilities: dict) -> go.Figure:
    """Generates probability distribution bar chart for single flower prediction."""
    species = list(probabilities.keys())
    probs = [probabilities[s] * 100 for s in species]
    colors = [SPECIES_COLOR_MAP.get(s, PURPLE) for s in species]
    
    fig = go.Figure(data=[
        go.Bar(
            x=species,
            y=probs,
            marker_color=colors,
            text=[f"{p:.1f}%" for p in probs],
            textposition='outside'
        )
    ])
    fig.update_layout(
        title="🌸 Prediction Probability Distribution (%)",
        xaxis_title="Iris Species",
        yaxis_title="Probability (%)",
        yaxis_range=[0, 115]
    )
    return apply_custom_plotly_theme(fig, show_legend=False)

def plot_confidence_gauge(confidence_pct: float) -> go.Figure:
    """Generates a smooth Plotly Indicator Gauge for prediction confidence in Dark Mode."""
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=confidence_pct,
        number={'suffix': "%", 'font': {'color': "#F8FAFC", 'size': 32}},
        title={'text': "Prediction Confidence", 'font': {'size': 14, 'color': "#94A3B8"}},
        gauge={
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#475569"},
            'bar': {'color': PURPLE},
            'bgcolor': "#1E1B4B",
            'borderwidth': 1,
            'bordercolor': "rgba(167, 139, 250, 0.3)",
            'steps': [
                {'range': [0, 60], 'color': 'rgba(239, 68, 68, 0.25)'},
                {'range': [60, 85], 'color': 'rgba(245, 158, 11, 0.25)'},
                {'range': [85, 100], 'color': 'rgba(16, 185, 129, 0.25)'}
            ]
        }
    ))
    fig.update_layout(height=240, margin=dict(l=20, r=20, t=40, b=20))
    return apply_custom_plotly_theme(fig, show_legend=False)
