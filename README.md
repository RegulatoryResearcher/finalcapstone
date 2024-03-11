Sentiment Analysis of Amazon Customer Reviews
Overview
This repository contains a Python script for performing sentiment analysis on Amazon customer reviews using the Pandas and SpaCy libraries. The script loads a CSV file containing customer reviews, preprocesses the text data, predicts the sentiment of each sentence using SpaCy's pre-trained English model, and saves the results to a new CSV file.

Requirements
Python 3.x
Pandas
SpaCy
Installation
Install Python: Download Python
Install Pandas:
Copy code
pip install pandas
Install SpaCy:
Copy code
pip install spacy
Download and install the English model for SpaCy:
Copy code
python -m spacy download en_core_web_sm
Usage
Clone this repository or download the Python script (amazon_reviews_sentiment.py) to your local machine.
Open a terminal or command prompt and navigate to the directory containing the Python script.
Run the script using the following command:
Copy code
python amazon_reviews_sentiment.py
The script will read the specified CSV file containing Amazon customer reviews, perform sentiment analysis on the text data, and save the results to a new CSV file.
Sample Data
The sample data used in this script is a subset of Amazon customer reviews stored in a CSV file (amazon_customer_reviews.csv). The file contains columns for review text, ratings, and other metadata.

Output
After running the script, a new CSV file (amazon_customer_reviews_with_sentiment.csv) will be generated, containing the original review data along with an additional column for sentiment labels (Positive, Negative, or Neutral) assigned to each sentence in the reviews.

Author
This script was written by Niamh

License
This project is licensed under the MIT License.
