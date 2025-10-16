# predict.py
import pickle

# Load vectorizer and model
with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)
with open("spam_model.pkl", "rb") as f:
    model = pickle.load(f)

def predict_message(msg):
    vec = vectorizer.transform([msg])
    pred = model.predict(vec)[0]
    return "✅ Not Spam" if pred == 0 else "🚨 Spam"

# Test examples
msg1 = "Congratulations! You won $1000 cash!"
msg2 = "Are we meeting tomorrow?"
print(msg1, "→", predict_message(msg1))
print(msg2, "→", predict_message(msg2))
