import streamlit as st
import pandas as pd
import joblib

# Load model and scaler
model = joblib.load("loan_approval_model.pkl")
scaler = joblib.load("scaler.pkl")

# Column structure expected by the model (with original spacing preserved)
EXPECTED_COLUMNS = [
    'no_of_dependents',
    'income_annum',
    'loan_amount',
    'loan_term',
    'cibil_score',
    'residential_assets_value',
    'commercial_assets_value',
    'luxury_assets_value',
    'bank_asset_value',
    'education_ Not Graduate',
    'self_employed_ Yes          '
]

def preprocess_input(data):
    df = pd.DataFrame([data])
    
    # DO NOT strip strings; keep original spacing to match model
    df = pd.get_dummies(df)
    df = df.reindex(columns=EXPECTED_COLUMNS, fill_value=0)
    df_scaled = scaler.transform(df)
    return df_scaled

def predict(data):
    processed = preprocess_input(data)
    result = model.predict(processed)
    return "Approved" if result[0] == 1 else "Rejected"

# Streamlit UI
st.set_page_config(page_title="Loan Approval Predictor")
st.title("Loan Approval Prediction App")
st.write("Fill out the information below to check if your loan might be approved.")

# Input form
with st.form("loan_form"):
    no_of_dependents = st.number_input("Number of Dependents", min_value=0, step=1)
    education = st.selectbox("Education Level", ["Graduate", "Not Graduate"])
    self_employed = st.selectbox("Self-Employed", ["No", "Yes"])
    income_annum = st.number_input("Annual Income ($)", min_value=0.0, step=100.0)
    loan_amount = st.number_input("Loan Amount ($)", min_value=0.0, step=100.0)
    loan_term = st.number_input("Loan Term (in months)", min_value=1, step=1)
    cibil_score = st.number_input("CIBIL Score", min_value=300, max_value=900, step=1)
    residential_assets_value = st.number_input("Residential Assets Value ($)", min_value=0.0, step=100.0)
    commercial_assets_value = st.number_input("Commercial Assets Value ($)", min_value=0.0, step=100.0)
    luxury_assets_value = st.number_input("Luxury Assets Value ($)", min_value=0.0, step=100.0)
    bank_asset_value = st.number_input("Bank Assets Value ($)", min_value=0.0, step=100.0)

    submitted = st.form_submit_button("Predict Loan Status")

    if submitted:
        user_data = {
            'no_of_dependents': no_of_dependents,
            'education': education,
            'self_employed': self_employed,
            'income_annum': income_annum,
            'loan_amount': loan_amount,
            'loan_term': loan_term,
            'cibil_score': cibil_score,
            'residential_assets_value': residential_assets_value,
            'commercial_assets_value': commercial_assets_value,
            'luxury_assets_value': luxury_assets_value,
            'bank_asset_value': bank_asset_value
        }

        prediction = predict(user_data)
        st.subheader(f"Loan Status: {prediction}")
