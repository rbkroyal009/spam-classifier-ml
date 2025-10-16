# preprocess.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import os

# Correct dataset path (relative to src folder)
data_path = os.path.join("..", "data", "spam.csv")

# Load dataset
df = pd.read_csv(data_path, encoding='latin-1')[['v1', 'v2']]
df.columns = ['label', 'message']

# Encode labels: ham=0, spam=1
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# TF-IDF vectorization
vectorizer = TfidfVectorizer(stop_words='english', max_features=3000)
X = vectorizer.fit_transform(df['message'])

# Save vectorizer
with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("✅ Preprocessing complete. Vectorizer saved as 'vectorizer.pkl'.")
print("Sample data:")
print(df.head())
