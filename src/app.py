import joblib
import streamlit as st
import re
import random

VECTOR_FILE = "vectorizer.joblib"
MODEL_FILE = "spam_model.joblib"

# Check if files exist
import os
if not os.path.exists(VECTOR_FILE):
    st.error(f"Vectorizer file not found: {VECTOR_FILE}")
    st.stop()
if not os.path.exists(MODEL_FILE):
    st.error(f"Model file not found: {MODEL_FILE}")
    st.stop()

# Load model and vectorizer
vectorizer = joblib.load(VECTOR_FILE)
model = joblib.load(MODEL_FILE)

# Preprocessing function
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

# Prediction function
def predict_message(message):
    clean_msg = preprocess_text(message)
    vectorized_msg = vectorizer.transform([clean_msg])
    prediction = model.predict(vectorized_msg)[0]
    return prediction

# Example messages
examples = [
    "Congratulations! You've won a prize!",
    "Hey, are we meeting today?",
    "URGENT! Your account has been compromised",
    "Can you call me back later?",
    "You have been selected for a $1000 gift card"
]

# Streamlit interface
st.set_page_config(page_title="Spam Classifier", page_icon="📧", layout="wide")
st.title("📧 Spam Classifier")
st.subheader("Detect whether a message is Spam or Not Spam")

# Input
if 'message' not in st.session_state:
    st.session_state['message'] = ""

message = st.text_area("Enter your message here:", value=st.session_state.get('message', ''), height=120)

# Random suggestion
if st.button("💡 Suggest Random Message"):
    st.session_state['message'] = random.choice(examples)
    message = st.session_state['message']

# Predict
if st.button("Predict"):
    if message.strip() == "":
        st.warning("⚠️ Please enter a message to predict.")
    else:
        result = predict_message(message)
        color = "#FF4B4B" if str(result).lower() == "spam" else "#28A745"
        st.markdown(
            f'<div style="padding:25px;border-radius:15px;font-size:28px;font-weight:bold;text-align:center;color:white;background-color:{color}">Prediction: {result}</div>',
            unsafe_allow_html=True
        )

# Footer
st.markdown("---")
st.markdown('<p style="text-align:center;">Made with ❤️ by Bharath Kumar Ramisetti</p>', unsafe_allow_html=True)
