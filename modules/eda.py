"""
FloraAI - EDA Logic Module
Provides Exploratory Data Analysis computation functions for Iris flower characteristics.
"""

import pandas as pd
import numpy as np

def get_species_group_stats(df: pd.DataFrame) -> pd.DataFrame:
    """Computes mean values of features grouped by species."""
    feature_cols = [c for c in df.columns if c != "Species"]
    return df.groupby("Species")[feature_cols].mean().round(2).reset_index()

def get_correlation_matrix(df: pd.DataFrame) -> pd.DataFrame:
    """Calculates Pearson correlation matrix for numerical features."""
    feature_cols = [c for c in df.columns if c != "Species"]
    return df[feature_cols].corr().round(3)
