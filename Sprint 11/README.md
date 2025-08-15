# Insurance Customer Analysis and Machine Learning Models

## Project Overview
This project involves an in-depth analysis of customer data to support the **Sure Tomorrow** insurance company’s marketing and prediction efforts using machine learning and linear algebra techniques.

The main objectives were:
- Identify similar customers using the **k-Nearest Neighbors (kNN)** algorithm.
- Train a classification model to predict the likelihood of a new customer receiving an insurance benefit.
- Implement and evaluate a **Linear Regression** model using **RMSE** and **R²** metrics.
- Apply **matrix transformation** techniques to protect data privacy without affecting model accuracy.

---

## Methodology
1. **Data Exploration & Preprocessing**
   - Cleaned and prepared the dataset for modeling.
   - Scaled features for kNN performance improvement.

2. **Model Development**
   - **kNN Classifier**: Measured performance compared to a dummy classifier.
   - **Linear Regression**: Predicted the number of benefits and validated using RMSE & R².

3. **Data Privacy**
   - Applied feature matrix multiplication by an invertible matrix to mask values while preserving predictive performance.

4. **Validation**
   - Confirmed that transformations did not affect accuracy or predictions.

---

## Results
- **kNN** outperformed the dummy classifier in benefit prediction.
- **Linear Regression** achieved competitive RMSE and R² values.
- Data privacy method successfully masked original features without reducing model performance.

---

## Installation & Setup
Install Juypter Notebook

Open Sprint 11.ipynb

Install necessary libaries

---

## References
- scikit-learn Documentation: https://scikit-learn.org/
- NumPy Documentation: https://numpy.org/
- Pandas Documentation: https://pandas.pydata.org/

---

## Author
Developed as part of the **TripleTen Data Science Program**.

