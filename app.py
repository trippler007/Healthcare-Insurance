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
# THEME + SIDEBAR FIX (FULL)
# --------------------------------------------------
st.markdown("""
<style>

/* -------------------------------
   GLOBAL BACKGROUND
--------------------------------*/
body {
    background-color: #f8fafc;
}

/* Main container */
.block-container {
    max-width: 1100px;
    padding-top: 2.5rem;
    padding-bottom: 3rem;
}

/* -------------------------------
   HEADINGS
--------------------------------*/
h1 {
    font-size: 42px;
    color: #0f172a;
    font-weight: 800;
}

h2 {
    font-size: 30px;
    color: #1e293b;
    margin-top: 2.5rem;
}

h3 {
    font-size: 22px;
    color: #334155;
}

/* -------------------------------
   TEXT
--------------------------------*/
p, li {
    font-size: 17px;
    color: #475569;
    line-height: 1.75;
}

/* -------------------------------
   SIDEBAR
--------------------------------*/
[data-testid="stSidebar"] {
    background-color: #0f172a;
    padding-top: 1rem;
}

[data-testid="stSidebar"] h1 {
    color: #f8fafc;
}

/* Radio container */
[data-testid="stSidebar"] .stRadio {
    background-color: #0f172a;
    padding: 0.5rem;
    border-radius: 10px;
}

/* Each nav item */
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] > label {
    background-color: transparent;
    padding: 0.6rem 0.8rem;
    margin-bottom: 0.3rem;
    border-radius: 8px;
    color: #e5e7eb;
    transition: all 0.2s ease-in-out;
}

/* Hover */
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] > label:hover {
    background-color: #1e293b;
    cursor: pointer;
}

/* Selected */
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] > label:has(input:checked) {
    background-color: #e5e7eb;
    color: #0f172a;
    font-weight: 600;
}

/* -------------------------------
   BUTTONS
--------------------------------*/
.stButton > button {
    background-color: #2563eb;
    color: white;
    font-size: 16px;
    padding: 0.6rem 1.4rem;
    border-radius: 8px;
    border: none;
}

.stButton > button:hover {
    background-color: #1d4ed8;
}

/* -------------------------------
   CARDS
--------------------------------*/
.card {
    background-color: white;
    padding: 1.8rem;
    border-radius: 14px;
    box-shadow: 0px 8px 24px rgba(0,0,0,0.05);
    margin-bottom: 2rem;
}

/* -------------------------------
   METRICS
--------------------------------*/
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
# HOME PAGE
# --------------------------------------------------
if page == "Home":
    st.title("InsureSense")
    st.subheader("Smart Medical Insurance Cost Estimation System")

    st.markdown("""
    <div class="card">
    <p>
    Medical insurance costs depend on age, lifestyle habits, health indicators,
    and regional factors. Understanding these costs beforehand helps individuals
    plan healthcare expenses more effectively.
    </p>

    <p>
    <b>InsureSense</b> is a machine learning powered web application that estimates
    annual medical insurance costs using user-provided information.
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## Why InsureSense?")
    st.markdown("""
    <div class="card">
    <ul>
        <li>Healthcare costs are rising every year</li>
        <li>Lifestyle choices directly affect insurance premiums</li>
        <li>Machine learning provides transparent cost estimation</li>
        <li>Helps in financial and healthcare planning</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## Who Can Use This?")
    st.markdown("""
    <div class="card">
    <ul>
        <li>Individuals planning health insurance</li>
        <li>Students learning applied machine learning</li>
        <li>Healthcare analytics enthusiasts</li>
        <li>Portfolio & academic projects</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# --------------------------------------------------
# COST ESTIMATOR
# --------------------------------------------------
elif page == "Cost Estimator":
    st.header("Medical Insurance Cost Estimator")

    st.markdown("""
    <div class="card">
    <p>
    Enter accurate personal, health, and lifestyle details below.
    The system will generate an estimated annual insurance cost.
    </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.slider("Age (years)", 18, 100, 30)
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

    if st.button("Generate Insurance Cost"):
        prediction = model.predict(input_df)[0]

        st.success("Insurance cost estimate generated successfully")

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Calculated BMI", f"{bmi:.2f}")
        with col2:
            st.metric("Estimated Annual Cost", f"₹ {prediction:,.2f}")

        st.caption("This prediction is for informational purposes only.")

# --------------------------------------------------
# HOW IT WORKS
# --------------------------------------------------
elif page == "How It Works":
    st.header("How InsureSense Works")

    st.markdown("""
    <div class="card">
    <h3>1. Data Collection</h3>
    <p>Real-world medical insurance dataset is used.</p>

    <h3>2. Feature Engineering</h3>
    <p>BMI calculation and categorical encoding.</p>

    <h3>3. Model Training</h3>
    <p>Regression-based supervised learning model.</p>

    <h3>4. Prediction</h3>
    <p>User inputs are converted into insurance cost estimate.</p>
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
        <li><b>Age:</b> Higher age increases risk</li>
        <li><b>Smoking:</b> Most influential factor</li>
        <li><b>BMI:</b> Indicates health risk</li>
        <li><b>Dependents:</b> Coverage increases cost</li>
        <li><b>Region:</b> Healthcare cost varies geographically</li>
    </ul>

    <p><b>Most influential:</b> Smoking status & BMI</p>
    </div>
    """, unsafe_allow_html=True)

# --------------------------------------------------
# ABOUT
# --------------------------------------------------
elif page == "About the Project":
    st.header("About the Project")

    st.markdown("""
    <div class="card">
    <p>
    InsureSense is an end-to-end machine learning project demonstrating
    healthcare insurance cost prediction using real-world data.
    </p>

    <h3>Technology Stack</h3>
    <ul>
        <li>Python</li>
        <li>Pandas & NumPy</li>
        <li>Scikit-learn</li>
        <li>Streamlit</li>
        <li>Joblib</li>
    </ul>

    <h3>Use Cases</h3>
    <ul>
        <li>ML Portfolio Project</li>
        <li>Educational Demonstration</li>
        <li>Healthcare Analytics</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
