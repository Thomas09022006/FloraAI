"""
FloraAI - Botanical Recommendation Module
Generates botanical recommendations based on flower measurement inputs.
"""

from modules.insights import generate_prediction_rule_insights

def get_prediction_recommendations(sepal_len: float, sepal_wid: float, petal_len: float, petal_wid: float, species: str, confidence: float) -> list:
    """Generates botanical insights and recommendations for the predicted sample."""
    return generate_prediction_rule_insights(sepal_len, sepal_wid, petal_len, petal_wid, species, confidence)
