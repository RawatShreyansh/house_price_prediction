# Boston House Price Prediction

Welcome to the **Boston House Price Prediction** project! This web application predicts the median value of owner-occupied homes in Boston using various housing features. Built with Flask, scikit-learn, and a pre-trained regression model, it provides an interactive interface for users to input data and receive instant predictions.

---

## 🚀 Features

- **User-Friendly Web Interface:** Enter housing features and get instant price predictions.
- **Pre-trained ML Model:** Uses a regression model trained on the Boston housing dataset.
- **Modern UI:** Styled with Bootstrap and custom CSS for a clean, responsive look.

---

## 🏗️ Project Structure

```
.
├── app.py
├── requirements.txt
├── Dockerfile
├── data/
│   └── boston.csv
├── model/
│   ├── house_price_pred.ipynb
│   ├── regmodel.pkl
│   └── scaler.pkl
├── static/
│   └── style.css
└── templates/
    └── home.html
```

---

## ⚡ Installation & Usage

### 1. Clone the Repository

```sh
git clone https://github.com/yourusername/house_price_prediction.git
cd house_price_prediction
```

### 2. Create a Virtual Environment (Recommended)

```sh
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

### 4. Run the Application

```sh
python app.py
```

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

##  Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [scikit-learn](https://scikit-learn.org/)
- [Bootstrap](https://getbootstrap.com/)
- Boston Housing Dataset

---

