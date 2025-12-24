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
# CLEAN + READABLE COLOR THEME
# --------------------------------------------------
st.markdown("""
<style>

/* Background */
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
    margin-top: 2.5rem;
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

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #0f172a;
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] label {
    color: #e5e7eb;
}

/* Buttons */
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

/* Cards */
.card {
    background-color: white;
    padding: 1.8rem;
    border-radius: 14px;
    box-shadow: 0px 8px 24px rgba(0,0,0,0.05);
    margin-bottom: 2rem;
}

/* Metrics */
[data-testid="stMetric"] {
    background-color: #ffffff;
    padding: 1.2rem;
    border-radius: 12px;
    border-left: 5px solid #2563eb;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------
if "page" not in st.session_state:
    st.session_state.page = "Home"

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
    Medical insurance costs are influenced by a variety of factors including age,
    lifestyle habits, health indicators, and geographic location. For most individuals,
    understanding how these factors affect insurance pricing can be confusing and unclear.
    </p>

    <p>
    <b>InsureSense</b> is a machine learning powered web application that helps users
    estimate their annual medical insurance cost by analyzing key personal and health details.
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## Why InsureSense?")
    st.markdown("""
    <div class="card">
    <ul>
        <li>Rising healthcare costs make financial planning more important than ever</li>
        <li>Lifestyle choices like smoking significantly impact insurance premiums</li>
        <li>Data-driven predictions help users make informed healthcare decisions</li>
        <li>Provides quick, transparent, and easy-to-understand cost estimates</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## Who Can Use This?")
    st.markdown("""
    <div class="card">
    <ul>
        <li>Individuals planning to purchase health insurance</li>
        <li>Students learning applied machine learning</li>
        <li>Professionals exploring healthcare analytics</li>
        <li>Anyone curious about insurance cost drivers</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Start Cost Estimation"):
        st.session_state.page = "Cost Estimator"
        st.rerun()

# --------------------------------------------------
# COST ESTIMATOR PAGE
# --------------------------------------------------
elif page == "Cost Estimator":
    st.header("Medical Insurance Cost Estimator")

    st.markdown("""
    <div class="card">
    <p>
    Please enter accurate personal, health, and lifestyle information below.
    The machine learning model will analyze these inputs and generate an
    estimated annual insurance cost.
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### Personal & Health Details")

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

    # BMI
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

        st.caption("Disclaimer: This prediction is generated by a machine learning model and should be used for informational purposes only.")

# --------------------------------------------------
# HOW IT WORKS
# --------------------------------------------------
elif page == "How It Works":
    st.header("How InsureSense Works")

    st.markdown("""
    <div class="card">
    <h3>1. Data Collection</h3>
    <p>
    The model is trained on a real-world medical insurance dataset containing
    demographic information, lifestyle habits, and insurance charges.
    </p>

    <h3>2. Feature Engineering</h3>
    <p>
    Important features such as BMI are calculated, and categorical variables
    like gender, smoking status, and region are encoded.
    </p>

    <h3>3. Model Training</h3>
    <p>
    A supervised regression-based machine learning algorithm learns patterns
    between user attributes and insurance costs.
    </p>

    <h3>4. Prediction</h3>
    <p>
    When a user enters their information, the trained model predicts an
    estimated annual insurance cost.
    </p>
    </div>
    """, unsafe_allow_html=True)

# --------------------------------------------------
# INSIGHTS
# --------------------------------------------------
elif page == "Insights & Factors":
    st.header("Key Factors Affecting Insurance Cost")

    st.markdown("""
    <div class="card">
    <p>
    Medical insurance pricing depends on multiple interconnected factors.
    Understanding these factors helps users interpret the prediction results
    more effectively.
    </p>

    <ul>
        <li><b>Age:</b> Older individuals generally have higher medical risks</li>
        <li><b>Smoking:</b> Strongest factor influencing insurance premiums</li>
        <li><b>BMI:</b> Higher BMI increases likelihood of medical conditions</li>
        <li><b>Dependents:</b> More dependents increase total coverage cost</li>
        <li><b>Region:</b> Healthcare costs vary by geographic location</li>
    </ul>

    <p><b>Most influential factors:</b> Smoking status and BMI</p>
    </div>
    """, unsafe_allow_html=True)

# --------------------------------------------------
# ABOUT PAGE
# --------------------------------------------------
elif page == "About the Project":
    st.header("About the Project")

    st.markdown("""
    <div class="card">
    <p>
    InsureSense is an end-to-end machine learning project designed to demonstrate
    how data-driven models can be applied to real-world healthcare and insurance
    problems.
    </p>

    <p>
    The project focuses on model training, feature engineering, user interface
    design, and practical deployment using Streamlit.
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
        <li>Machine learning portfolio project</li>
        <li>Educational demonstrations</li>
        <li>Healthcare cost analysis</li>
        <li>Insurance pricing insights</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
