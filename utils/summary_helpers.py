"""
FloraAI - Summary Helpers Module
Provides aggregation functions for final project dashboard and overview statistics.
"""

def get_project_stats_kpis() -> dict:
    """Returns top-level KPI metrics for the project summary."""
    return {
        "num_modules": 5,
        "num_models": 4,
        "total_samples": 150,
        "num_features": 4,
        "num_species": 3,
        "architecture": "Modular Streamlit App"
    }

def get_ml_workflow_steps() -> list:
    """Returns the ordered steps of the Machine Learning workflow."""
    return [
        {"step": "1", "title": "Dataset Ingestion", "desc": "150 Iris flower samples with 4 physical feature measurements.", "icon": "📁"},
        {"step": "2", "title": "Data Preprocessing", "desc": "Cleaned missing values, removed Id column, normalized labels.", "icon": "🧼"},
        {"step": "3", "title": "Exploratory Data Analysis", "desc": "Visualized distributions, scatter matrices, and correlation heatmaps.", "icon": "📊"},
        {"step": "4", "title": "Model Training & CV", "desc": "Trained 4 classification models with 5-fold Stratified Cross Validation.", "icon": "🤖"},
        {"step": "5", "title": "Model Evaluation", "desc": "Compared Accuracy, Precision, Recall, and F1-score to pick Best Model.", "icon": "🏆"},
        {"step": "6", "title": "Model Persistence", "desc": "Saved Best Model artifact with joblib for instant real-time inference.", "icon": "💾"},
        {"step": "7", "title": "Species Prediction", "desc": "Real-time interactive flower species prediction with confidence scoring.", "icon": "🌸"}
    ]
