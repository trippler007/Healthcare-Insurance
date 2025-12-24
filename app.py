import streamlit as st
import pandas as pd
import joblib

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="InsureSense | Insurance Cost Estimator",
    layout="wide"
)

# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------
model = joblib.load("model.joblib")

# --------------------------------------------------
# MODERN COLOR THEME
# --------------------------------------------------
st.markdown("""
<style>

/* Background */
body {
    background-color: #f1f5f9;
}

/* Main container */
.block-container {
    max-width: 1050px;
    padding-top: 3rem;
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
    line-height: 1.8;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f172a, #1e293b);
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] label {
    color: #e5e7eb;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(90deg, #2563eb, #1d4ed8);
    color: white;
    font-size: 16px;
    padding: 0.6rem 1.4rem;
    border-radius: 8px;
    border: none;
    transition: 0.2s ease-in-out;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #1d4ed8, #1e40af);
    transform: translateY(-2px);
}

/* Inputs */
input, select {
    border-radius: 8px !important;
}

/* Metrics */
[data-testid="stMetric"] {
    background-color: #ffffff;
    padding: 1.3rem;
    border-radius: 14px;
    border-left: 6px solid #2563eb;
    box-shadow: 0px 8px 24px rgba(0,0,0,0.05);
}

/* Success alert */
.stAlert {
    background-color: #ecfeff;
    border-left: 6px solid #06b6d4;
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

st.session_state.page = page

# --------------------------------------------------
# HOME PAGE
# --------------------------------------------------
if page == "Home":
    st.title("InsureSense")
    st.subheader("Medical Insurance Cost Estimation using Machine Learning")

    st.markdown("""
    InsureSense ek machine learning based system hai jo aapke personal,
    health aur lifestyle details ke basis par annual medical insurance
    cost estimate karta hai.
    """)

    st.markdown("### 🔹 Why this matters")
    st.markdown("""
    - Healthcare costs rapidly badh rahe hain  
    - Smoking aur BMI insurance price ko kaafi impact karte hain  
    - Data-based estimates better financial planning me help karte hain  
    """)

    if st.button("Estimate Your Insurance Cost"):
        st.session_state.page = "Cost Estimator"
        st.rerun()

# --------------------------------------------------
# COST ESTIMATOR PAGE
# --------------------------------------------------
elif page == "Cost Estimator":
    st.header("Medical Insurance Cost Estimator")

    st.markdown("### 👤 User Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.slider("Age", 18, 100, 30)
        sex = st.selectbox("Gender", ["male", "female"])

    with col2:
        height = st.slider("Height (cm)", 140, 210, 170)
        weight = st.slider("Weight (kg)", 40, 150, 70)

    with col3:
        smoker = st.selectbox("Smoking Status", ["yes", "no"])
        children = st.number_input("Number of Children", 0, 10, 0)

    region = st.selectbox(
        "Residential Region",
        ["northeast", "northwest", "southeast", "southwest"]
    )

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

    if st.button("Generate Cost Estimate"):
        prediction = model.predict(input_df)[0]

        st.success("Insurance cost estimate generated successfully!")

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Body Mass Index (BMI)", f"{bmi:.2f}")
        with col2:
            st.metric("Estimated Annual Cost", f"₹ {prediction:,.2f}")

        st.caption("⚠ This is an estimated value for informational purposes only.")

# --------------------------------------------------
# HOW IT WORKS
# --------------------------------------------------
elif page == "How It Works":
    st.header("How InsureSense Works")

    st.markdown("""
    **Step 1:** Healthcare insurance dataset se model training  
    **Step 2:** Categorical features encoding & BMI calculation  
    **Step 3:** Regression-based machine learning model training  
    **Step 4:** User inputs se insurance cost prediction  
    """)

# --------------------------------------------------
# INSIGHTS PAGE
# --------------------------------------------------
elif page == "Insights & Factors":
    st.header("Key Factors Affecting Insurance Cost")

    st.markdown("""
    - **Age:** Age ke saath cost increase hoti hai  
    - **Smoking:** Sabse zyada influential factor  
    - **BMI:** Higher BMI = higher health risk  
    - **Children:** Dependents badhne se cost badhti hai  
    - **Region:** Location ke hisaab se pricing vary karti hai  
    """)

# --------------------------------------------------
# ABOUT PAGE
# --------------------------------------------------
elif page == "About the Project":
    st.header("About the Project")

    st.markdown("""
    Yeh project machine learning ka real-world healthcare use case
    demonstrate karta hai. Iska purpose education aur analytics hai.
    """)

    st.markdown("### 🛠 Tech Stack")
    st.markdown("""
    - Python  
    - Pandas & NumPy  
    - Scikit-learn  
    - Streamlit  
    - Joblib  
    """)

    st.markdown("### 🎯 Use Cases")
    st.markdown("""
    - ML portfolio project  
    - Healthcare analytics  
    - Insurance cost estimation  
    """)
