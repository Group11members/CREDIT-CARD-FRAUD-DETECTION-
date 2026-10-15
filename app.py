
import streamlit as st
from model import predict_fraud

st.set_page_config(
    page_title="Credit Card Fraud Detection",
    page_icon="💳",
    layout="wide"
)

# Page styling
st.markdown("""
<style>
.stApp {
    background-color: #0f172a;
    color: #f1f5f9;
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

h1, h2, h3 {
    color: #f8fafc;
}

div[data-testid="stNumberInput"] label {
    color: #dbeafe;
}

div[data-testid="stNumberInput"] input {
    background-color: #f8fafc;
    color: #111827;
}

div[data-testid="stFormSubmitButton"] button {
    background-color: #7c3aed;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 10px;
    font-weight: bold;
    width: 100%;
}

div[data-testid="stFormSubmitButton"] button:hover {
    background-color: #6d28d9;
    color: white;
}

.model-card {
    background-color: #1e293b;
    border: 1px solid #334155;
    border-radius: 12px;
    padding: 18px;
    margin-bottom: 15px;
}

.model-label {
    color: #c4b5fd;
    font-size: 14px;
}

.model-value {
    color: #f8fafc;
    font-size: 19px;
    font-weight: bold;
}

.footer {
    color: #94a3b8;
    text-align: center;
    font-size: 13px;
    margin-top: 35px;
}
</style>
""", unsafe_allow_html=True)


# Heading
st.title("💳 Credit Card Fraud Detection")
st.write("Predict potential fraud using a trained machine-learning model.")


# Model information
st.subheader("About the Model")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="model-card">
        <div class="model-label">Algorithm</div>
        <div class="model-value">Random Forest</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="model-card">
        <div class="model-label">Input Features</div>
        <div class="model-value">29 Features</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="model-card">
        <div class="model-label">Task</div>
        <div class="model-value">Binary Classification</div>
    </div>
    """, unsafe_allow_html=True)


# Disclaimer
st.warning(
    "**Disclaimer:** This academic project uses anonymized features "
    "V1–V28 and transaction Amount. The original meanings of V1–V28 "
    "are unavailable in the dataset representation. Predictions are "
    "estimates and may be incorrect; they are not definitive fraud "
    "determinations. Anonymized features alone do not guarantee "
    "complete privacy. Do not use predictions as the sole basis "
    "for financial decisions."
)


# Transaction form
st.subheader("Transaction Analysis")
st.caption("Enter the 29 feature values to generate a prediction.")

with st.form("transaction_form"):
    features = []
    columns = st.columns(3)

    for i in range(29):
        with columns[i % 3]:
            name = f"V{i + 1}" if i < 28 else "Amount"

            value = st.number_input(
                name,
                value=0.0,
                format="%.6f",
                key=name
            )

            features.append(value)

    submitted = st.form_submit_button("🔍 Predict Transaction")


# Prediction result
if submitted:
    try:
        prediction, probability = predict_fraud(features)

        st.subheader("Prediction Result")

        if prediction == 1:
            st.error("⚠️ Potentially Fraudulent Transaction")
        else:
            st.success("✅ Legitimate Transaction")

        if probability is not None:
            st.metric("Estimated Fraud Probability", f"{probability:.2%}")

        st.caption("The model's estimate is not a guarantee of the transaction's true status.")

    except Exception as error:
        st.error(f"Prediction failed: {error}")


# Footer
st.markdown("""
<div class="footer">
    Credit Card Fraud Detection | Machine Learning Capstone Project
</div>
""", unsafe_allow_html=True)
