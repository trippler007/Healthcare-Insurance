import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("model.joblib")

# Page configuration
st.set_page_config(
    page_title="HealthSure | Medical Insurance Cost Estimator",
    layout="wide"
)

# Custom CSS for professional styling
st.markdown("""
<style>
    .main {
        background-color: #f7f9fc;
    }
    .title-text {
        font-size: 38px;
        font-weight: 700;
        color: #1f2933;
    }
    .subtitle-text {
        font-size: 16px;
        color: #4b5563;
        margin-bottom: 25px;
    }
    .section-header {
        font-size: 22px;
        font-weight: 600;
        color: #111827;
        margin-top: 30px;
        margin-bottom: 15px;
    }
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    .result-value {
        font-size: 28px;
        font-weight: 700;
        color: #0f172a;
    }
    .result-label {
        font-size: 14px;
        color: #6b7280;
    }
</style>
""", unsafe_allow_html=True)

# Title section
st.markdown('<div class="title-text">HealthSure: Medical Insurance Cost Estimator</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle-text">'
    'Predict estimated medical insurance charges based on personal, lifestyle, '
    'and demographic information using a machine learning model.'
    '</div>',
    unsafe_allow_html=True
)

# Input section
st.markdown('<div class="section-header">Personal & Lifestyle Information</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        age = st.slider("Age", 18, 100, 25)
        sex = st.selectbox("Gender", ["male", "female"])
        children = st.number_input("Number of Dependents", 0, 10, 0)
        smoker = st.selectbox("Smoking Status", ["yes", "no"])
        st.markdown('</div>', unsafe_allow_html=True)

with col2:
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        height = st.slider("Height (cm)", 140, 210, 170)
        weight = st.slider("Weight (kg)", 40, 150, 70)
        region = st.selectbox(
            "Residential Region",
            ["northeast", "northwest", "southeast", "southwest"]
        )
        st.markdown('</div>', unsafe_allow_html=True)

# BMI calculation
height_m = height / 100
bmi = weight / (height_m ** 2)

# Prepare input for model
input_df = pd.DataFrame({
    "age": [age],
    "sex": [sex],
    "bmi": [bmi],
    "children": [children],
    "smoker": [smoker],
    "region": [region]
})

# Prediction section
st.markdown('<div class="section-header">Prediction Result</div>', unsafe_allow_html=True)

predict_col1, predict_col2 = st.columns([1, 3])

with predict_col1:
    predict_button = st.button("Estimate Insurance Cost", use_container_width=True)

with predict_col2:
    st.markdown(
        "Click the button to calculate your estimated medical insurance charges "
        "based on the provided information."
    )

if predict_button:
    prediction = model.predict(input_df)[0]

    result_col1, result_col2 = st.columns(2)

    with result_col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="result-label">Calculated Body Mass Index</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="result-value">{bmi:.2f}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with result_col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="result-label">Estimated Annual Insurance Cost</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="result-value">Rs {prediction:,.2f}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.info(
        "This estimate is generated using a machine learning model trained on historical "
        "insurance data and should be used for informational purposes only."
    )
