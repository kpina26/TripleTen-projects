# Customer Churn Prediction Project

## Project Overview
This project focuses on predicting customer churn using various machine learning models, including Decision Tree, Random Forest, XGBoost, and LightGBM. The goal was to achieve an **AUC-ROC score of 0.87 or above** while ensuring data preprocessing, feature engineering, and model optimization steps were thoroughly implemented.

## Steps Performed
- Loaded and merged datasets (`contract`, `personal`, `internet`, and `phone`) using `customerID`.
- Performed **data cleaning**:
  - Converted date columns to datetime format.
  - Handled missing values in `TotalCharges` by coercing to numeric and dropping null rows.
  - Filled nulls in `MultipleLines` with `"No phone service"`.
- Created new features: **Churn** and **Tenure**.
- Conducted **Exploratory Data Analysis (EDA)** to identify trends by contract type, tenure, and monthly charges.
- Implemented preprocessing pipelines for categorical and numerical features.
- Trained models: Decision Tree, Random Forest, XGBoost, LightGBM.
- Tuned hyperparameters using **GridSearchCV** with optimized parameter grids to reduce runtime.
- Evaluated models using **AUC-ROC**.

## Challenges & Solutions
- **Missing Values**: Handled with coercion to numeric and dropping nulls.
- **Unclear Categorical Values**: Filled missing categorical data logically.
- **Unbalanced Classes**: Used train-test split strategy to maintain class balance.
- **Long Runtimes in XGBoost & LightGBM**: Reduced parameter ranges and optimized GridSearchCV.

## 🚀 Results
| Model     | AUC-ROC Score |
|-----------|--------------|
| XGBoost   | **0.8905**   |
| LightGBM  | **0.8927**   |

✅ Both models exceeded the target score of **0.87**, showing strong performance in predicting customer churn.

## Repository Structure
```
├── data/               # Raw and processed datasets
├── notebooks/          # Jupyter notebooks with analysis and modeling
├── README.md           # Project documentation
└── requirements.txt    # Dependencies
```

## Tools & Libraries Used
- Python
- Pandas, NumPy
- Scikit-learn
- XGBoost, LightGBM
- Matplotlib, Seaborn

## How to Run the Project

Install Juypter Notebook

Open Sprint 17.ipynb

Install necessary libaries

## License
This project is licensed under the MIT License.

---
**Author:** Kelvin Pina
