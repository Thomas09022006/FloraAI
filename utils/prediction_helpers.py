"""
FloraAI - Prediction Helpers Module
Inference logic, input scaling, probability estimation, and feature contributions.
"""

import pandas as pd
import numpy as np
import datetime
from modules.save_model import load_saved_model_artifact
from utils.dataset_helpers import load_dataset
from utils.training_helpers import train_and_evaluate_models
from modules.save_model import save_best_model_artifact

def get_or_create_model():
    """
    Loads saved best model artifact, or automatically trains a model if missing.
    """
    artifact = load_saved_model_artifact()
    if artifact is not None:
        return artifact, False
        
    # Auto-train default model if not saved yet
    df = load_dataset()
    results, best_name, splits = train_and_evaluate_models(df, ["Random Forest Classifier", "Logistic Regression"])
    save_best_model_artifact(results, best_name, splits)
    artifact = load_saved_model_artifact()
    return artifact, True

def predict_iris_sample(sepal_len: float, sepal_wid: float, petal_len: float, petal_wid: float, artifact: dict) -> dict:
    """
    Executes single-sample model inference for Iris species prediction.
    """
    model = artifact["model"]
    scaler = artifact.get("scaler")
    is_scaled = artifact.get("is_scaled", False)
    target_names = artifact["target_names"]
    
    feature_cols = artifact.get("feature_names", ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"])
    input_df = pd.DataFrame([[sepal_len, sepal_wid, petal_len, petal_wid]], columns=feature_cols)
    
    if is_scaled and scaler is not None:
        input_data_eval = scaler.transform(input_df)
    else:
        input_data_eval = input_df
        
    pred_idx = model.predict(input_data_eval)[0]
    predicted_species = target_names[pred_idx]
    
    # Calculate probabilities
    if hasattr(model, "predict_proba"):
        probs = model.predict_proba(input_data_eval)[0]
    else:
        # Distance-based fallback approximation if predict_proba unavailable
        probs = np.zeros(len(target_names))
        probs[pred_idx] = 1.0
        
    prob_dict = {target_names[i]: float(probs[i]) for i in range(len(target_names))}
    confidence_pct = float(probs[pred_idx] * 100)
    
    # Measurement summary table
    measurement_table = pd.DataFrame([
        {"Feature": "Sepal Length (cm)", "Value": f"{sepal_len:.2f}"},
        {"Feature": "Sepal Width (cm)", "Value": f"{sepal_wid:.2f}"},
        {"Feature": "Petal Length (cm)", "Value": f"{petal_len:.2f}"},
        {"Feature": "Petal Width (cm)", "Value": f"{petal_wid:.2f}"},
        {"Feature": "Predicted Species", "Value": predicted_species},
        {"Feature": "Confidence Score", "Value": f"{confidence_pct:.1f}%"}
    ])
    
    return {
        "species": predicted_species,
        "confidence": confidence_pct,
        "probabilities": prob_dict,
        "model_name": artifact["model_name"],
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "measurement_table": measurement_table,
        "importance_df": artifact.get("importance_df")
    }
