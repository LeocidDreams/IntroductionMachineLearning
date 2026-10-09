# Microsoft Introduction to Machine Learning — Study Notes & Projects

This repository contains code, notes, and practical exercises completed as part of Microsoft's **Introduction to Machine Learning** path. It covers core machine learning concepts, supervised and unsupervised learning algorithms, and model evaluation techniques using Python and Scikit-Learn.

---

## 📌 Repository Overview

* **Goal:** Understand foundational ML algorithms and learn how to build, evaluate, and tune models.
* **Primary Language:** Python 3.x
* **Key Libraries:** `scikit-learn`, `pandas`, `numpy`, `matplotlib`, `seaborn`

---

## 🧠 Topics Covered

### 1. Fundamentals & Workflow

* Data preprocessing, cleaning, and feature engineering
* Train-test splits and avoiding data leakage
* Exploratory Data Analysis (EDA)

### 2. Supervised Learning

* **Regression:** Linear Regression, Polynomial Regression, Ridge/Lasso
* **Classification:** Logistic Regression, Decision Trees, Random Forests, Support Vector Machines (SVM)
* Model metrics: RMSE, $R^2$, Accuracy, Precision, Recall, F1-Score, ROC-AUC

### 3. Unsupervised Learning

* **Clustering:** K-Means, Hierarchical Clustering
* **Dimensionality Reduction:** Principal Component Analysis (PCA)

### 4. Model Selection & Optimization

* Hyperparameter tuning using `GridSearchCV` and `RandomizedSearchCV`
* Cross-validation strategies ($k$-fold)

---

## 📁 Structure

```text
.
├── notebooks/
│   ├── 01_data_preprocessing.ipynb
│   ├── 02_regression_models.ipynb
│   ├── 03_classification_models.ipynb
│   └── 04_clustering_pca.ipynb
├── data/                  # Sample datasets used in exercises
├── scripts/               # Helper Python modules
├── requirements.txt       # Dependencies
└── README.md

```

---

## 🛠️ Quickstart

1. **Clone the repository:**
```bash
git clone https://github.com/your-username/repository-name.git
cd repository-name

```


2. **Create and activate a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

```


3. **Install dependencies:**
```bash
pip install -r requirements.txt

```


4. **Launch Jupyter Notebook:**
```bash
jupyter notebook

```



---

## 📜 Acknowledgments & Certificate

* Course provided by **Microsoft Learn**.
* Special thanks to the Microsoft Learn community and open-source contributors for dataset access.
