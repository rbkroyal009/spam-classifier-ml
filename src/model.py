# model.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import joblib

# Load dataset
df = pd.read_csv("../data/spam.csv", encoding="latin-1")
df = df[['v2', 'v1']]
df.columns = ['text', 'label']

# Split
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42)

# Vectorizer
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)

# Model
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Save vectorizer and model using joblib
joblib.dump(vectorizer, "vectorizer.joblib")
joblib.dump(model, "spam_model.joblib")

print("✅ Model and vectorizer saved successfully with joblib!")
