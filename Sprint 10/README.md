# Mining Plant — Predicting Gold Recovery (sMAPE)

## Project Overview
Objective: **predict metal recovery** at a mining plant at two stages — **Rougher** and **Final** — and evaluate models with a **weighted sMAPE** metric (25% Rougher, 75% Final).  
The work mirrors an industrial ML pipeline: data audit → cleaning & EDA → feature alignment for train/test → model training with cross‑validation → test evaluation vs a **dummy baseline**.

---

## Data
Three CSV files were provided:
- `gold_recovery_train.csv` — training data (features + targets)
- `gold_recovery_test.csv` — test data (features only)
- `gold_recovery_full.csv` — full dataset for EDA

Key groups of features (examples):
- **Inputs & states**: `rougher.input.*`, `primary_cleaner.*`, `secondary_cleaner.*`
- **Outputs (targets)**: `rougher.output.recovery`, `final.output.recovery`
- **Concentrations** by stage for Au/Ag/Pb/Sol: `*.concentrate_au`, `*.concentrate_ag`, `*.concentrate_pb`, `*.concentrate_sol`

**Targets**
- `rougher.output.recovery` (Rougher stage)
- `final.output.recovery` (Final stage)

---

## Metric
**sMAPE** (symmetric Mean Absolute Percentage Error) for each target; project score is the weighted average:  
\( \text{FinalScore} = 0.25\cdot sMAPE_{rougher} + 0.75\cdot sMAPE_{final} \)

---

## Workflow

1. **Data Audit & Alignment**
   - Checked shapes, dtypes, duplicates, and missing values.
   - Ensured that **train/test have consistent feature sets** (removed columns absent in test before training).

2. **Quality Cleaning**
   - Recreated total metal concentration at three stages (raw input, rougher output, final output) and **removed abnormal rows** with near‑zero totals (e.g., `< 1e-5`).  
   - Result: kept ~20k valid rows after removing ~2.3k abnormal rows.

3. **EDA Highlights**
   - **Au/Ag/Pb histograms** across stages show:
     - **Gold (Au)** shifts to **higher concentrations** as purification progresses (expected).
     - **Silver (Ag)** moderately improves; more overlap between stages.
     - **Lead (Pb)** changes little, indicating limited impact from purification.
   - **Feed size** distributions compared between train and test to confirm similarity.
   - Boxplots after cleaning show more realistic concentration ranges.

4. **Modeling**
   - Models: **DecisionTreeRegressor**, **RandomForestRegressor**, **LinearRegression**.
   - Hyperparameter tuning with **GridSearchCV** (5‑fold), custom **sMAPE scorer**.
   - Baseline: **DummyRegressor(strategy='mean')**.

5. **Evaluation**
   - Cross‑validation on train; final evaluation on the **real test set** using the project’s weighted sMAPE.

---

## Results (from notebook)
- **Linear Regression** (validation): sMAPE ≈ **13.33**
- **Decision Tree** (validation): best CV score reported; **test sMAPE ≈ 18.54**
- **Dummy baseline** (test): sMAPE ≈ **13.18**

> Note: Although the Decision Tree achieved strong CV scores, it **under‑performed on the test set** (18.54). The baseline achieved ~13.18, indicating that further feature engineering or regularization is needed. (Random Forest CV also explored.)

---

## Conclusion
- The pipeline demonstrates an **end‑to‑end industry workflow** for recovery prediction with a target‑specific **weighted sMAPE**.
- **Generalization gap** observed (good CV, weaker test) suggests improvements such as:
  - Time‑aware validation / leakage checks
  - Feature engineering (process lags, ratios, rolling stats)
  - Model ensembling (Random Forest, Gradient Boosting) and robust regularization
  - Outlier‑resistant losses and quantile models

---

## Tech Stack
- Python: **pandas, numpy, scikit‑learn, matplotlib, seaborn**
- Models: Linear Regression, Decision Tree, Random Forest
- Validation: GridSearchCV (5‑fold) with custom **sMAPE** scorer

---

## 🚀 How to Run
```bash
# 1) Create environment and install deps
pip install -r requirements.txt

# 2) Launch the notebook
jupyter notebook
# open Sprint_10.ipynb (or your notebook file) and Run All
```

---

## 🗂 Suggested Repo Structure
```
.
├── data/                         # (optional) datasets or a README with download instructions
├── notebooks/                    # Jupyter notebooks (e.g., Sprint_10.ipynb)
├── src/                          # reusable functions (metrics, cleaning, etc.) - optional
├── images/                       # screenshots/plots for the README gallery - optional
├── requirements.txt
└── README.md
```

---

## 🖼 (Optional) Screenshot Gallery
Place exported figures into `images/` and embed like:
```html
<p>
  <a href="images/au_hist.png"><img src="images/au_hist.png" width="31%"></a>
  <a href="images/feed_size.png"><img src="images/feed_size.png" width="31%"></a>
  <a href="images/boxplot_cleaned.png"><img src="images/boxplot_cleaned.png" width="31%"></a>
</p>
```
