# app.py
import streamlit as st
import joblib
import re
import os
import random

# -------------------------------
# File paths (joblib files are in root folder)
# -------------------------------
VECTOR_FILE = "vectorizer.joblib"
MODEL_FILE = "spam_model.joblib"

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
vectorizer = joblib.load(VECTOR_FILE)
model = joblib.load(MODEL_FILE)

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
# Streamlit app setup
# -------------------------------
st.set_page_config(
    page_title="📧 Spam Classifier",
    page_icon="📧",
    layout="wide"
)

# Custom CSS
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
    .example-button {
        margin: 5px;
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
# Previous 5 searches
# -------------------------------
if 'history' not in st.session_state:
    st.session_state['history'] = []

if message.strip() != "" and message not in st.session_state['history']:
    st.session_state['history'].insert(0, message)
    st.session_state['history'] = st.session_state['history'][:5]  # keep last 5

if st.session_state['history']:
    st.subheader("🕘 Last 5 messages")
    for i, msg_hist in enumerate(st.session_state['history']):
        st.write(f"{i+1}. {msg_hist}")

# -------------------------------
# Predict button
# -------------------------------
if st.button("Predict"):
    if message.strip() == "":
        st.warning("⚠️ Please enter a message to predict.")
    else:
        result = predict_message(message)
        # Convert to string if it's numeric
        result_str = str(result)
        color = "#FF4B4B" if result_str.lower() == "spam" else "#28A745"
        st.markdown(
            f'<div class="prediction-box" style="background-color:{color}">Prediction: {result_str}</div>',
            unsafe_allow_html=True
        )

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.markdown('<p style="text-align:center;">Made with ❤️ by Bharath Kumar Ramisetti</p>', unsafe_allow_html=True)
