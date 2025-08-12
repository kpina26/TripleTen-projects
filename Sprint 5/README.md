# World of Video Games

## Project Overview
An online store, Ice, sells video games worldwide. The goal of this project is to analyze the key factors that influence game sales, including:
- User and expert reviews
- Game genres
- Platforms
- ESRB ratings

The analysis explores historical video game sales data to identify trends and patterns that determine a game's success. Using 2016 data as a reference point, the goal is to build a data-driven strategy for 2017 to help identify potential top-performing games and consoles.

---

## Dataset
- **Source**: `games.csv` (Practicum-provided dataset)
- **Columns**:
  - `Name`: Game title
  - `Platform`: Gaming platform (e.g., PS4, Xbox, Wii)
  - `Year_of_Release`: Release year
  - `Genre`: Game genre
  - `NA_sales`, `EU_sales`, `JP_sales`, `Other_sales`: Regional sales in millions of copies
  - `Critic_Score`, `User_Score`: Review ratings
  - `Rating`: ESRB rating

---

## Methods
- **Data Preprocessing**: Handling missing values, converting data types, and filtering by relevant years.
- **Exploratory Data Analysis (EDA)**: Sales trends by region, platform performance, top genres.
- **Statistical Testing**: Comparing average user scores and sales between platforms and genres.
- **Visualization**: Histograms, boxplots, bar charts for sales and ratings.

---

## Results & Insights
- Identified top-performing platforms and genres for 2016.
- Found correlations between critic scores, user scores, and game sales.
- Regional sales differences suggest tailored marketing strategies for different markets.

---

## How to Run

1. **Clone this repository**  
   ```bash
   git clone https://github.com/yourusername/world-of-video-games.git
   cd world-of-video-games
   ```

2. **Install required libraries**  
   Make sure you have Python 3.8+ installed. Then run:  
   ```bash
   pip install pandas numpy matplotlib seaborn scipy
   ```

3. **Obtain the dataset**  
   - The notebook will first try to load `datasets/games.csv` if available locally.  
   - If not found, it will automatically download from:  
     ```
     https://practicum-content.s3.us-west-1.amazonaws.com/datasets/games.csv
     ```

4. **Open the Jupyter Notebook**  
   ```bash
   jupyter notebook Sprint_5.ipynb
   ```

5. **Run the analysis**  
   Execute the cells in order to reproduce the full data exploration, statistical tests, and insights.

---

## Technologies Used
- Python (Pandas, NumPy, Matplotlib, Seaborn, SciPy)
- Jupyter Notebook
- VS Code

---

## Author
**Kelvin Pina**  
Data Science Portfolio Project | TripleTen Bootcamp