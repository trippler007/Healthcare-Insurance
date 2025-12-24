import streamlit as st
import pandas as pd
import joblib

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="InsureSense | Medical Insurance Estimator",
    layout="wide"
)

# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------
model = joblib.load("model.joblib")

# --------------------------------------------------
# THEME (LIGHT SIDEBAR + BUTTONS)
# --------------------------------------------------
st.markdown("""
<style>

/* Global background */
body {
    background-color: #f8fafc;
}

/* Main container */
.block-container {
    max-width: 1100px;
    padding-top: 2.5rem;
    padding-bottom: 3rem;
}

/* Headings */
h1 {
    font-size: 42px;
    color: #0f172a;
    font-weight: 800;
}
h2 {
    font-size: 30px;
    color: #1e293b;
}
h3 {
    font-size: 22px;
    color: #334155;
}

/* Text */
p, li {
    font-size: 17px;
    color: #475569;
    line-height: 1.75;
}

/* ---------------- SIDEBAR ---------------- */
[data-testid="stSidebar"] {
    background-color: #e5e7eb;
    padding-top: 1rem;
}

[data-testid="stSidebar"] h1 {
    color: #0f172a;
}

/* Navigation container */
[data-testid="stSidebar"] .stRadio {
    background-color: #f1f5f9;
    padding: 0.6rem;
    border-radius: 12px;
}

/* Nav items */
[data-testid="stSidebar"] .stRadio label {
    padding: 0.6rem 0.8rem;
    border-radius: 8px;
    color: #0f172a;
    font-weight: 500;
}

/* Hover */
[data-testid="stSidebar"] .stRadio label:hover {
    background-color: #c7d2fe;
}

/* Selected */
[data-testid="stSidebar"] .stRadio label:has(input:checked) {
    background-color: #2563eb;
    color: white;
    font-weight: 600;
}

/* ---------------- BUTTONS ---------------- */
.stButton > button {
    background-color: #93c5fd;
    color: #0f172a;
    font-size: 16px;
    padding: 0.6rem 1.4rem;
    border-radius: 8px;
    border: none;
    font-weight: 600;
}

.stButton > button:hover {
    background-color: #60a5fa;
}

/* ---------------- CARDS ---------------- */
.card {
    background-color: white;
    padding: 1.8rem;
    border-radius: 14px;
    box-shadow: 0px 8px 24px rgba(0,0,0,0.05);
    margin-bottom: 2rem;
}

/* ---------------- METRICS ---------------- */
[data-testid="stMetric"] {
    background-color: #ffffff;
    padding: 1.2rem;
    border-radius: 12px;
    border-left: 5px solid #2563eb;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SIDEBAR NAVIGATION
# --------------------------------------------------
st.sidebar.title("InsureSense")

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Cost Estimator",
        "How It Works",
        "Insights & Factors",
        "About the Project"
    ]
)

# --------------------------------------------------
# HOME
# --------------------------------------------------
if page == "Home":
    st.title("InsureSense")
    st.subheader("Smart Medical Insurance Cost Estimation System")

    st.markdown("""
    <div class="card">
    <p>
    InsureSense is a machine learning based web application that estimates
    annual medical insurance costs using personal, health, and lifestyle data.
    </p>
    </div>
    """, unsafe_allow_html=True)

# --------------------------------------------------
# COST ESTIMATOR
# --------------------------------------------------
elif page == "Cost Estimator":
    st.header("Medical Insurance Cost Estimator")

    st.markdown("""
    <div class="card">
    <p>Enter your details below to estimate insurance cost.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.slider("Age", 18, 100, 30)
        sex = st.selectbox("Gender", ["male", "female"])

    with col2:
        height = st.slider("Height (cm)", 140, 210, 170)
        weight = st.slider("Weight (kg)", 40, 150, 70)

    with col3:
        smoker = st.selectbox("Smoking Status", ["yes", "no"])
        children = st.number_input("Number of Dependents", 0, 10, 0)

    region = st.selectbox(
        "Residential Region",
        ["northeast", "northwest", "southeast", "southwest"]
    )

    bmi = weight / ((height / 100) ** 2)

    input_df = pd.DataFrame({
        "age": [age],
        "sex": [sex],
        "bmi": [bmi],
        "children": [children],
        "smoker": [smoker],
        "region": [region]
    })

    if st.button("Generate Insurance Cost"):
        prediction = model.predict(input_df)[0]

        st.success("Insurance cost estimate generated")

        c1, c2 = st.columns(2)
        c1.metric("BMI", f"{bmi:.2f}")
        c2.metric("Estimated Annual Cost", f"₹ {prediction:,.2f}")

# --------------------------------------------------
# HOW IT WORKS
# --------------------------------------------------
elif page == "How It Works":
    st.header("How InsureSense Works")

    st.markdown("""
    <div class="card">
    <p>Data collection → Feature engineering → Model training → Prediction</p>
    </div>
    """, unsafe_allow_html=True)

# --------------------------------------------------
# INSIGHTS
# --------------------------------------------------
elif page == "Insights & Factors":
    st.header("Key Factors Affecting Insurance Cost")

    st.markdown("""
    <div class="card">
    <ul>
        <li>Age</li>
        <li>Smoking status</li>
        <li>BMI</li>
        <li>Dependents</li>
        <li>Region</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# --------------------------------------------------
# ABOUT PAGE (FIXED DATASET SECTION)
# --------------------------------------------------
elif page == "About the Project":
    st.header("About the Project")

    st.markdown("""
    <div class="card">
    <p>
    InsureSense demonstrates a real-world machine learning use case
    in healthcare insurance cost prediction.
    </p>

    <h3>Tech Stack</h3>
    <ul>
        <li>Python</li>
        <li>Pandas & NumPy</li>
        <li>Scikit-learn</li>
        <li>Streamlit</li>
        <li>Joblib</li>
    </ul>

    <h3>Dataset</h3>
    <p>
    Healthcare Insurance Dataset<br>
    <a href="https://healthcare-insurance-j6tw5lybbhumwmlrghpvp6.streamlit.app/#medical-insurance-cost-predictor" target="_blank">
    Access the dataset here
    </a>
    </p>

    <h3>Use Cases</h3>
    <ul>
        <li>ML Portfolio Project</li>
        <li>Healthcare Analytics</li>
        <li>Insurance Cost Estimation</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
