# 📰 Fake News Detection v2

This project detects whether a news headline or article is **Real** or **Fake** using **Machine Learning (Logistic Regression)** and **TF-IDF vectorization**. It was built and trained on a labeled dataset of real and fake news articles.

---

## 📁 Files

- `app.ipynb` – Google Colab notebook with full pipeline
- `True.csv` / `Fake.csv` – Datasets used for training
- `tfidf_vectorizer_v2.pkl` – Saved vectorizer
- `fake_news_model_v2.pkl` – Trained Logistic Regression model
- `requirements.txt` – Python dependencies

---

## 🧠 Model Workflow

1. **Data Loading** – Combines and labels fake & real datasets
2. **Text Preprocessing** – Lowercase, remove digits/punctuation, lemmatization
3. **Vectorization** – TF-IDF on cleaned text
4. **Model Training** – Logistic Regression with accuracy evaluation
5. **Export** – Saves model & vectorizer for inference

---

## 🔍 Dataset Info

- **True.csv**: Verified real news articles
- **Fake.csv**: Articles flagged as misinformation
- Source: [Kaggle Fake and Real News Dataset](https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset)

---

## 📊 Model Performance

- **Accuracy:** ~95%
- **Evaluation:** Confusion matrix, classification report

---

## 🚀 How to Run

You can run the full training pipeline on **Google Colab**:
1. Upload `True.csv` and `Fake.csv`
2. Follow each step in `app.ipynb`
3. Download the `.pkl` files for deployment

---

## 📦 Dependencies

Install all dependencies using:

```bash
pip install -r requirements.txt
