# Rusty Bargain Used Car Sales Price Prediction

## Overview
Rusty Bargain is a used car sales service aiming to develop a predictive tool to help users estimate the market value of their vehicles based on historical listings. This project explores multiple regression-based machine learning models to predict car prices using historical technical specifications, trim levels, registration details, and market data.

The dataset includes:
- **Technical Specifications**: Model, brand, gearbox type, power, fuel type, etc.
- **Registration Details**: Year, month, postal code.
- **Market Data**: Date crawled, date created, last seen, price.

The models were evaluated on **RMSE** (Root Mean Squared Error), training time, and prediction time.

---

## Project Workflow

### 1. Data Loading & Initial Exploration
- Imported necessary libraries: NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn, LightGBM.
- Loaded the dataset (`car_data.csv`) and reviewed structure, types, and sample entries.

### 2. Data Preprocessing
- **Column name standardization** to lowercase with underscores.
- Converted date-related columns to `datetime` objects.
- Removed irrelevant columns such as `number_of_pictures`.
- Handled missing values:
  - Filled `vehicle_type`, `gearbox`, `model`, `fuel_type`, and `not_repaired` with `"unknown"`.
  - Replaced zero months in `registration_month` with the mode of valid months.
  - Replaced unrealistic `power` values with mode of valid range (20–1000).
- Removed duplicates and filtered out extreme price outliers using the IQR method.
- One-hot encoded categorical variables.

### 3. Exploratory Data Analysis (EDA)
- Visualized **price distribution**.
- Compared **price by vehicle type** using boxplots.
- Observed heavy right skew in price distribution and notable variation across vehicle categories.

### 4. Model Training & Hyperparameter Tuning
Models tested:
1. **Linear Regression** (baseline)
2. **Decision Tree Regressor** (GridSearchCV for hyperparameter tuning)
3. **Random Forest Regressor** (GridSearchCV for hyperparameter tuning)
4. **LightGBM Regressor** (GridSearchCV for hyperparameter tuning)

### 5. Model Evaluation
Evaluated models based on:
- RMSE (lower is better)
- Training time
- Prediction time

| Model            | RMSE     | Training Time (sec) | Prediction Time (sec) |
|------------------|----------|---------------------|------------------------|
| Linear Regression| 2364.52  | 7.73                 | 0.1151                 |
| Decision Tree    | 1586.71  | 233.62               | 0.0871                 |
| Random Forest    | 1418.61  | 1013.37              | 1.4630                 |
| LightGBM         | **1376.63** | 93.84                | 0.6120                 |

---

## Conclusion
- **LightGBM** delivered the best performance with the lowest RMSE of **1376.63**, balanced training time, and fast predictions.
- **Random Forest** achieved competitive RMSE but had the slowest training and prediction times.
- **Decision Tree** improved accuracy over Linear Regression but was slower.
- **Linear Regression** served as a baseline with the fastest training and prediction speeds but the highest error.

**Final Choice:** LightGBM — best balance of accuracy and efficiency.

---

## How to Run
1. Clone the repository:
```bash
git clone <your-repo-link>
cd <your-repo-folder>
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Place the dataset in the `datasets/` folder as `car_data.csv`.
4. Run the Jupyter Notebook:
```bash
jupyter notebook Sprint_12.ipynb
```

---

## Technologies Used
- Python (Pandas, NumPy, Matplotlib, Seaborn)
- Scikit-learn
- LightGBM
- Jupyter Notebook

---

## Author
Kelvin Pina
