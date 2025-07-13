# 📰 Fake News Detection App (v2)

This is a machine learning-based web app that detects whether a news article or headline is **REAL** or **FAKE** using Natural Language Processing and a Logistic Regression model.

---

## 📂 Dataset

We used the **Fake and Real News Dataset** from Kaggle which contains:

- ✅ `True.csv` – Real news
- ❌ `Fake.csv` – Fake news

Both datasets were labeled and merged, cleaned using NLP, and vectorized using `TfidfVectorizer`.

---

## ⚙️ Model

- ✅ Preprocessing: stopword removal, lemmatization, punctuation cleanup
- 🔠 Vectorizer: TF-IDF (`max_features=5000`)
- 🤖 Classifier: Logistic Regression
- 💾 Model saved using `joblib`

---

## 🧪 Accuracy

Achieved an accuracy of around **90%+** on the test set.

---

## 💻 Web App (Built with Streamlit)

Enter any news article or headline in the input box, and the app will predict whether it's **REAL** or **FAKE**.

---

## 🖼 Screenshots

### ✅ Real News Prediction

![Real News](Screenshot_62.png)

### ❌ Fake News Prediction
Screenshot (62).PNG
---

## 🚀 How to Run

```bash
# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
