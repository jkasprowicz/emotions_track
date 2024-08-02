import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline

# Load the CSV file
df = pd.read_csv('imdb_reviews_summary_and_ratings.csv')

# Clean the ratings to convert them to numerical values
df['rating'] = df['rating'].str.extract('(\d+)').astype(int)

print(df.head())

tokenizer = AutoTokenizer.from_pretrained("SchuylerH/bert-multilingual-go-emtions")
model = AutoModelForSequenceClassification.from_pretrained("SchuylerH/bert-multilingual-go-emtions")
nlp = pipeline("sentiment-analysis", model = model, tokenizer = tokenizer)


# Function to predict emotion for a given summary
def predict_emotion(summary):
    try:
        result = nlp(summary)
        # Assuming the model returns a list of dictionaries with 'label' and 'score'
        if result:
            label = result[0]['label']
            score = result[0]['score']
            print(f"Summary: {summary}\nPredicted Emotion: {label}, Score: {score}\n")
            return label
        else:
            print(f"Summary: {summary}\nPredicted Emotion: Unknown\n")
            return 'Unknown'
    except Exception as e:
        print(f"Error processing summary: {summary}\nException: {e}\n")
        return 'Error'

# Apply the function to the 'summary' column
df['emotion'] = df['summary'].apply(predict_emotion)

# Save the DataFrame with emotions
df.to_csv('imdb_reviews_with_emotions.csv', index=False)

print("Emotion inference completed and saved to 'imdb_reviews_with_emotions.csv'")

print(df.head())