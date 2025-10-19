# model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

# -------------------------------
# Load dataset (example: SMS Spam Collection)
# -------------------------------
DATA_FILE = "../data/spam.csv"  # update with your dataset path
if not os.path.exists(DATA_FILE):
    raise FileNotFoundError(f"Dataset not found: {DATA_FILE}")

df = pd.read_csv(DATA_FILE, encoding='latin-1')
df = df.rename(columns={'v1': 'label', 'v2': 'text'})  # rename according to dataset
df = df[['text', 'label']]

# -------------------------------
# Train/Test Split
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    df['text'], df['label'], test_size=0.2, random_state=42
)

# -------------------------------
# Vectorizer
# -------------------------------
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# -------------------------------
# Train Model
# -------------------------------
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# -------------------------------
# Evaluate Model
# -------------------------------
y_pred = model.predict(X_test_vec)
print(f"✅ Accuracy: {accuracy_score(y_test, y_pred):.4f}\n")
print("Classification Report:\n", classification_report(y_test, y_pred))

# -------------------------------
# Save Model and Vectorizer
# -------------------------------
joblib.dump(model, "../spam_model.joblib")
joblib.dump(vectorizer, "../vectorizer.joblib")
print("✅ Model and vectorizer saved successfully!")
