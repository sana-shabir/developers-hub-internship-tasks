# 🧠 Internship Tasks — Data Science & Machine Learning
### Developers Hub Corporation | Sana Shabir

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat&logo=python&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0?style=flat&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat)
![Internship](https://img.shields.io/badge/Internship-Developers%20Hub-blue?style=flat)

---

## 📋 Overview

This repository contains **3 Data Science & Machine Learning tasks** completed during my internship at **Developers Hub Corporation**. The tasks cover EDA, unsupervised learning (clustering), and supervised learning (classification).

---

## 📂 Repository Structure
📦 developershub-internship
┣ 📜 internship task1.py   → Iris Dataset — EDA & Visualization

┣ 📜 internship task2.py   → Loan Dataset — Clustering & Risk Analysis

┗ 📜 internship task3.py   → Customer Churn — Classification & Feature Importance

---

## 🎯 Task Descriptions

### Task 1 — Iris Dataset Analysis (EDA)
![EDA](https://img.shields.io/badge/Type-Exploratory%20Data%20Analysis-9cf?style=flat)
![Dataset](https://img.shields.io/badge/Dataset-Iris-lightgrey?style=flat)

Performed comprehensive EDA on the classic Iris dataset:

- 📊 Data inspection and summary statistics
- 🔵 Scatter plots — petal & sepal dimensions by species
- 📉 Histogram distribution analysis
- 📦 Box plot comparisons across species

---

### Task 2 — Credit Risk Analysis (Unsupervised Learning)
![ML](https://img.shields.io/badge/Type-Unsupervised%20Learning-orange?style=flat)
![Algorithm](https://img.shields.io/badge/Algorithm-KMeans%20Clustering-yellow?style=flat)
![Dataset](https://img.shields.io/badge/Dataset-Loan%20Application-lightgrey?style=flat)

Analyzed loan application data using **K-Means Clustering** to identify credit risk groups:

- 🧹 Missing value imputation (mode for categorical, median for numerical)
- 🔤 Label encoding for categorical variables
- 📊 Loan amount & applicant income distribution
- 🎯 K-Means clustering (2 clusters) → Low Risk vs High Risk groups

**Features Used:**
`Gender` · `Married` · `Dependents` · `Education` · `Self_Employed` · `LoanAmount` · `Credit_History`

---

### Task 3 — Customer Churn Prediction (Supervised Learning)
![ML](https://img.shields.io/badge/Type-Supervised%20Learning-red?style=flat)
![Algorithm](https://img.shields.io/badge/Algorithm-Random%20Forest-brightgreen?style=flat)
![Dataset](https://img.shields.io/badge/Dataset-Bank%20Churn-lightgrey?style=flat)
![Accuracy](https://img.shields.io/badge/Accuracy-85--86%25-success?style=flat)

Built a **Random Forest Classifier** to predict customer churn for a banking institution:

- 🗑️ Removed irrelevant columns (RowNumber, CustomerId, Surname)
- 🔤 Label encoding for Gender & Geography
- 🌲 Random Forest Classifier (80/20 train-test split)
- 📈 Feature importance analysis

**Model Performance:**

| Metric | Score |
|---|---|
| ✅ Accuracy | ~85–86% |
| 🎯 Target Variable | Exited (Churn) |
| 🌲 Algorithm | Random Forest |
| 🔀 Train/Test Split | 80 / 20 |

---

## 🔧 Installation & Requirements

```bash
pip install pandas matplotlib seaborn scikit-learn numpy
```

| Library | Purpose |
|---|---|
| ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white) | Data manipulation |
| ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat&logo=python&logoColor=white) | Data visualization |
| ![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0?style=flat&logo=python&logoColor=white) | Statistical visualizations |
| ![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white) | Machine learning models |

---

## 🚀 Usage

```bash
# Task 1 — Iris EDA
python "internship task1.py"

# Task 2 — Credit Risk (update CSV path first)
python "internship task2.py"

# Task 3 — Churn Prediction (update CSV path first)
python "internship task3.py"
```

> ⚠️ **Note:** Update the CSV file paths in Task 2 and Task 3 to match your local directory before running.

---

## 📁 Dataset Information

| Task | Dataset | Size |
|---|---|---|
| Task 1 | Iris (built-in seaborn) | 150 rows × 5 cols |
| Task 2 | Loan Application (CSV) | ~614 rows × 13 cols |
| Task 3 | Customer Churn (CSV) | ~10,000 rows × 14 cols |

---

## ✅ Key Learnings

- 🔍 **EDA** — Statistical summaries and meaningful visualizations
- 🧹 **Data Preprocessing** — Handling missing values & encoding
- 🤖 **Unsupervised Learning** — K-Means clustering for pattern discovery
- 🌲 **Supervised Learning** — Random Forest for classification
- 📊 **Model Evaluation** — Accuracy, confusion matrix, F1-score
- 📈 **Feature Importance** — Understanding what drives predictions

---

## 👩‍💻 Author

**Sana Shabir**
Data Science Intern @ Developers Hub Corporation

[![GitHub](https://img.shields.io/badge/GitHub-sana--shabir-181717?style=flat&logo=github&logoColor=white)](https://github.com/sana-shabir)
[![Email](https://img.shields.io/badge/Gmail-sanashabir2233@gmail.com-D14836?style=flat&logo=gmail&logoColor=white)](mailto:sanashabir2233@gmail.com)
