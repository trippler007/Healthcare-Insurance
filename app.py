import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load trained model
model = joblib.load(open("model.joblib", "rb"))

st.title("💡 Medical Insurance Cost Predictor")

st.write("Fill in the details below to estimate medical insurance charges.")

# Collect user input
age = st.number_input("Age", min_value=0, max_value=100, value=25)
sex = st.selectbox("Sex", ["male", "female"])
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)
smoker = st.selectbox("Smoker", ["yes", "no"])
region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

# Convert input into dataframe (must match training preprocessing)
input_dict = {
    "age": [age],
    "sex": [1 if sex == "male" else 0],  # Label encoding
    "bmi": [bmi],
    "children": [children],
    "smoker": [1 if smoker == "yes" else 0],  # Label encoding
    "region_northeast": [1 if region == "northeast" else 0],
    "region_northwest": [1 if region == "northwest" else 0],
    "region_southeast": [1 if region == "southeast" else 0],
    "region_southwest": [1 if region == "southwest" else 0],
}

input_df = pd.DataFrame(input_dict)

# Predict button
if st.button("Predict Insurance Charges"):
    prediction = model.predict(input_df)[0]
    st.success(f"Estimated Insurance Cost: Rs {prediction:,.2f}")
