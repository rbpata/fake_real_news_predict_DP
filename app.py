from flask import Flask, render_template, request
import numpy as np
import tensorflow as tf
from utils.preprocess import text_to_sequence

app = Flask(__name__)
model = tf.keras.models.load_model('model/model.h5')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        news_title = request.form['news']
        processed_input = text_to_sequence(news_title)
        prediction = model.predict(processed_input)[0][0]
        label = 'REAL' if prediction > 0.5 else 'FAKE'
        return render_template('result.html', prediction=label)


if __name__ == '__main__':
    app.run(debug=True)
