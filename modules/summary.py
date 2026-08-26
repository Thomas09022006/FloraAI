"""
FloraAI - Summary Module
Aggregates project metadata and workflow timeline data.
"""

from utils.summary_helpers import get_project_stats_kpis, get_ml_workflow_steps

def get_summary_kpis() -> dict:
    """Returns summary KPI metrics."""
    return get_project_stats_kpis()

def get_workflow_timeline() -> list:
    """Returns ML workflow timeline steps."""
    return get_ml_workflow_steps()
