import streamlit as st
import pickle
import os

# Load vectorizer and model
with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)
with open("spam_model.pkl", "rb") as f:
    model = pickle.load(f)

def predict_message(msg):
    vec = vectorizer.transform([msg])
    pred = model.predict(vec)[0]
    return "✅ Not Spam" if pred == 0 else "🚨 Spam"

# Streamlit interface
st.title("📩 Spam Message Classifier")
st.write("Enter a message below to check if it is spam or not.")

user_input = st.text_area("Your Message:")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter a message!")
    else:
        result = predict_message(user_input)
        st.success(result)
