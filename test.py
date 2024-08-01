from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline

# Load the model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("SchuylerH/bert-multilingual-go-emtions")
model = AutoModelForSequenceClassification.from_pretrained("SchuylerH/bert-multilingual-go-emtions")

text = "why do you have to do that?."
nlp = pipeline("sentiment-analysis", model = model, tokenizer = tokenizer)

result = nlp(text)

print(result)
