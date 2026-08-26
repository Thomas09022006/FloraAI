"""
FloraAI - Training Helpers Module
Core Machine Learning pipelines, model training, cross-validation, and metrics computation.
"""

import time
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

MODEL_FACTORY = {
    "Logistic Regression": lambda: LogisticRegression(max_iter=200, random_state=42),
    "Decision Tree Classifier": lambda: DecisionTreeClassifier(random_state=42),
    "Random Forest Classifier": lambda: RandomForestClassifier(n_estimators=100, random_state=42),
    "K-Nearest Neighbors": lambda: KNeighborsClassifier(n_neighbors=5)
}

MODEL_DESCRIPTIONS = {
    "Logistic Regression": "Linear classification model using sigmoid function for probability estimation.",
    "Decision Tree Classifier": "Tree-based model splitting data on feature thresholds to maximize information gain.",
    "Random Forest Classifier": "Ensemble of decision trees voting to achieve high accuracy and prevent overfitting.",
    "K-Nearest Neighbors": "Non-parametric instance-based classifier assigning class by majority neighbor vote."
}

def train_and_evaluate_models(df: pd.DataFrame, selected_models: list, test_size: float = 0.2, random_state: int = 42) -> tuple:
    """
    Trains selected ML models on the Iris dataset and computes evaluation metrics.
    Returns: (results_dict, best_model_name, dataset_splits)
    """
    feature_cols = [c for c in df.columns if c != "Species"]
    X = df[feature_cols]
    y = df["Species"]
    
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)
    target_names = label_encoder.classes_.tolist()
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_encoded, test_size=test_size, random_state=random_state, stratify=y_encoded
    )
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    results = {}
    
    for model_name in selected_models:
        if model_name not in MODEL_FACTORY:
            continue
            
        model = MODEL_FACTORY[model_name]()
        
        # Scale for LR & KNN, raw for Decision Tree & Random Forest for direct interpretability
        use_scaled = model_name in ["Logistic Regression", "K-Nearest Neighbors"]
        X_tr = X_train_scaled if use_scaled else X_train.values
        X_te = X_test_scaled if use_scaled else X_test.values
        
        start_time = time.time()
        model.fit(X_tr, y_train)
        elapsed_time = time.time() - start_time
        
        y_pred = model.predict(X_te)
        
        acc = accuracy_score(y_test, y_pred)
        prec = precision_score(y_test, y_pred, average="macro")
        rec = recall_score(y_test, y_pred, average="macro")
        f1 = f1_score(y_test, y_pred, average="macro")
        
        # Cross validation
        cv_scores = cross_val_score(model, X_tr, y_train, cv=5, scoring="accuracy")
        cv_mean = cv_scores.mean()
        
        # Confusion matrix
        cm = confusion_matrix(y_test, y_pred)
        
        # Classification report dict
        clf_rep = classification_report(y_test, y_pred, target_names=target_names, output_dict=True)
        
        # Feature Importance / Coefficients
        importance_df = None
        if hasattr(model, "feature_importances_"):
            importance_df = pd.DataFrame({
                "Feature": [c.replace("Cm", " (cm)") for c in feature_cols],
                "Importance": model.feature_importances_
            }).sort_values("Importance", ascending=False)
        elif hasattr(model, "coef_"):
            # Average absolute coefficients across classes
            coef_mean = np.mean(np.abs(model.coef_), axis=0)
            importance_df = pd.DataFrame({
                "Feature": [c.replace("Cm", " (cm)") for c in feature_cols],
                "Importance": coef_mean
            }).sort_values("Importance", ascending=False)
            
        results[model_name] = {
            "model": model,
            "scaler": scaler if use_scaled else None,
            "is_scaled": use_scaled,
            "accuracy": acc,
            "precision": prec,
            "recall": rec,
            "f1_score": f1,
            "cv_score": cv_mean,
            "training_time": elapsed_time,
            "confusion_matrix": cm,
            "classification_report": clf_rep,
            "importance_df": importance_df,
            "predictions": y_pred,
            "y_test": y_test
        }
        
    # Best model selection (highest accuracy, then highest F1)
    best_model_name = max(results.keys(), key=lambda m: (results[m]["accuracy"], results[m]["f1_score"]))
    
    splits_info = {
        "train_samples": len(X_train),
        "test_samples": len(X_test),
        "num_features": len(feature_cols),
        "num_classes": len(target_names),
        "target_names": target_names,
        "feature_names": feature_cols,
        "label_encoder": label_encoder
    }
    
    return results, best_model_name, splits_info
