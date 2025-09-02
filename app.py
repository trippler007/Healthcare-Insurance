import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load model and columns
model = pickle.load(open("model.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

st.title("💊 Medical Insurance Charges Prediction")

# User Inputs
age = st.number_input("Age", min_value=0, max_value=100, value=25)
sex = st.selectbox("Sex", ["male", "female"])
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)
smoker = st.selectbox("Smoker", ["yes", "no"])
region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

# Convert inputs to DataFrame
input_data = pd.DataFrame([[age, sex, bmi, children, smoker, region]], 
                          columns=['age', 'sex', 'bmi', 'children', 'smoker', 'region'])

# Apply same preprocessing as training
input_data['sex'] = input_data['sex'].map({'female':0, 'male':1})
input_data['smoker'] = input_data['smoker'].map({'no':0, 'yes':1})
input_data = pd.get_dummies(input_data, columns=['region'], dtype=int)

# Ensure same column order
for col in columns:
    if col not in input_data:
        input_data[col] = 0
input_data = input_data[columns]

# Predict
if st.button("Predict Charges"):
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated Insurance Charges: ${prediction:,.2f}")
