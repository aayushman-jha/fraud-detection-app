# 💳 Fraud Detection Pipeline

A machine learning application that predicts whether a financial transaction is **Fraudulent** or **Legitimate** using a Scikit-learn pipeline deployed with Streamlit.

🔗 **Live Demo:** https://fraud-detection-pipeline.streamlit.app/

---

## Overview

Financial institutions process millions of transactions every day, making fraud detection a critical component of secure digital payments.

This project demonstrates an end-to-end machine learning workflow that classifies financial transactions based on key transaction attributes. The model is deployed as an interactive Streamlit application where users can enter transaction details and receive an instant prediction.

---

## Features

- Real-time fraud prediction
- Interactive Streamlit web application
- End-to-end Scikit-learn Pipeline
- Automatic preprocessing of categorical and numerical features
- Clean and responsive user interface
- Deployable machine learning solution

---

## Input Features

The application uses the following transaction information:

- Transaction Type
- Transaction Amount
- Sender Balance Before Transaction
- Sender Balance After Transaction
- Receiver Balance Before Transaction
- Receiver Balance After Transaction

---

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit

---

## Project Structure

```text
Fraud-Detection-Pipeline/
│
├── streamlit_app.py
├── fraud_detection_rf_pipeline.pkl
├── requirements.txt
├── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/Fraud-Detection-Pipeline.git
```

Navigate to the project directory:

```bash
cd Fraud-Detection-Pipeline
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run streamlit_app.py
```

---

**AAYUSHMAN JHA**
