# 📊 Revenue Analysis of Megaline Prepaid Plans

## Overview
This project analyzes user activity data from **Megaline's prepaid mobile plans** to determine which plan — **Surf** or **Ultimate** — is more profitable. 
The analysis includes data cleaning, feature engineering, exploratory data analysis, and statistical hypothesis testing.  
The goal is to support **strategic decision-making** regarding pricing, plan offerings, and customer retention.

---

## Business Problem
Megaline, a telecom provider, wants to optimize profitability by understanding which prepaid plan generates higher revenue and how usage behavior differs across plans.  
Key questions include:
- Which plan brings in more monthly revenue?
- Are usage patterns significantly different between the two plans?
- Are there regional differences in revenue?

---

## Dataset Description
The analysis uses five datasets:
1. **Calls** – Call durations and dates per user.
2. **Messages** – Number of text messages sent per user per date.
3. **Internet** – Volume of internet data used per user per date.
4. **Plans** – Plan names, monthly charges, and allowances for calls, messages, and internet.
5. **Users** – User demographics, signup dates, and assigned plans.

**Data Characteristics:**
- Covers a **1-year** period.
- Contains missing values and requires preprocessing.
- Multiple datasets require merging for analysis.

---

## Methodology

### 1. Data Cleaning & Preprocessing
- Converted date columns to `datetime` format.
- Removed missing values in key fields.
- Rounded call durations to the nearest minute.
- Aggregated data **per user per month** for calls, messages, and internet usage.
- Merged datasets into one master analytical table.

### 2. Feature Engineering
- Created **monthly usage metrics** (total calls, messages, internet MBs).
- Calculated **monthly revenue** per user, including extra charges for exceeding plan limits.

### 3. Exploratory Data Analysis
- **Usage Behavior:**  
  - Internet usage is generally higher for **Ultimate** plan users.
  - Surf plan users show less variability in internet consumption.
- **Revenue Analysis:**  
  - Mean monthly revenue:  
    - Surf: ~$60.71  
    - Ultimate: ~$72.31  
  - Revenue distributions show Ultimate plan users have more spread-out values.
- **Visualizations:**  
  - Histograms for monthly revenue.  
  - Boxplots comparing Surf vs. Ultimate usage and revenue.

### 4. Hypothesis Testing
Two main statistical tests were performed (α = 0.05):
1. **Plan Revenue Difference:**  
   - **H₀:** Average revenue is the same for Surf and Ultimate users.  
   - **H₁:** Average revenue differs between plans.  
   - Result: **Reject H₀** — revenue difference is statistically significant.
2. **Regional Revenue Difference (NY-NJ vs. Other Regions):**  
   - **H₀:** Average revenue is the same for NY-NJ and other regions.  
   - **H₁:** Average revenue differs between regions.  
   - Result: **Reject H₀** — regional revenue differences are statistically significant.

---

## Results & Insights
- **Ultimate plan users generate higher average monthly revenue** than Surf users.
- Internet usage is significantly higher among Ultimate users, with more variation in usage patterns.
- Revenue differences also exist between **NY-NJ** customers and customers in other regions.
- Findings suggest that **Ultimate** has stronger profitability potential, but pricing and data allowance optimization could increase Surf plan competitiveness.

---

## Conclusion & Recommendations
- Focus marketing efforts on promoting **Ultimate** plans to high-data users.
- Consider adjusting **Surf** plan allowances or pricing to increase average revenue per user.
- Regional pricing strategies could improve profitability in lower-performing areas.
- Further analysis with more recent data could confirm long-term trends.

---

## Technologies Used
- **Python**: pandas, numpy, matplotlib, scipy
- **Jupyter Notebook**
- **VS Code**

---

## How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/megaline-revenue-analysis.git
   cd megaline-revenue-analysis
   ```
2. Install required libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Open the Jupyter Notebook:
   ```bash
   jupyter notebook Sprint_3.ipynb
   ```

---

## Author
**Kelvin Pina**  
Data Science Portfolio Project | TripleTen Bootcamp  
