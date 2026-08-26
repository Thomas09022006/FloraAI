"""
FloraAI - Dataset Helpers Module
Handles loading, caching, cleaning, and statistical summaries for the Iris dataset.
"""

import os
import pandas as pd
import numpy as np
import streamlit as st

DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "Iris.csv")

@st.cache_data
def load_dataset(file_path: str = DATA_PATH) -> pd.DataFrame:
    """
    Loads and caches the Iris dataset. Drops the 'Id' column if present.
    """
    if not os.path.exists(file_path):
        # Fallback if path doesn't exist directly
        file_path = os.path.join(os.getcwd(), "data", "Iris.csv")
        
    df = pd.read_csv(file_path)
    if "Id" in df.columns:
        df = df.drop(columns=["Id"])
    return df

def dataset_summary(df: pd.DataFrame) -> dict:
    """
    Returns summary statistics and counts for the dataset.
    """
    feature_cols = [c for c in df.columns if c != "Species"]
    return {
        "total_samples": len(df),
        "total_features": len(feature_cols),
        "species_count": df["Species"].nunique() if "Species" in df.columns else 0,
        "missing_values": df.isnull().sum().sum(),
        "duplicates": df.duplicated().sum(),
        "memory_kb": round(df.memory_usage(deep=True).sum() / 1024, 2),
        "feature_names": feature_cols,
        "species_names": df["Species"].unique().tolist() if "Species" in df.columns else []
    }

def feature_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates detailed statistical metrics for numeric flower measurement features.
    """
    feature_cols = [c for c in df.columns if c != "Species"]
    descriptions = {
        "SepalLengthCm": "Length of the sepal in centimeters (calyx structure).",
        "SepalWidthCm": "Width of the sepal in centimeters.",
        "PetalLengthCm": "Length of the inner petal in centimeters.",
        "PetalWidthCm": "Width of the inner petal in centimeters."
    }
    
    stats_list = []
    for col in feature_cols:
        series = df[col]
        stats_list.append({
            "Feature Name": col.replace("Cm", " (cm)"),
            "Minimum": round(series.min(), 2),
            "Maximum": round(series.max(), 2),
            "Mean": round(series.mean(), 2),
            "Median": round(series.median(), 2),
            "Std Dev": round(series.std(), 2),
            "Description": descriptions.get(col, "Flower metric feature")
        })
        
    return pd.DataFrame(stats_list)

def species_distribution(df: pd.DataFrame) -> pd.DataFrame:
    """
    Computes sample count and percentage breakdown for each Iris flower species.
    """
    counts = df["Species"].value_counts().reset_index()
    counts.columns = ["Species", "Count"]
    total = len(df)
    counts["Percentage (%)"] = ((counts["Count"] / total) * 100).round(1)
    return counts
