<<<<<<< HEAD
# Spam Classifier ML Project

A **Machine Learning Spam Classifier** that detects whether a text message is spam or not.  
Built with **Python**, **scikit-learn**, and **Streamlit** for an interactive web interface.

---

## 🔹 Features

- Preprocess text messages using **TF-IDF vectorization**
- Train and test **Naive Bayes classifier**
- Save trained model and vectorizer for reuse
- Interactive **Streamlit web app** for real-time prediction
- Fully portable and accessible from any device

---

## 🔹 Folder Structure
spam-classifier-ml/
├── data/
│ └── spam.csv # Dataset
├── src/
│ ├── preprocess.py # Text preprocessing
│ ├── model.py # Model training
│ ├── predict.py # Test predictions
│ └── app.py # Streamlit app
├── requirements.txt # Required Python packages
└── README.md # Project documentation


## How to Run
1. Clone the repo:
```bash
git clone https://github.com/<your-username>/spam-classifier-ml.git
cd spam-classifier-ml/src

##Install packages:
pip install -r ../requirements.txt
pip install streamlit

##Run the Streamlit app:
streamlit run app.py


click to run:http://192.168.1.7:8501

>>>>>>> 96e3923 (Add model, vectorizer, app.py and update README)

