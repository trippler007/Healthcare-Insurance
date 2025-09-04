import streamlit as st
import joblib
import numpy as np
import pandas as pd

model = joblib.load("model.joblib")

st.title("💡 Medical Insurance Cost Predictor")

st.write("Fill in the details below to estimate medical insurance charges.")

# Collect user input
age = st.number_input("Age", min_value=0, max_value=100, value=25)
sex = st.selectbox("Sex", ["male", "female"])
height = st.number_input("Height (in cm)", min_value=100.0, max_value=250.0, value=170.0)
weight = st.number_input("Weight (in kg)", min_value=30.0, max_value=200.0, value=70.0)
children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)
smoker = st.selectbox("Smoker", ["yes", "no"])
region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

# Calculate BMI internally
height_m = height / 100  # convert cm to meters
bmi = weight / (height_m ** 2)

# Convert input into dataframe (must match training preprocessing)
input_dict = {
    "age": [age],
    "sex": [sex],
    "bmi": [bmi],
    "children": [children],
    "smoker": [smoker],
    "region": [region],
}

input_df = pd.DataFrame(input_dict)

# Predict button
if st.button("Predict Insurance Charges"):
    prediction = model.predict(input_df)[0]
    st.info(f"Calculated BMI: {bmi:.2f}")
    st.success(f"Estimated Insurance Cost: Rs {prediction:,.2f}")
