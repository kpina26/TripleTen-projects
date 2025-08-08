# IMDb TV Shows Analysis – Golden Age of Television

📌**Project Overview**
This project analyzes a dataset of movies and shows from IMDb to investigate whether highly-rated TV shows released during the "Golden Age" of television (starting in 1999 with The Sopranos) also received the most votes from viewers.

The focus is only on TV shows, excluding movies, to test the assumption that higher-rated shows tend to have more votes.


🎯 **Objectives**
Evaluate the quality of the dataset (missing values, duplicates, formatting issues).

Preprocess the data to ensure accuracy and consistency.

Analyze the relationship between IMDb ratings and the number of votes.


📂 **Dataset**
The dataset (movies_and_shows.csv) contains:

Actor/Director names

Character names

Role type (actor/director)

Title of the movie/show

Type (movie/show)

Release year

Genres

IMDb score

IMDb votes


🛠 **Methodology**
Stage 1 – Data Overview
Loaded the dataset using pandas.

Inspected general information with .info() and .head().

Identified:

Mixed case and whitespace in column names.

Numeric columns stored as objects.

Missing values in title, imdb_score, and imdb_votes.

Stage 2 – Data Preprocessing
Renamed columns to snake_case, removed spaces, and replaced incorrect characters.

Removed rows with missing values in imdb_score and imdb_votes.

Removed 6,994 duplicate rows.

Standardized the type column to merge implicit duplicates (SHOW, tv show, shows → show).

Stage 3 – Data Analysis
Filtered the dataset to only include TV shows released in 1999 or later.

Grouped IMDb scores into integer buckets (1–10).

Removed outlier scores with very few votes (e.g., scores 2, 3, 10).

Calculated average number of votes per score.

Sorted results in descending order of average votes.


📊 **Key Findings**
Top 3 scores with the highest average votes were:

Score 9 → ~126,904 votes

Score 8 → ~30,299 votes

Score 7 → ~8,727 votes

The analysis confirms the assumption: highly-rated shows (scores 7–9) have the most votes.


🖥 **Technologies Used**
Python (pandas, numpy)

Jupyter Notebook / VS Code

CSV dataset from TripleTen


📌 **Conclusion**
The research confirms that during the "Golden Age" of television, higher-rated TV shows also received the most audience engagement, as measured by IMDb votes.
This trend holds for scores between 4–9, with scores 7–9 dominating in popularity.


📎 **How to Run**
Clone this repository.

Place the movies_and_shows.csv file in the datasets/ directory.

Open the Jupyter Notebook and run all cells.