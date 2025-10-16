# model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
import pickle
import os

# Correct dataset path
data_path = os.path.join("..", "data", "spam.csv")

# Load dataset
df = pd.read_csv(data_path, encoding='latin-1')[['v1', 'v2']]
df.columns = ['label', 'message']
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# Load vectorizer
with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Transform text
X = vectorizer.transform(df['message'])
y = df['label']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Evaluate
pred = model.predict(X_test)
print("✅ Accuracy:", accuracy_score(y_test, pred))
print("\nClassification Report:\n", classification_report(y_test, pred))

# Save model
with open("spam_model.pkl", "wb") as f:
    pickle.dump(model, f)
print("✅ Model saved as 'spam_model.pkl'")
