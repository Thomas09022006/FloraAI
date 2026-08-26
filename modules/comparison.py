"""
FloraAI - Comparison Module
Compares trained models and selects the top-performing classifier.
"""

import pandas as pd

def build_comparison_dataframe(results: dict) -> pd.DataFrame:
    """Builds a formatted comparison table for all trained models."""
    rows = []
    for model_name, res in results.items():
        rows.append({
            "Model Name": model_name,
            "Accuracy": round(res["accuracy"], 4),
            "Precision": round(res["precision"], 4),
            "Recall": round(res["recall"], 4),
            "F1 Score": round(res["f1_score"], 4),
            "CV Score": round(res["cv_score"], 4),
            "Training Time (s)": round(res["training_time"], 4)
        })
    df_comp = pd.DataFrame(rows)
    return df_comp.sort_values(by=["Accuracy", "F1 Score"], ascending=False).reset_index(drop=True)

def get_best_model_details(results: dict, best_model_name: str) -> dict:
    """Returns detailed metrics and justification for the best model."""
    best = results[best_model_name]
    return {
        "name": best_model_name,
        "accuracy": best["accuracy"],
        "f1_score": best["f1_score"],
        "cv_score": best["cv_score"],
        "training_time": best["training_time"],
        "reason": f"{best_model_name} achieved the highest cross-validated classification accuracy ({best['accuracy']*100:.1f}%) and optimal F1-score balance across all species."
    }
