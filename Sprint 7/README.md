# Megaline Mobile 📱

[📂 View Project Notebook](./Sprint%207.ipynb)

## Overview  
Megaline is a mobile carrier looking to transition customers from outdated legacy plans to one of its newer offerings: the Smart or Ultra plan. The goal of this project was to develop a classification model that predicts which plan a customer is most likely to use based on their behavioral data.

## Objective  
- Build a model that achieves at least **0.75 accuracy** on the test dataset.  
- Compare multiple algorithms and select the best-performing one.  

## Dataset  
The dataset contains behavioral data of Smart and Ultra plan users:  
- **calls** — Number of calls made.  
- **minutes** — Total minutes of calls.  
- **messages** — Number of text messages sent.  
- **mb_used** — Internet data usage (in MB).  
- **is_ultra** — Target variable (1 for Ultra plan, 0 for Smart plan).  

## Tools & Libraries  
- **Python** (Pandas, NumPy, Scikit-learn)  
- **Matplotlib / Seaborn** for visualization  

## Methodology  
1. **Data Exploration & Preparation**:  
   - Checked for missing values and confirmed dataset integrity.  
   - Split the dataset into training, validation, and test sets.  

2. **Model Training & Tuning**:  
   - **Decision Tree Classifier** — Tuned `max_depth` from 1 to 10.  
   - **Random Forest Classifier** — Tuned `n_estimators` from 10 to 100.  
   - **Logistic Regression** — Adjusted `max_iter` to ensure convergence.  

3. **Evaluation Metrics**:  
   - Used **accuracy score** as the primary metric.  
   - Compared validation results to select the best model.  

## Results  
- **Decision Tree**: Best validation accuracy — **0.796** (`max_depth=8`)  
- **Random Forest**: Best validation accuracy — **0.802** (`n_estimators=100`)  
- **Logistic Regression**: Validation accuracy — **0.740**  
- **Final Model**: Random Forest achieved **0.812 test accuracy**.  

## Conclusion  
The **Random Forest Classifier** was selected as the best model due to its strong generalization, robustness to overfitting, and high accuracy on unseen data. It outperformed both the Decision Tree and Logistic Regression models.

## Repo Structure  
```
📦 megaline-mobile-project
 ┣ Sprint 7.ipynb   # Main analysis notebook
 ┗ README.md        # Project documentation
```

## How to Run  
Install Juypter Notebook

Open Sprint 7.ipynb

Install necessary libaries


## Author  
Kelvin Pina  
