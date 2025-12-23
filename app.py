import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("model.joblib")

st.set_page_config(
    page_title="InsureSense | Medical Insurance Cost Estimation",
    layout="wide"
)

# ================= CUSTOM CSS =================
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0f172a, #020617);
}

.main {
    background: transparent;
}

.app-container {
    max-width: 1200px;
    margin: auto;
    padding: 40px;
}

.title {
    font-size: 42px;
    font-weight: 700;
    color: #e5e7eb;
}

.subtitle {
    font-size: 16px;
    color: #9ca3af;
    margin-bottom: 35px;
}

.glass-card {
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(12px);
    border-radius: 16px;
    padding: 25px;
    box-shadow: 0px 10px 30px rgba(0,0,0,0.4);
    margin-bottom: 25px;
}

.section-title {
    font-size: 20px;
    font-weight: 600;
    color: #f9fafb;
    margin-bottom: 20px;
}

.label-text {
    color: #d1d5db;
}

.result-value {
    font-size: 36px;
    font-weight: 700;
    color: #38bdf8;
}

.bmi-value {
    font-size: 28px;
    font-weight: 600;
    color: #facc15;
}

.note {
    font-size: 13px;
    color: #9ca3af;
}
</style>
""", unsafe_allow_html=True)

# ================= APP UI =================
st.markdown('<div class="app-container">', unsafe_allow_html=True)

st.markdown('<div class="title">InsureSense</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">'
    'An intelligent system that estimates medical insurance costs using personal, '
    'health, and lifestyle attributes.'
    '</div>',
    unsafe_allow_html=True
)

# Input Section
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Personal & Health Details</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    age = st.slider("Age", 18, 100, 30)
    sex = st.selectbox("Gender", ["male", "female"])

with col2:
    height = st.slider("Height (cm)", 140, 210, 170)
    weight = st.slider("Weight (kg)", 40, 150, 70)

with col3:
    children = st.number_input("Number of Dependents", 0, 10, 0)
    smoker = st.selectbox("Smoking Status", ["yes", "no"])

region = st.selectbox(
    "Residential Region",
    ["northeast", "northwest", "southeast", "southwest"]
)

st.markdown('</div>', unsafe_allow_html=True)

# BMI Calculation
height_m = height / 100
bmi = weight / (height_m ** 2)

input_df = pd.DataFrame({
    "age": [age],
    "sex": [sex],
    "bmi": [bmi],
    "children": [children],
    "smoker": [smoker],
    "region": [region]
})

# Predict Button
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
predict = st.button("Generate Insurance Cost Estimate", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# Result Section
if predict:
    prediction = model.predict(input_df)[0]

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Estimated Outcome</div>', unsafe_allow_html=True)

    r1, r2 = st.columns(2)

    with r1:
        st.markdown("Body Mass Index")
        st.markdown(f'<div class="bmi-value">{bmi:.2f}</div>', unsafe_allow_html=True)

    with r2:
        st.markdown("Estimated Annual Insurance Cost")
        st.markdown(
            f'<div class="result-value">Rs {prediction:,.2f}</div>',
            unsafe_allow_html=True
        )

    st.markdown(
        '<div class="note">'
        'This estimation is generated using a machine learning model trained on historical insurance data. '
        'Actual costs may vary.'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
