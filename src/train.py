import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib
from preprocess import clean_text

DATA_CSV = os.path.join(os.path.dirname(__file__), '..', 'data', 'smsspam.csv')
MODEL_DIR = os.path.join(os.path.dirname(__file__), '..', 'models')

def main():
    os.makedirs(MODEL_DIR, exist_ok=True)
    df = pd.read_csv(DATA_CSV)
    df['clean'] = df['message'].astype(str).apply(clean_text)
    X = df['clean']
    y = df['label']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    pipe = Pipeline([
        ('tfidf', TfidfVectorizer(max_features=5000)),
        ('clf', LogisticRegression(max_iter=1000))
    ])
    print('Training model...')
    pipe.fit(X_train, y_train)
    print('Evaluating...')
    preds = pipe.predict(X_test)
    acc = accuracy_score(y_test, preds)
    prec = precision_score(y_test, preds)
    rec = recall_score(y_test, preds)
    f1 = f1_score(y_test, preds)
    print(f'Accuracy: {acc:.4f}  Precision: {prec:.4f}  Recall: {rec:.4f}  F1: {f1:.4f}')
    model_path = os.path.join(MODEL_DIR, 'spam_classifier.joblib')
    joblib.dump(pipe, model_path)
    print('Saved model to', model_path)

if __name__ == '__main__':
    main()
