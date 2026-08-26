"""
FloraAI - Training Module
Coordinates model training execution and session state caching.
"""

import pandas as pd
from utils.training_helpers import train_and_evaluate_models, MODEL_DESCRIPTIONS

def get_supported_model_descriptions() -> dict:
    """Returns model names and descriptions."""
    return MODEL_DESCRIPTIONS

def execute_model_training(df: pd.DataFrame, selected_models: list) -> tuple:
    """Executes training workflow for selected models."""
    return train_and_evaluate_models(df, selected_models)
