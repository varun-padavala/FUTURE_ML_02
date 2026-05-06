# FUTURE_ML_02
Support Ticket Classification & Prioritization System

## 📌 Project Overview
This project is an NLP-based machine learning system that automatically classifies customer support tickets and assigns priority levels.

The system helps support teams:
- categorize tickets faster
- identify urgent issues
- reduce manual workload
- improve response efficiency

---

## 🚀 Features
- Text preprocessing
- TF-IDF vectorization
- Ticket category classification
- Priority prediction
- Streamlit web interface
- Hybrid ML + rule-based prediction system

---

## 🛠️ Tech Stack
- Python
- Scikit-learn
- Pandas
- Streamlit
- NLP preprocessing

---

## 📂 Dataset
Customer Support Ticket Dataset from Kaggle.

Dataset includes:
- Ticket Description
- Ticket Type
- Ticket Priority

---

## 🧠 Machine Learning Workflow
1. Data Cleaning
2. Text Preprocessing
3. TF-IDF Feature Extraction
4. Model Training
5. Prediction
6. Priority Classification

---

## ▶️ How to Run

### Install dependencies
```bash
pip install -r requirements.txt
```

### Train model
```bash
python src/train.py
```

### Run application
```bash
python -m streamlit run app/app.py
```

---

## 📸 Screenshots
(Add screenshots here)

---

## ✅ Example Predictions

Input:
```text
I was charged twice for my subscription
```

Output:
```text
Category: Billing issue
Priority: High
```

---

## 📌 Future Improvements
- Better NLP models
- Deep learning integration
- Better dataset balancing
- Real-time ticket dashboard

---

## 👨‍💻 Author
Varun Padavala