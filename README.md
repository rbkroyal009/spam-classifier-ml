📧 Spam Classifier ML Project

A Machine Learning project that detects whether a text message is Spam or Not Spam using a Naive Bayes classifier. Built with Python, scikit-learn, and Streamlit for an interactive web interface.

🚀 Live Demo

You can try the app live locally on your network: 
   http://192.168.1.7:8501
   
🔹 Features

 -->Text preprocessing with TF-IDF vectorization
 
 -->Naive Bayes classifier trained for spam detection
 
 -->Save and reuse trained model and vectorizer (.joblib)
 
 -->Interactive Streamlit web app for real-time prediction
 
 -->Random message suggestions for testing
 
 -->Keeps last 5 messages for quick access
 
 -->Fully portable and accessible on any device

 🧰 Tech Stack
 
-->Python – Core language

-->scikit-learn – ML model & vectorizer

-->pandas / numpy – Data handling

-->Streamlit – Web app interface

-->joblib – Model & vectorizer persistence

📂 Project Structure

Folders:

  data/ – Contains the dataset (spam.csv)
  
  src/ – Source code for the project

  preprocess.py – Text preprocessing functions

  model.py – Model training script

  predict.py – Script for testing predictions
  
  app.py – Streamlit web app
  
Files:

  spam_model.joblib – Trained Naive Bayes model
  
  vectorizer.joblib – Saved TF-IDF vectorizer

  requirements.txt – Required Python packages

  README.md – Project documentation

⚡ Run the App
streamlit run app.py

 ## 📸 Screenshots

**Home Screen**  
<img width="1920" height="1080" alt="home" src="https://github.com/user-attachments/assets/17e39835-295b-4a41-9d72-2d0f70f85a7d" />


**Spam Prediction Example**  

<img width="1920" height="1080" alt="spam_prediction png" src="https://github.com/user-attachments/assets/b35c62ac-9221-459c-be5b-2c61d0232448" />

**Ham Prediction Example**  

<img width="1920" height="1080" alt="ham_prediction" src="https://github.com/user-attachments/assets/84e30eb6-54d0-4552-b824-f71cec54e98e" />

📈 How It Works

Text Preprocessing:

Lowercase conversion

Remove special characters

Remove extra spaces

TF-IDF Vectorization:

Converts text messages into numerical features.

Prediction:

Naive Bayes classifier predicts spam or ham

Display result in color-coded box (Red = Spam, Green = Not Spam)

💡 Made By
Bharath Kumar Ramisetti

