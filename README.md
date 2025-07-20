---

## 📰 Fake News Detection Web App

This project is a simple yet elegant Flask web application that uses a machine learning model to detect whether a given news headline is **Fake** or **Real**. The UI is designed with a 3D gradient style to ensure a responsive and visually appealing experience.

---

### 🚀 Features

- 🔍 Predicts whether a news headline is real or fake
- 🧠 Trained using machine learning (TF-IDF + Logistic Regression/Neural Network)
- 🎨 Beautiful, modern 3D UI with responsive design
- 🧪 Easy to run locally

---

### 🖼️ Screenshots

#### 📝 Input Interface
![Input UI](images/1.png)

#### ✅ Prediction Output
![Output UI](images/2.png)

---


### 🛠️ Installation and Setup

```bash
# Clone the repository
git clone https://github.com/rbpata/fake_real_news_predict_DP.git
cd fake-news-detector

# Create virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt

# Run the app
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

---

### 📁 Project Structure

```
.
├── app.py
├── model/model.h5
├── templates/
│   ├── index.html
│   └── result.html
├── static/
│   └── style.css
├── images/
│   ├── 1.png
│   └── 2.png
├── requirements.txt
└── README.md
```

---

### 📌 Future Enhancements

- 📱 Add mobile-first enhancements
- 🌐 Deploy on Heroku or Render
- 🔄 Add real-time API integration for latest news
- 📊 Show model confidence scores

---

### 🙌 Contribution

Feel free to fork this repository and submit pull requests. All kinds of contributions are welcome!

---

