import streamlit as st
import pickle
import string
import nltk
from nltk.stem.porter import PorterStemmer

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
from nltk.corpus import stopwords

ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    # Remove non-alphanumeric
    text = [i for i in text if i.isalnum()]

    # Remove stopwords and punctuation
    text = [i for i in text if i not in stopwords.words('english') and i not in string.punctuation]

    # Stemming
    text = [ps.stem(i) for i in text]

    return " ".join(text)

# Load models
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

# UI
st.set_page_config(page_title="SMS Spam Classifier", page_icon="📱")
st.title("📱 SMS Spam Classifier")
st.write("Enter an SMS message below to check if it's spam or not.")

input_sms = st.text_area("Enter your message here", height=150)

if st.button("🔍 Predict"):
    if input_sms.strip() == "":
        st.warning("Please enter a message first.")
    else:
        # Preprocess
        transformed_sms = transform_text(input_sms)

        # Vectorize
        vector_input = tfidf.transform([transformed_sms])

        # Predict
        result = model.predict(vector_input)[0]

        # Display result
        if result == 1:
            st.error("🚨 This message is SPAM!")
        else:
            st.success("✅ This message is NOT Spam.")
