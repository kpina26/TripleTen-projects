# OilyGiant Mining Company — Optimal Oil Well Region Selection

## Project Overview
OilyGiant aims to identify the **most profitable** and **least risky** region for developing a new oil well.  
Geological data from three regions were analyzed, each containing features (`f0`, `f1`, `f2`) and the target variable `product`, representing the volume of reserves in thousand barrels.

A **Linear Regression** model was trained for each region using a 75:25 training-validation split, with performance evaluated using **RMSE**.  
The **top 200 wells** with the highest predicted reserves were selected for each region, and their **actual reserves** were used to calculate revenue and profit based on:
- **Budget:** $100 million
- **Revenue per thousand barrels:** $4,500

A **bootstrapping** technique with 1,000 iterations estimated average profit, 95% confidence intervals, and risk of loss.  
The **optimal region** was selected based on the highest expected profit and a loss risk **below 2.5%**.

---

## Dataset
Three datasets: `geo_data_0.csv`, `geo_data_1.csv`, `geo_data_2.csv`  
Each contains:
- `id` — unique well ID
- `f0`, `f1`, `f2` — geological features
- `product` — actual reserves (target variable)

---

## Workflow

1. **Data Exploration**
   - Checked dataset shape, data types, duplicates, and missing values.
   - Reviewed descriptive statistics for each region.

2. **Model Training**
   - Split data into training (75%) and validation (25%) sets.
   - Trained a **Linear Regression** model for each region.
   - Measured performance using **RMSE**.

3. **Profit Calculation**
   - Selected **top 200 wells** with highest predicted reserves.
   - Calculated total actual reserves, total revenue, and profit.

4. **Bootstrapping**
   - Repeated sampling 1,000 times for each region to estimate:
     - Mean profit
     - 95% confidence interval
     - Risk of loss

5. **Region Selection**
   - Chose the region with the highest expected profit and risk < 2.5%.

---

## Results

| Region | Avg Predicted Reserves | RMSE  | Total Profit     | Mean Profit     | 95% CI (Lower, Upper)       | Risk of Loss |
|--------|-----------------------|-------|------------------|-----------------|-----------------------------|--------------|
| 0      | 92.40                  | 37.76 | $33,591,411.24   | $3,928,937.05   | (-$1,030,973.68, $8,689,397.88) | 7.00%        |
| 1      | 68.71                  | 0.89  | $52,146,860.97   | $4,395,754.61   | ($481,964.46, $8,316,484.39) | **1.70%**    |
| 2      | Data not shown here    | -     | -                | -               | -                           | -            |

**Best Region to Develop:** **Region 1**  
- **Expected Profit:** $4,395,754.61  
- **Risk of Loss:** 1.70%

---

## Conclusion
Region 1 offers the highest profitability and meets the risk requirement (<2.5%).  
The model successfully identified this region as the optimal development site based on predictive modeling and statistical risk assessment.

---

## Tech Stack
- Python (Pandas, NumPy, Matplotlib, Scikit-learn)
- Linear Regression
- Bootstrapping for risk estimation

---

## How to Run

Install Juypter Notebook

Open Sprint 9.ipynb

Install necessary libaries
