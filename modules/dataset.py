"""
FloraAI - Dataset Module
Interface for dataset operations and session state synchronization.
"""

import pandas as pd
from utils.dataset_helpers import load_dataset, dataset_summary, feature_statistics, species_distribution

def get_cleaned_dataset() -> pd.DataFrame:
    """Retrieves and cleans the Iris dataset."""
    return load_dataset()

def get_summary_metrics(df: pd.DataFrame) -> dict:
    """Returns dataset summary metrics dictionary."""
    return dataset_summary(df)

def get_feature_table(df: pd.DataFrame) -> pd.DataFrame:
    """Returns formatted feature summary statistics table."""
    return feature_statistics(df)

def get_species_counts(df: pd.DataFrame) -> pd.DataFrame:
    """Returns species sample counts and percentages."""
    return species_distribution(df)
