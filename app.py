import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load model
model = joblib.load("model.joblib")

# Page configuration
st.set_page_config(page_title="Medical Insurance Predictor", page_icon="💊", layout="centered")

# Title
st.title("💡 Medical Insurance Cost Predictor")
st.markdown("Estimate your **medical insurance charges** by providing the details below.")

# Sidebar inputs
st.sidebar.header("Input Details")

age = st.sidebar.slider("Age", 0, 100, 25)
sex = st.sidebar.radio("Sex", ["male", "female"])
height = st.sidebar.slider("Height (cm)", 100, 250, 170)
weight = st.sidebar.slider("Weight (kg)", 30, 200, 70)
children = st.sidebar.number_input("Number of Children", 0, 10, 0)
smoker = st.sidebar.radio("Smoker", ["yes", "no"])
region = st.sidebar.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

# Calculate BMI
height_m = height / 100
bmi = weight / (height_m ** 2)

# Prepare input for model
input_dict = {
    "age": [age],
    "sex": [sex],
    "bmi": [bmi],
    "children": [children],
    "smoker": [smoker],
    "region": [region],
}
input_df = pd.DataFrame(input_dict)

# Predict button in main page
st.markdown("### Results")
if st.button("Predict Insurance Charges"):
    prediction = model.predict(input_df)[0]
    
    # Display results in columns
    col1, col2 = st.columns(2)
    col1.metric("💪 BMI", f"{bmi:.2f}")
    col2.metric("💰 Estimated Cost", f"Rs {prediction:,.2f}")
    
    st.success("✅ Prediction complete!")
