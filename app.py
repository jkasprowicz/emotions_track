from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline

app = Flask(__name__)

tokenizer = AutoTokenizer.from_pretrained("SchuylerH/bert-multilingual-go-emtions")
model = AutoModelForSequenceClassification.from_pretrained("SchuylerH/bert-multilingual-go-emtions")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['text']
    nlp = pipeline("sentiment-analysis", model = model, tokenizer = tokenizer)

    if not text:
        return render_template('index.html', emotion_scores={})

    try:
        result = nlp(text)
        print(result)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return render_template('index.html', result=result)



if __name__ == '__main__':
    app.run(debug=True)
