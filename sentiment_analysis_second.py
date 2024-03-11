import pandas as pd
import spacy

# Load the English model
nlp = spacy.load('en_core_web_sm')

# Load the CSV file
df = pd.read_csv(r"C:\Users\niamh\Documents\Data Science\Task 21\amazon_customer_reviews.csv", 
                 nrows=1000,  # Read only the first 1000 rows
                 dtype={'reviews.text': 'string', 18: 'object', 1: 'object', 10: 'object'})

# Drop rows with missing values in the 'reviews.text' column
df.dropna(subset=['reviews.text'], inplace=True)

# Remove duplicates
df.drop_duplicates(subset=['reviews.text'], keep='first', inplace=True)

# Text preprocessing function
def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()
    # Tokenize text (separate into individual sentences)
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]
    return sentences
    
# Function to predict sentiment for each sentence
def predict_sentiment(sentence):
    # Analyze sentiment using SpaCy
    doc = nlp(sentence)
    sentiment_score = sum([token.sentiment for token in doc]) / len(doc)
    
    # Determine sentiment label for the sentence
    if sentiment_score > 0:
        sentiment_label = "Positive"
    elif sentiment_score < 0:
        sentiment_label = "Negative"
    else:
        sentiment_label = "Neutral"
    
    return sentiment_label

# Apply sentiment analysis to each sentence in each review text
df['Sentiment'] = df['reviews.text'].apply(preprocess_text).explode().apply(predict_sentiment)

# Save the DataFrame to a CSV file
df.to_csv(r"C:\Users\niamh\Documents\Data Science\Task 21\amazon_customer_reviews_with_sentiment.csv", index=False)

# Print a message indicating successful CSV creation
print("CSV file successfully created.")
