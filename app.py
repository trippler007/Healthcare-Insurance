import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("model.joblib")

# Page config
st.set_page_config(page_title="Medical Insurance Predictor", page_icon="💊", layout="wide")

# Title
st.title("💡 Medical Insurance Cost Predictor")
st.markdown("Estimate your **medical insurance charges** by providing the details below:")

# Input columns
col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", 0, 100, 25)
    sex = st.radio("Sex", ["male", "female"])
    children = st.number_input("Number of Children", 0, 10, 0)
    smoker = st.radio("Smoker", ["yes", "no"])

with col2:
    height = st.slider("Height (cm)", 100, 250, 170)
    weight = st.slider("Weight (kg)", 30, 200, 70)
    region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

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

# Predict button
if st.button("Predict Insurance Charges"):
    prediction = model.predict(input_df)[0]
    
    # Show results in two side-by-side cards
    res_col1, res_col2 = st.columns(2)
    res_col1.metric("💪 BMI", f"{bmi:.2f}")
    res_col2.metric("💰 Estimated Cost", f"Rs {prediction:,.2f}")
    
    st.success("✅ Prediction complete!")
