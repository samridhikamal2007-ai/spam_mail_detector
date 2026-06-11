import os
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
import joblib

APP = Flask(__name__)
CORS(APP)

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'models', 'spam_classifier.joblib')

def load_model():
    if not os.path.exists(MODEL_PATH):
        return None
    return joblib.load(MODEL_PATH)

MODEL = load_model()

@APP.route('/')
def index():
    return render_template('index.html')

@APP.route('/predict', methods=['POST'])
def predict():
    global MODEL
    if MODEL is None:
        MODEL = load_model()
        if MODEL is None:
            return jsonify({'error':'Model not found. Run training first.'}), 400
    data = request.json or {}
    text = data.get('text') or request.form.get('text')
    if not text:
        return jsonify({'error':'No text provided'}), 400
    pred = MODEL.predict([text])[0]
    prob = None
    try:
        prob = float(MODEL.predict_proba([text])[0].max())
    except Exception:
        prob = None
    label = 'spam' if int(pred)==1 else 'ham'
    return jsonify({'label': label, 'probability': prob})

if __name__ == '__main__':
    APP.run(debug=True)
