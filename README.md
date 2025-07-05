# 🏦 Loan Approval Prediction App

This is a web-based application that allows users to simulate a loan application and instantly receive a prediction of whether the loan would be **approved** or **rejected**. The prediction is made using a machine learning model trained on real loan application data.

## 📌 What does this app do?

This project uses a classification model to determine the outcome of a loan request based on several applicant features such as income, credit score, assets, and employment status.

The goal is to demonstrate how machine learning can assist financial institutions in automating decision-making processes and also serve as a professional portfolio project.

---

## 📁 Dataset source

The dataset used to train this model was obtained from Kaggle:

🔗 [Loan Approval Prediction Dataset on Kaggle](https://www.kaggle.com/datasets/architsharma01/loan-approval-prediction-dataset)

---

## 🧠 How does it work?

The app was developed using:
- **Python**
- **Scikit-learn** (for machine learning)
- **Streamlit** (for the web app)
- **Pandas** (for data handling)

The core model is an **ensemble of classifiers** (Random Forest, Logistic Regression, SVM) combined using a **Voting Classifier**. The model was optimized via Grid Search and trained with scaled and preprocessed data.

---

## 🚀 How to run the app locally

> Requirements: Python 3.8+ installed on your system

### Step 1: Clone this repository
```bash
git clone https://github.com/your-username/loan-approval-app.git
cd loan-approval-app
```

### Step 2: Create and activate a virtual environment (optional but recommended)

#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the app
```bash
streamlit run loan_predictor_app.py
```

Your browser will open a local server where you can interact with the loan prediction form.

---

## 🧪 Example use case

Fill in the form fields such as:

- Annual income
- Loan amount
- Loan term
- Number of dependents
- Education level
- Credit score (CIBIL)
- Values of assets (residential, commercial, luxury, bank)

Click **Predict Loan Status**, and the app will show whether the loan would be approved or rejected according to the trained model.

---

## 📁 Files in this project

- `loan_predictor_app.py`: Main Streamlit application.
- `loan_approval_model.pkl`: Trained ensemble model.
- `scaler.pkl`: Scaler used during training (to ensure consistent input processing).
- `loan_approval_dataset.csv`: Original dataset used to train the model.
- `loan_predictor.ipynb`: Jupyter notebook used for data exploration, model training and evaluation.
- `requirements.txt`: List of dependencies.
- `README.md`: You’re reading it!

---

## 👨‍💻 Author

Created with care and curiosity by Agustin Gorrin.  
This project is part of my data analytics and machine learning portfolio.

---

## 📫 Contact

Feel free to connect or reach out via:

- GitHub: [github.com/gus12green](https://github.com/gus12green)
- LinkedIn: [linkedin.com/in/agustín-gorrín-santana/](https://linkedin.com/in/agustín-gorrín-santana/)

---

## ⚠️ Disclaimers

- This app is **not for commercial use** and is purely educational and demonstrative.  
  I do **not profit** in any way from its use or from the underlying dataset.

- This app runs **entirely on your local machine**. No data entered into the calculator is collected, transmitted or stored anywhere.  
  **You retain complete privacy over any information entered in the form.**
