# 2017 Instacart Data Analysis

## Project Overview
This project analyzes Instacart grocery order data from 2017 to uncover customer shopping habits. Using Python and data visualization, we explore ordering patterns by time, day, product popularity, and reorder trends.
The analysis was conducted as part of a data science sprint and focuses on data cleaning, exploratory data analysis (EDA), and generating actionable insights.

## Dataset Description
### The analysis uses multiple CSV files provided by Instacart:

- instacart_orders.csv — Order-level data with timestamps, customer IDs, and time between orders.

- products.csv — Product information including aisle and department IDs.

- aisles.csv — Aisle names and IDs.

- departments.csv — Department names and IDs.

- order_products.csv — Links products to orders, including order sequence and whether items were reordered.

## Objectives
- Clean and prepare the dataset by handling duplicates and missing values.

- Explore shopping patterns by hour of day, day of week, and time between orders.

- Identify the most popular products and most frequently reordered products.

- Analyze order size distribution to understand typical shopping behavior.

## Data Cleaning
### Steps performed:

- Duplicate removal:

- Checked and removed full duplicate rows in all datasets.

- Verified no duplicate order_id or product_id entries.

- Missing value handling:

- Filled missing product_name values with "Unknown".

- Investigated missing add_to_cart_order values and replaced them with 999 for outlier identification.

- Data type checks:

- Confirmed integer and float formats for numeric columns.

- Verified value ranges for order_hour_of_day (0–23) and order_dow (0–6).

## Exploratory Data Analysis
1️⃣ Ordering Behavior
By Hour of Day:

Orders peak between late morning and early afternoon.

By Day of Week:

Highest order volume occurs on Sundays and Mondays.

Days Since Prior Order:

Common intervals: 7 days (weekly shopping) and 30 days.

2️⃣ Popular Products
Top products ordered:

Bananas

Bag of organic bananas

Organic strawberries

Organic baby spinach
... (full top 20 in notebook)

3️⃣ Order Size
Median items per order: 8

Most orders contain fewer than 10 items.

4️⃣ Reorder Patterns
Most frequently reordered items:

Banana

Bag of organic bananas

Organic strawberries

Organic baby spinach
... (full top 20 in notebook)

## Visualizations
- Bar plots for orders by hour/day.

- Histogram for days since prior order.

- Distribution plots for items per order.

- Comparative histograms for Wednesday vs Saturday ordering patterns.

## Key Insights
- Weekly grocery habits: Many users reorder around the same day each week.

- Bananas dominate both in popularity and reorder frequency.

- Order sizes are small, indicating frequent but lighter shopping trips.

- Peak hours are mid-morning to mid-afternoon, suggesting customers order during breaks or after morning errands.

## Technologies Used
- Python (pandas, matplotlib)

- Jupyter Notebook / VS Code

- Data visualization for trend discovery

- CSV data handling for multi-file dataset integration

## How to Run
Clone this repository:

bash
Copy
Edit
git clone https://github.com/yourusername/instacart-analysis.git
Install dependencies:

bash
Copy
Edit
pip install pandas matplotlib
Run the Jupyter Notebook:

bash
Copy
Edit
jupyter notebook Sprint_2.ipynb

## License
This project is for educational purposes and uses public datasets provided by Instacart for analysis.