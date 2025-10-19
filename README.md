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


---

## 🔹 Installation & Usage

### 1️⃣ Clone the repository
```bash
git clone https://github.com/rbkroyal009/spam-classifier-ml.git
cd spam-classifier-ml/src

##installations
pip install -r ../requirements.txt
pip install streamlit

##run 
streamlit run app.py
🔹 Technologies Used

Python 3.x

pandas, numpy

scikit-learn (for TF-IDF & Naive Bayes)

Streamlit (for web app)

=======
# Spam Classifier ML Project

Detects whether a text message is spam or not using Machine Learning and Streamlit.

## Features
- Preprocessing with TF-IDF
- Naive Bayes model
- Streamlit web app interface
- Fully portable and accessible from any device

## Folder Structure
spam-classifier-ml/
├── data/
│ └── spam.csv
├── src/
│ ├── preprocess.py
│ ├── model.py
│ ├── predict.py
│ └── app.py
├── requirements.txt
└── README.md


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
