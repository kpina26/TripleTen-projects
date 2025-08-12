# Telecom Customer Churn Prediction

## Project Overview
The goal of this project was to predict **customer churn** for a telecom company using historical customer data.  
The task required achieving an **F1 score of at least 0.59** on the test set.  
Various preprocessing techniques, resampling strategies, and classification models were tested to improve performance, with a focus on **handling class imbalance**.

---

## Dataset
The dataset includes customer account details, contract types, demographics, and service usage information.  
The target variable is:
- **Churn** — 1 if the customer left, 0 if retained

---

## Workflow

1. **Data Preprocessing**
   - Removed irrelevant features (`customerID`)
   - Converted categorical features to numerical format using encoding
   - Checked and handled missing values
   - Standardized numerical features for model training

2. **Exploratory Data Analysis (EDA)**
   - Examined feature distributions and relationships with churn
   - Checked for class imbalance
   - Visualized categorical vs. churn rates

3. **Resampling for Class Imbalance**
   - Tested **Downsampling** and **SMOTE Upsampling**
   - Applied **class weight balancing** for models

4. **Modeling**
   - Tested the following models:
     - Logistic Regression
     - Decision Tree Classifier
     - Random Forest Classifier
   - Used **validation sets** to compare models on F1 score and AUC-ROC

5. **Model Selection & Final Testing**
   - Chose the best model based on validation results
   - Retrained on upsampled training data
   - Evaluated on the test set

---

## Results

| Model               | F1 Score (Val) | AUC (Val) |
|--------------------|---------------|-----------|
| Logistic Regression | 0.4625        | 0.7255    |
| Decision Tree       | 0.5042        | 0.7021    |
| Random Forest       | **0.5957**    | **0.8530** |

**Best Model:** Random Forest Classifier (with downsampling)  
**Test Set Performance:**
- **F1 Score:** 0.6085  
- **AUC-ROC:** 0.833

---

## ROC Curve – Random Forest
![ROC Curve](roc_curve_random_forest.png)

---

## Conclusion
- The **Random Forest Classifier** performed best, exceeding the target F1 score.
- The model shows strong separation ability (AUC = 0.833) and is suitable for deployment.
- Possible improvements:
  - Threshold tuning for optimal F1
  - Adding new engineered features
  - Testing advanced models (XGBoost, LightGBM)

---

## Tech Stack
- Python (Pandas, NumPy, Matplotlib, Scikit-learn, Imbalanced-learn)
- Jupyter Notebook / VS Code
- Machine Learning Models: Logistic Regression, Decision Tree, Random Forest

---

## How to Run

1. Clone this repository:
```bash
git clone https://github.com/yourusername/telecom-churn-prediction.git
```
2. Navigate to the project folder:
```bash
cd telecom-churn-prediction
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Run the Jupyter Notebook:
```bash
jupyter notebook
```
