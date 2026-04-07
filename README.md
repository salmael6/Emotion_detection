# 🧠 Emotion Detection using NLP

## 📌 Project Overview

This project implements an intelligent **Natural Language Processing (NLP)** solution for **emotion detection in text**. The system classifies user input into one of four emotions:
👉 **Joy, Sadness, Anger, Fear**

It combines text preprocessing, feature engineering using **TF-IDF**, and a **machine learning model (Logistic Regression)**, deployed through an interactive **Streamlit web application**.

---

## 🎥 Demo

https://github.com/salmael6/Emotion_detection/demo_detection_emotion.mp4

---

## 🎯 Objectives

* Build a complete NLP pipeline for emotion classification
* Clean and preprocess textual data effectively
* Transform text into numerical features using TF-IDF
* Train and evaluate a robust classification model
* Deploy an interactive application for real-time predictions

---

## 📂 Project Structure

```
├── data/
│   └── combined_emotion.csv
├── notebooks/
│   └── emotion_detector.ipynb
├── model/
│   └── emotion_detector.pkl
├── app/
│   └── app.py
└── README.md
```

---

## ⚙️ Technologies Used

* **Python 3**
* **Pandas / NumPy** – Data manipulation
* **Scikit-learn** – Machine learning
* **Matplotlib / WordCloud** – Visualization
* **Streamlit** – Web application
* **Joblib** – Model saving

---

## 📊 Dataset

* Source: Kaggle – *Sentiment and Emotion Analysis Dataset*
* Size: ~422,000 text samples
* Emotions used in this project:

  * Joy 😊
  * Sadness 😢
  * Anger 😡
  * Fear 😨

⚠️ Note: Classes *Love* and *Surprise* were removed to improve balance.

---

## 🔄 NLP Pipeline

### 1. Data Preprocessing

* Lowercasing text
* Removing punctuation, links, emails, numbers
* Tokenization
* Stopword removal
* Lemmatization
* Removing rare words (hapax)

### 2. Feature Extraction

* **TF-IDF Vectorization**

  * Max features: 5000
  * Unigrams + Bigrams

### 3. Model

* **Logistic Regression (Multiclass)**
* Parameter: `max_iter=1000`

---

## 📈 Model Performance

* **Accuracy:** ~95.5%
* Strong precision and recall across all classes
* Minor confusion in ambiguous emotional expressions

---

## 🚀 Application (Streamlit)

The application allows users to:

* Enter a text sentence
* Click on **"Detect Emotion"**
* View the predicted emotion instantly

### Example:

```
Input: "I feel really happy today!"
Output: Joy 😊
```

---

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/salmael6/Emotion_detection.git
cd Emotion_detection
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit app

```bash
streamlit run app/app.py
```

---

## 💡 Future Improvements

* Use **Deep Learning models** (LSTM, Transformers, BERT)
* Handle multi-label emotions
* Improve performance on ambiguous sentences
* Deploy online (Streamlit Cloud / Hugging Face Spaces)

---

## 📚 References

* Jurafsky & Martin – *Speech and Language Processing*
* Salton & Buckley – TF-IDF
* Scikit-learn Documentation

---

## 👩‍💻 Author

**Salma EL FORKANI**


