# Beta Bank Customer Churn Prediction

## Project Overview  
Beta Bank is experiencing customer churn, where clients are gradually leaving the service each month. To reduce losses and retain customers, the bank aims to **predict which clients are likely to leave** in the near future using historical behavioral data.  

The primary goal is to build a classification model that can accurately predict customer churn and **maximize the F1 score**, with a target of **≥ 0.59** on the test set. The project also evaluates the **AUC-ROC** metric to assess the model’s ability to distinguish between classes.  

To address class imbalance, we implemented **upsampling (SMOTE)**, **downsampling**, and **class weight adjustments**.

---

## Dataset  
The dataset contains **10,000 entries** with 14 features, including customer demographics, account information, and activity history.  

Key columns:  
- **CreditScore** – Customer’s credit rating  
- **Geography** – Customer’s country  
- **Gender** – Male/Female  
- **Age**, **Tenure**, **Balance** – Customer profile data  
- **NumOfProducts** – Number of bank products used  
- **HasCrCard**, **IsActiveMember** – Account indicators  
- **EstimatedSalary** – Approximate annual income  
- **Exited** – Target variable (1 = churned, 0 = retained)

---

## Project Workflow  

1. **Data Preprocessing**  
   - Standardized column names  
   - Handled missing values in `tenure` (median imputation)  
   - Dropped irrelevant identifiers (`RowNumber`, `CustomerId`, `Surname`)  
   - Encoded categorical variables using `LabelEncoder` and `OneHotEncoder`  

2. **Exploratory Data Analysis (EDA)**  
   - Checked for duplicates and missing values  
   - Analyzed class imbalance  
   - Reviewed feature distributions and correlations  

3. **Modeling**  
   - Models tested:  
     - Logistic Regression  
     - Decision Tree Classifier  
     - Random Forest Classifier  
   - Applied **GridSearchCV** for hyperparameter tuning  
   - Implemented:
     - **Class Weight Balancing**
     - **SMOTE Upsampling**
     - **Downsampling**

4. **Evaluation Metrics**  
   - **F1 Score** – primary metric  
   - **AUC-ROC** – secondary metric  
   - ROC curve visualization for the best model  

---

## Results  

| Model               | F1 Score (Val) | AUC (Val) |
|--------------------|---------------|-----------|
| Logistic Regression | 0.4625        | 0.7255    |
| Decision Tree       | 0.5042        | 0.7021    |
| Random Forest       | **0.5957**    | **0.8530** |

- **Best Model:** Random Forest Classifier (with downsampling)  
- **Test Set Performance:**  
  - **F1 Score:** 0.6085  
  - **AUC-ROC:** 0.833  
- ROC curve shows strong class separation despite F1 being slightly below the target.

---

## ROC Curve – Best Model (Random Forest)
![ROC Curve](roc_curve_random_forest.png)

---

## Conclusion  
- The **Random Forest Classifier** with downsampling achieved the best results, demonstrating strong discrimination between churned and retained customers.  
- Final F1 score was **0.6085** and AUC-ROC was **0.833**.  
- While slightly below the desired F1 threshold, the model shows potential and could be improved further through:  
  - Threshold tuning  
  - Additional feature engineering  
  - Ensemble methods  

---

## Tech Stack  
- **Python** (Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, Imbalanced-learn)  
- **Jupyter Notebook / VS Code**  
- **Machine Learning Models:** Logistic Regression, Decision Tree, Random Forest  

---

## How to Run  

Install Juypter Notebook

Open Sprint 8.ipynb

Install necessary libaries
