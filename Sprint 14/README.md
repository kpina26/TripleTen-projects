
# Film Junky Union - IMDB Review Classification

## Project Overview
This project focuses on developing and evaluating machine learning models to classify IMDB movie reviews as positive or negative. 
Through comprehensive data preprocessing, exploratory data analysis, and model training, the system can effectively manage and 
moderate user-submitted movie reviews.

## Key Features
- Preprocessing of raw text data, including tokenization, stopword removal, and lemmatization.
- Comparison of multiple models: Logistic Regression, spaCy, LGBM, and BERT.
- Implementation of TF-IDF vectorization and transformer-based embeddings.
- Evaluation using F1 score to determine the most effective model.

## Models Implemented
1. **Logistic Regression (TF-IDF)**
2. **spaCy NLP model (TF-IDF)**
3. **LGBM Classifier (TF-IDF)**
4. **BERT Transformer-based model**

## Results
- Models 2–4 rely on TF-IDF and traditional classifiers, which can misclassify complex or nuanced reviews.
- **BERT** outperformed other models, achieving an **F1 score of 0.67** even with a smaller training dataset, demonstrating 
  its ability to understand contextual meaning.

## Conclusion
This solution can be integrated into an automated system to help the Film Junky Union efficiently manage and moderate 
user-submitted movie reviews, improving the accuracy and fairness of the review platform.

## How to Run

Install Juypter Notebook

Open Sprint 14.ipynb

Install necessary libaries

## License
This project is licensed under the MIT License.
