import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('imdb_reviews_with_emotions.csv')
df['emotion'] = df['emotion'].astype('category')
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')


plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='emotion', y='rating', palette='Set2')
plt.title('Rating Distribution by Emotion')
plt.xlabel('Emotion')
plt.ylabel('Rating')
plt.xticks(rotation=45)
plt.show()


plt.figure(figsize=(12, 6))
sns.violinplot(data=df, x='emotion', y='rating', palette='Set2')
plt.title('Rating Distribution by Emotion')
plt.xlabel('Emotion')
plt.ylabel('Rating')
plt.xticks(rotation=45)
plt.show()

average_ratings = df.groupby('emotion')['rating'].mean().reset_index()
heatmap_data = average_ratings.pivot_table(index='emotion', values='rating', aggfunc=np.mean)

plt.figure(figsize=(10, 8))
sns.heatmap(heatmap_data, annot=True, cmap='YlGnBu', cbar=True)
plt.title('Average Rating by Emotion')
plt.xlabel('Emotion')
plt.ylabel('Average Rating')
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='emotion', hue='rating', palette='viridis')
plt.title('Frequency of Emotions by Rating')
plt.xlabel('Emotion')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

sns.pairplot(df[['rating', 'emotion']], hue='emotion', palette='Set2')
plt.title('Pair Plot of Ratings and Emotions')
plt.show()
