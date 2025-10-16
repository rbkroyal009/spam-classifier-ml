# app.py
import streamlit as st
import pickle
import re
import os
import random

# -------------------------------
# File paths (inside src/)
# -------------------------------
VECTOR_FILE = "src/vectorizer.pkl"
MODEL_FILE = "src/spam_model.pkl"

# -------------------------------
# Check if files exist
# -------------------------------
if not os.path.exists(VECTOR_FILE):
    st.error(f"Vectorizer file not found: {VECTOR_FILE}")
    st.stop()
if not os.path.exists(MODEL_FILE):
    st.error(f"Model file not found: {MODEL_FILE}")
    st.stop()

# -------------------------------
# Load model and vectorizer
# -------------------------------
with open(VECTOR_FILE, "rb") as f:
    vectorizer = pickle.load(f)

with open(MODEL_FILE, "rb") as f:
    model = pickle.load(f)

# -------------------------------
# Preprocessing function
# -------------------------------
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

# -------------------------------
# Prediction function
# -------------------------------
def predict_message(message):
    clean_msg = preprocess_text(message)
    vectorized_msg = vectorizer.transform([clean_msg])
    prediction = model.predict(vectorized_msg)[0]
    return prediction

# -------------------------------
# Random message suggestions
# -------------------------------
examples = [
    "Congratulations! You've won a prize!",
    "Hey, are we meeting today?",
    "URGENT! Your account has been compromised",
    "Can you call me back later?",
    "You have been selected for a $1000 gift card"
]

# -------------------------------
# Streamlit setup
# -------------------------------
st.set_page_config(
    page_title="📧 Spam Classifier",
    page_icon="📧",
    layout="wide"
)

# Custom CSS for background and title
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #fdfbfb 0%, #c9d6ff 100%);
        font-family: 'Segoe UI', sans-serif;
    }
    .title {
        color: #4B0082;
        font-size: 42px;
        font-weight: bold;
        text-align: center;
    }
    .prediction-box {
        padding: 25px;
        border-radius: 15px;
        font-size: 28px;
        font-weight: bold;
        text-align: center;
        color: white;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------------
# Main header
# -------------------------------
st.markdown('<h1 class="title">📧 Spam Classifier</h1>', unsafe_allow_html=True)
st.subheader("Detect whether a message is Spam or Not Spam")

# -------------------------------
# Sidebar with instructions & examples
# -------------------------------
st.sidebar.header("Instructions")
st.sidebar.write("1. Enter your message in the text area.")
st.sidebar.write("2. Click **Predict** to see the result.")
st.sidebar.write("3. Use the random suggestion buttons for quick testing.")
st.sidebar.write("### Example Messages")
for msg in examples:
    if st.sidebar.button(msg[:40] + "...", key=msg):
        st.session_state['message'] = msg

# -------------------------------
# Text input area
# -------------------------------
if 'message' not in st.session_state:
    st.session_state['message'] = ""

message = st.text_area(
    "Enter your message here:", 
    value=st.session_state.get('message', ''), 
    height=120
)

# -------------------------------
# Random suggestion button
# -------------------------------
if st.button("💡 Suggest Random Message"):
    st.session_state['message'] = random.choice(examples)
    message = st.session_state['message']

# -------------------------------
# Predict button
# -------------------------------
if st.button("Predict"):
    if message.strip() == "":
        st.warning("⚠️ Please enter a message to predict.")
    else:
        result = predict_message(message)
        color = "#FF4B4B" if result.lower() == "spam" else "#28A745"
        st.markdown(
            f'<div class="prediction-box" style="background-color:{color}">Prediction: {result}</div>',
            unsafe_allow_html=True
        )

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.markdown('<p style="text-align:center;">Made by Bharath Kumar Ramisetti</p>', unsafe_allow_html=True)
