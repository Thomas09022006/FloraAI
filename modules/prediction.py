"""
FloraAI - Prediction Module
Execution wrapper for single-sample Iris flower prediction.
"""

from utils.prediction_helpers import get_or_create_model, predict_iris_sample

def load_prediction_model():
    """Loads prediction model artifact and returns auto-trained status."""
    return get_or_create_model()

def make_prediction(sepal_len: float, sepal_wid: float, petal_len: float, petal_wid: float, artifact: dict) -> dict:
    """Executes single sample flower prediction."""
    return predict_iris_sample(sepal_len, sepal_wid, petal_len, petal_wid, artifact)
