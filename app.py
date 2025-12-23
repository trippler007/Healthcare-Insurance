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
# BASIC READABLE THEME
# --------------------------------------------------
st.markdown("""
<style>
body {
    background-color: #f9fafb;
}
h1, h2, h3 {
    color: #0f172a;
}
p, li {
    color: #334155;
    font-size: 15px;
}
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SESSION STATE FOR NAVIGATION
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
    ],
    index=[
        "Home",
        "Cost Estimator",
        "How It Works",
        "Insights & Factors",
        "About the Project"
    ].index(st.session_state.page)
)

st.session_state.page = page

# --------------------------------------------------
# HOME PAGE
# --------------------------------------------------
if page == "Home":
    st.title("InsureSense")
    st.subheader("Medical Insurance Cost Estimation using Machine Learning")

    st.markdown("""
    Healthcare insurance costs depend on multiple personal, health, and lifestyle factors.
    This application estimates medical insurance charges using a machine learning model
    trained on real-world insurance data.
    """)

    st.markdown("### Why this matters")
    st.markdown("""
    - Healthcare costs are rising and difficult to predict  
    - Lifestyle choices like smoking and BMI impact insurance pricing  
    - Data-driven estimates support better financial planning  
    """)

    if st.button("Estimate Your Insurance Cost"):
        st.session_state.page = "Cost Estimator"
        st.rerun()

# --------------------------------------------------
# COST ESTIMATOR PAGE
# --------------------------------------------------
elif page == "Cost Estimator":
    st.header("Medical Insurance Cost Estimator")
    st.write("Enter your personal and health details below.")

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

    predict = st.button("Generate Cost Estimate")

    if predict:
        prediction = model.predict(input_df)[0]

        st.success("Insurance cost estimated successfully")

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Body Mass Index (BMI)", f"{bmi:.2f}")
        with col2:
            st.metric("Estimated Annual Cost", f"Rs {prediction:,.2f}")

        st.caption("This estimate is for informational purposes only.")

# --------------------------------------------------
# HOW IT WORKS PAGE
# --------------------------------------------------
elif page == "How It Works":
    st.header("How the System Works")

    st.markdown("""
    **1. Data Collection**  
    The dataset includes age, BMI, smoking status, dependents, region, and insurance charges.

    **2. Feature Processing**  
    Categorical features are encoded and BMI is calculated.

    **3. Model Training**  
    A supervised machine learning regression model is trained on historical insurance data.

    **4. Prediction**  
    User inputs are processed and passed to the trained model to estimate insurance cost.
    """)

# --------------------------------------------------
# INSIGHTS PAGE
# --------------------------------------------------
elif page == "Insights & Factors":
    st.header("Key Factors Affecting Insurance Cost")

    st.markdown("""
    - **Age:** Insurance cost generally increases with age  
    - **Smoking:** Smoking significantly raises insurance charges  
    - **BMI:** Higher BMI is associated with increased healthcare risk  
    - **Dependents:** More dependents can increase coverage cost  
    - **Region:** Insurance pricing varies across regions  
    """)

    st.markdown("**Most impactful factors:** Smoking status and BMI")

# --------------------------------------------------
# ABOUT PAGE
# --------------------------------------------------
elif page == "About the Project":
    st.header("About the Project")

    st.markdown("""
    This project demonstrates the application of machine learning in predicting healthcare
    insurance costs based on demographic and lifestyle attributes.
    """)

    st.markdown("### Tech Stack")
    st.markdown("""
    - Python  
    - Pandas, NumPy  
    - Scikit-learn  
    - Streamlit  
    - Joblib  
    """)

    st.markdown("### Dataset")
    st.markdown("""
    Healthcare Insurance Dataset  
    [Click here to access the dataset](https://healthcare-insurance-j6tw5lybbhumwmlrghpvp6.streamlit.app/#medical-insurance-cost-predictor)
    """)

    st.markdown("### Use Case")
    st.markdown("""
    - Educational purposes  
    - Financial planning insights  
    - Healthcare analytics demonstration  
    """)
