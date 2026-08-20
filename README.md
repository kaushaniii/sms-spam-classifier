# 📩 SMS Spam Classifier

An end-to-end Machine Learning web application built using Streamlit that classifies SMS/messages as either Spam or Ham (Not Spam) in real-time.

🔗 Live Demo: [sms-spam-classifier.streamlit.app](https://sms-spam-classifier-jgui9fkcr6osuj7xms9aqc.streamlit.app/)

---

## 📌 Features

- Real-Time Classification: Instantly detects whether an entered text message is Spam or Ham.
- Natural Language Processing (NLP): Preprocesses text using tokenization, stopword removal, and stemming/vectorization.
- Interactive UI: Clean and responsive interface built with Streamlit.
- Lightweight & Fast: Optimized model pipeline for quick inference.

---

## 🛠️ Tech Stack & Libraries

- Language: Python
- Web Framework: [Streamlit](https://streamlit.io/)
- Machine Learning & NLP: 
  - scikit-learn
  - nltk
- Data Manipulation: pandas, numpy
- Model Serialization: pickle / joblib

---

## 📂 Project Structure

`text
├── app.py                 # Streamlit application script
├── model.pkl              # Trained ML model (e.g., Naive Bayes / Random Forest)
├── vectorizer.pkl         # Trained TF-IDF / Bag of Words vectorizer
├── requirements.txt       # Python dependencies
├── SMS_Spam_Classifier.ipynb    # Notebook containing EDA, preprocessing & model training
└── README.md              # Project documentation
