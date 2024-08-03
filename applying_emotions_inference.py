import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline

df = pd.read_csv('imdb_reviews_summary_and_ratings.csv')

df['rating'] = df['rating'].str.extract('(\d+)').astype(int)

print(df.head())

tokenizer = AutoTokenizer.from_pretrained("SchuylerH/bert-multilingual-go-emtions")
model = AutoModelForSequenceClassification.from_pretrained("SchuylerH/bert-multilingual-go-emtions")
nlp = pipeline("sentiment-analysis", model = model, tokenizer = tokenizer)


def predict_emotion(summary):
    try:
        result = nlp(summary)
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

df['emotion'] = df['summary'].apply(predict_emotion)

df.to_csv('imdb_reviews_with_emotions.csv', index=False)

print("Emotion inference completed and saved to 'imdb_reviews_with_emotions.csv'")

print(df.head())