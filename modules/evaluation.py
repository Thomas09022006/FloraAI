"""
FloraAI - Evaluation Module
Formats evaluation metrics, confusion matrix, and classification report data.
"""

import pandas as pd

def format_classification_report_table(clf_report_dict: dict) -> pd.DataFrame:
    """Formats classification report dictionary into a clean DataFrame table."""
    rows = []
    for key, val in clf_report_dict.items():
        if isinstance(val, dict):
            rows.append({
                "Class / Metric": key,
                "Precision": round(val["precision"], 3),
                "Recall": round(val["recall"], 3),
                "F1-Score": round(val["f1-score"], 3),
                "Support": int(val["support"])
            })
    return pd.DataFrame(rows)
