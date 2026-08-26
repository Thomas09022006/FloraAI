"""
FloraAI - Model Persistence Module
Saves and loads trained models and pipeline artifacts using joblib.
"""

import os
import joblib

MODEL_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "models")
DEFAULT_MODEL_PATH = os.path.join(MODEL_DIR, "best_model.joblib")

def save_best_model_artifact(results: dict, best_model_name: str, splits_info: dict, file_path: str = DEFAULT_MODEL_PATH) -> bool:
    """
    Saves the complete inference pipeline artifact (model, scaler, encoders, features) to disk.
    """
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    best_res = results[best_model_name]
    
    artifact = {
        "model_name": best_model_name,
        "model": best_res["model"],
        "scaler": best_res["scaler"],
        "is_scaled": best_res["is_scaled"],
        "feature_names": splits_info["feature_names"],
        "target_names": splits_info["target_names"],
        "label_encoder": splits_info["label_encoder"],
        "accuracy": best_res["accuracy"],
        "f1_score": best_res["f1_score"],
        "importance_df": best_res["importance_df"]
    }
    
    joblib.dump(artifact, file_path)
    return True

def load_saved_model_artifact(file_path: str = DEFAULT_MODEL_PATH) -> dict:
    """
    Loads saved model pipeline artifact if exists.
    """
    if not os.path.exists(file_path):
        # Fallback path check
        file_path = os.path.join(os.getcwd(), "models", "best_model.joblib")
        if not os.path.exists(file_path):
            return None
            
    try:
        artifact = joblib.load(file_path)
        return artifact
    except Exception:
        return None
