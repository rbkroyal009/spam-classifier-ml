# model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score
import pickle
import os

# Load dataset
df = pd.read_csv("../data/spam.csv", encoding='latin1')  # fixes utf-8 errors
df = df.rename(columns={df.columns[0]:'label', df.columns[1]:'text'})  # adjust column names
df = df[['text','label']]

# Split data
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42)

# Vectorizer
vectorizer = TfidfVectorizer(stop_words='english')
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train model
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Evaluate
y_pred = model.predict(X_test_vec)
print("✅ Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Save vectorizer and model inside src/
os.makedirs("src", exist_ok=True)
with open("src/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

with open("src/spam_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model and vectorizer saved successfully!")
