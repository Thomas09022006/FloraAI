# 🌸 FloraAI – AI-Powered Iris Flower Classification Platform

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.3+-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-5.17+-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**FloraAI** is a modern Botanical Machine Learning Web Application designed for interactive exploration, model training, performance evaluation, and real-time species prediction of Iris flowers (*Setosa*, *Versicolor*, and *Virginica*).

Designed with a sleek **Botanical Glassmorphism UI**, custom dark purple sidebars, nature-inspired gradients, and interactive Plotly visualizations.

---

## 🌟 Key Features

1. **🌸 Home Dashboard**
   - Botanical Hero banner & quick navigation CTAs.
   - Machine Learning problem overview & real-world applications in botany and smart agriculture.
   - Interactive progress stepper and project stats.

2. **🌿 Iris Dataset Explorer**
   - KPI metrics (150 samples, 4 features, 3 species, missing values, duplicates).
   - Statistical feature summaries (min, max, mean, median, standard deviation).
   - Interactive Plotly Donut Chart & Bar Chart for species balance.
   - Histograms & Box Plots with interactive feature selection.
   - Heatmap correlation matrix & pairwise scatter matrix.
   - Searchable, scrollable dataset preview table.

3. **🤖 AI Model Training Center**
   - Train 4 Machine Learning classifiers:
     - **Logistic Regression**
     - **Decision Tree Classifier**
     - **Random Forest Classifier**
     - **K-Nearest Neighbors (KNN)**
   - 5-Fold Stratified Cross Validation and 80/20 train-test split.
   - Interactive model comparison table & grouped metric bar chart.
   - Confusion matrices, classification reports, and feature importance/coefficient charts.
   - Automatic best model selection and saving to `models/best_model.joblib`.
   - Downloadable model binary (`.joblib`) and metrics CSV files.

4. **🌸 AI Flower Species Predictor**
   - Interactive measurement sliders (Sepal Length, Sepal Width, Petal Length, Petal Width).
   - One-click specimen presets (Setosa, Versicolor, Virginica).
   - Real-time model inference with confidence percentage and probability distribution chart.
   - Plotly Confidence Gauge.
   - Botanical species profile cards (color, traits, native distribution, interesting facts).
   - Download prediction summary CSV.

5. **🎯 Project Summary & Final Polish**
   - Executive dashboard summarizing the end-to-end ML pipeline.
   - Architecture tree view, tech stack breakdown, local setup commands, and Streamlit Cloud deployment guide.

---

## 📂 Project Architecture

```text
FloraAI/
├── app.py                     # Main Streamlit Entry Point
├── requirements.txt           # Python Dependencies
├── README.md                  # Project Documentation
├── data/
│   └── Iris.csv               # Iris Botanical Dataset (150 samples)
├── models/
│   └── best_model.joblib      # Saved Model Artifact
├── pages/
│   ├── 1_Home.py              # 🌸 Home Dashboard
│   ├── 2_Dataset_Explorer.py  # 🌿 Iris Dataset Explorer
│   ├── 3_Model_Training.py    # 🤖 AI Model Training Center
│   ├── 4_Flower_Predictor.py  # 🌸 AI Flower Species Predictor
│   └── 5_Project_Summary.py   # 🎯 Project Summary
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
    └── summary_helpers.py
```

---

## 🚀 Quick Start Guide

### 1. Clone the Repository
```bash
git clone https://github.com/Thomas09022006/FloraAI.git
cd FloraAI
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Launch Application
```bash
streamlit run app.py
```

Access the dashboard at `http://localhost:8501`.

---

## ☁️ Deployment

### Streamlit Community Cloud
1. Push this repository to GitHub.
2. Log into [share.streamlit.io](https://share.streamlit.io).
3. Select repository `FloraAI` and branch `main`.
4. Set **Main file path** to `app.py`.
5. Click **Deploy!**

---

## 📜 License

This project is open-source under the **MIT License**.
