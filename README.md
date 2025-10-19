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
![Home Screen](screenshots/home.png)  

**Spam Prediction Example**  
![Spam Prediction](screenshots/spam_prediction.png)  

**Ham Prediction Example**  
![Ham Prediction](screenshots/ham_prediction.png)  



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
