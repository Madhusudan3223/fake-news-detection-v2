
import streamlit as st
import joblib
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download NLTK data (if not already present)
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("omw-1.4")

# Load trained model and vectorizer
model = joblib.load("fake_news_model_v2.pkl")
vectorizer = joblib.load("tfidf_vectorizer_v2.pkl")

# Text cleaning function
def clean_text(text):
    text = re.sub(r"<.*?>", "", text)  # remove HTML tags
    text = re.sub(r"http\S+|www\S+", "", text)  # remove URLs
    text = re.sub(r"[^a-zA-Z]", " ", text)  # keep only letters
    text = text.lower()
    words = text.split()
    stop_words = set(stopwords.words("english"))
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
    return " ".join(words)

# Prediction function
def predict_news(news_text):
    cleaned = clean_text(news_text)
    vect_input = vectorizer.transform([cleaned])
    prediction = model.predict(vect_input)
    return "REAL" if prediction[0] == 1 else "FAKE"

# Streamlit UI
st.set_page_config(page_title="📰 Fake News Detection App")
st.title("📰 Fake News Detection App")
st.markdown("Enter a news article or headline to detect if it's Fake or Real.")

news_input = st.text_area("🧾 Your News Text:", height=200)
if st.button("Check"):
    if news_input.strip() == "":
        st.warning("Please enter some news text.")
    else:
        result = predict_news(news_input)
        if result == "REAL":
            st.success("✅ This news is REAL.")
        else:
            st.error("❌ This news is FAKE.")
