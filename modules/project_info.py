"""
FloraAI - Project Information Module
Metadata regarding technology stack, features, and folder structure.
"""

def get_tech_stack_info() -> list:
    """Returns technology stack details."""
    return [
        {"name": "Python 3.10+", "category": "Language", "desc": "Core programming language.", "icon": "🐍"},
        {"name": "Streamlit", "category": "Frontend Framework", "desc": "Interactive web dashboard UI.", "icon": "👑"},
        {"name": "Scikit-Learn", "category": "Machine Learning", "desc": "Classification models, preprocessing & metrics.", "icon": "⚙️"},
        {"name": "Pandas & NumPy", "category": "Data Processing", "desc": "Dataframes, numerical arrays, and EDA.", "icon": "🐼"},
        {"name": "Plotly Express", "category": "Data Visualization", "desc": "Interactive, modern charts.", "icon": "📈"},
        {"name": "Joblib", "category": "Persistence", "desc": "Serializing and loading trained models.", "icon": "💾"}
    ]

def get_folder_architecture_text() -> str:
    """Returns folder structure tree as text."""
    return """FloraAI/
├── app.py                     # Main Streamlit Entry Point
├── requirements.txt           # Dependencies
├── README.md                  # Project Documentation
├── data/
│   └── Iris.csv               # Dataset (150 samples)
├── models/
│   └── best_model.joblib      # Saved ML Model Pipeline Artifact
├── pages/
│   ├── 1_Home.py              # 🌸 Home Dashboard
│   ├── 2_Dataset_Explorer.py  # 🌿 Iris Dataset Explorer
│   ├── 3_Model_Training.py    # 🤖 AI Model Training Center
│   ├── 4_Flower_Predictor.py  # 🌸 AI Flower Species Predictor
│   └── 5_Project_Summary.py   # 🎯 Project Summary & Final Polish
├── modules/                   # Business Logic & Model Processing
│   ├── dataset.py
│   ├── eda.py
│   ├── visualization.py
│   ├── insights.py
│   ├── training.py
│   ├── evaluation.py
│   ├── comparison.py
│   ├── save_model.py
│   ├── prediction.py
│   ├── flower_information.py
│   ├── recommendation.py
│   ├── summary.py
│   ├── deployment.py
│   └── project_info.py
└── utils/                     # UI, Dataset & ML Helper Utilities
    ├── ui_helpers.py
    ├── dataset_helpers.py
    ├── training_helpers.py
    ├── prediction_helpers.py
    └── summary_helpers.py"""
