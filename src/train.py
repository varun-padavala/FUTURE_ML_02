import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC

from preprocess import clean_text
from vectorizer import get_vectorizer

def train():

    # Load dataset
    df = pd.read_csv("data/raw/tickets.csv")

    # Remove empty rows
    df = df.dropna(subset=[
        'Ticket Description',
        'Ticket Subject',
        'Ticket Type',
        'Ticket Priority'
    ])

    # Convert Critical -> High
    df['Ticket Priority'] = df['Ticket Priority'].replace('Critical', 'High')

    # Combine subject + description
    df['combined_text'] = (
        df['Ticket Subject'].fillna('') + ' ' +
        df['Ticket Description'].fillna('')
    )

    # Clean text
    df['clean_text'] = df['combined_text'].apply(clean_text)

    # Convert text -> vectors
    vectorizer = get_vectorizer()
    X = vectorizer.fit_transform(df['clean_text'])

    # Labels
    y_cat = df['Ticket Type']
    y_pri = df['Ticket Priority']

    # Split for category model
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y_cat,
        test_size=0.2,
        random_state=42
    )

    # Train category model
    model_cat = LinearSVC()
    model_cat.fit(X_train, y_train)

    # Split for priority model
    X_train2, X_test2, y_train2, y_test2 = train_test_split(
        X,
        y_pri,
        test_size=0.2,
        random_state=42
    )

    # Train priority model
    model_pri = LinearSVC()
    model_pri.fit(X_train2, y_train2)

    # Save models
    pickle.dump(model_cat, open("models/category_model.pkl", "wb"))
    pickle.dump(model_pri, open("models/priority_model.pkl", "wb"))
    pickle.dump(vectorizer, open("models/tfidf_vectorizer.pkl", "wb"))

    print("✅ Models trained successfully!")

if __name__ == "__main__":
    train()