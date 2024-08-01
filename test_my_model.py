import tensorflow as tf
from transformers import BertTokenizer

# Load the tokenizer
tokenizer_path = '/Users/joaokasprowicz/Documents/Dev/emotions_track/tokenizer'
tokenizer = BertTokenizer.from_pretrained(tokenizer_path)

# Load the SavedModel as a TFSMLayer
model_path = '/Users/joaokasprowicz/Documents/Dev/emotions_track/full_model'
model = tf.keras.layers.TFSMLayer(model_path, call_endpoint='serving_default')

# Example input text
input_text = ["i love you"]

# Preprocess the input text
inputs = tokenizer(input_text, return_tensors='tf', padding=True, truncation=True)
input_ids = inputs['input_ids']
attention_mask = inputs['attention_mask']

# Perform inference
outputs = model(input_ids, attention_mask=attention_mask)

# Extract predictions
predictions = outputs['predictions'].numpy()
print(predictions)
