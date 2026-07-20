import streamlit as st
import pandas as pd
import joblib

model = joblib.load("fraud_detection_rf_pipeline.pkl")

st.title("Fraud Detection Prediction App")
st.subheader("Predict whether a financial transaction is fraudulent using a trained machine learning model.")
st.divider()

st.markdown("### 💳 Transaction Information")



transaction_type = st.selectbox("Transaction type",["TRANSFER","CASH_OUT","CASH_IN","DEBIT","PAYMENT"])

amount = st.number_input("Amount",min_value=0.0,value=1000.0, step=1000.0)

st.divider()

col1,col2 = st.columns(2)

with col1:

    st.markdown("#### 👤 Sender Account ")
    st.divider()

    oldbalanceOrg = st.number_input("Balance Before", min_value=0.0, value=10000.0 , step=1000.0)

    newbalanceOrig = st.number_input("Balance After", min_value=0.0, value=9000.0 , step=1000.0)


with col2:

    st.markdown("#### 👤Receiver Account")
    st.divider()

    oldbalanceDest = st.number_input("Balance Before", min_value=0.0, value=0.0 , step=1000.0)

    newbalanceDest = st.number_input("Balance After", min_value=0.0, value=0.0 , step=1000.0)

st.divider()

if st.button("🔍 Predict Fraud"):
    input_data = pd.DataFrame([
        {
            "type" : transaction_type,
            "amount" : amount,
            "oldbalanceOrg" : oldbalanceOrg,
            "newbalanceOrig" : newbalanceOrig,
            "oldbalanceDest" : oldbalanceDest,
            "newbalanceDest" : newbalanceDest
        }
    ])

    proba = model.predict_proba(input_data)[0]
    fraud_prob = proba[1]  # probability of class 1 (fraud)

    st.subheader(f" 📊 Fraud Probability: {fraud_prob:.2%}")

    st.progress(fraud_prob)

    threshold = 0.25  # tuned based on precision-recall analysis
    if fraud_prob >= threshold:
        st.error(f"⚠️🚨 Fraudulent Transaction Detected ({fraud_prob:.2%} confidence)")
    else:
        st.success(f"✅ Legitimate Transaction ({(1 - fraud_prob):.2%} confidence)")

    