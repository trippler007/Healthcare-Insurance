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
# LIGHT PINK THEME + CSS
# --------------------------------------------------
st.markdown("""
<style>
/* Whole page background */
body {
    background-color: #ffe0eb; /* soft light pink */
    color: #333333; /* dark gray text */
}

/* Page container padding */
.block-container {
    max-width: 1000px;
    padding-top: 3rem;
    padding-bottom: 3rem;
}

/* Headings - remove default Streamlit box */
h1, h2, h3 {
    background-color: #ffe0eb !important;
    box-shadow: none !important;
    padding: 0 !important;
    margin: 0.5rem 0 0.5rem 0;
    text-align: center;
    color: #c2185b;
}

/* Section cards */
.section {
    background-color: #ffffff;
    padding: 2rem;
    border-radius: 12px;
    margin-bottom: 2rem;
    box-shadow: none;
}

/* Buttons */
.stButton>button {
    background-color: #ff66b2; /* vibrant pink */
    color: white;
    font-size: 16px;
    padding: 0.6rem 1.2rem;
    border-radius: 8px;
    border: none;
    transition: background 0.3s;
}
.stButton>button:hover {
    background-color: #e65599;
}

/* Metrics / output boxes */
.stMetric {
    background-color: #ffe0eb;
    color: #333333;
    border-radius: 8px;
    padding: 1rem;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# TOP NAVIGATION
# --------------------------------------------------
tabs = ["Home", "Cost Estimator", "How It Works", "Insights & Factors", "About the Project"]
selected_tab = st.tabs(tabs)

# --------------------------------------------------
# HOME PAGE
# --------------------------------------------------
with selected_tab[0]:
    st.markdown('<div class="section">', unsafe_allow_html=True)

    st.markdown(
        """
        <h1>InsureSense</h1>
        <h3>Medical Insurance Cost Estimation using Machine Learning</h3>
        """,
        unsafe_allow_html=True
    )

    st.markdown("""
    Healthcare insurance costs are influenced by a combination of personal characteristics,
    health metrics, and lifestyle habits. Accurately estimating these costs can be challenging
    for individuals planning their healthcare expenses.

    InsureSense uses a machine learning model trained on real-world healthcare insurance data
    to provide an estimated annual insurance cost based on user-provided inputs.
    """)

    st.markdown("## Why this matters")
    st.markdown("""
    - Healthcare costs continue to rise globally  
    - Lifestyle choices such as smoking and body mass index strongly influence insurance pricing  
    - Data-driven cost estimates support informed financial and healthcare planning  
    """)

    st.markdown("### Get Started")
    if st.button("Estimate Your Insurance Cost"):
        st.experimental_rerun()  # Go to Cost Estimator tab
    st.markdown('</div>', unsafe_allow_html=True)

# --------------------------------------------------
# COST ESTIMATOR PAGE
# --------------------------------------------------
with selected_tab[1]:
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.header("Medical Insurance Cost Estimator")
    st.markdown("""
    Enter your personal, health, and lifestyle details below. The system will process
    this information and generate an estimated annual insurance cost.
    """)

    st.markdown("### User Information")
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

    st.markdown("### Generate Estimate")
    predict = st.button("Generate Cost Estimate")

    if predict:
        prediction = model.predict(input_df)[0]

        st.success("Insurance cost estimate generated successfully")

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Body Mass Index (BMI)", f"{bmi:.2f}")
        with col2:
            st.metric("Estimated Annual Cost", f"Rs {prediction:,.2f}")

        st.caption("This estimate is generated using a machine learning model and is for informational purposes only.")
    st.markdown('</div>', unsafe_allow_html=True)

# --------------------------------------------------
# HOW IT WORKS PAGE
# --------------------------------------------------
with selected_tab[2]:
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.header("How the System Works")

    st.markdown("""
    **Step 1: Data Collection**  
    The model is trained on a healthcare insurance dataset containing demographic,
    lifestyle, and regional information along with historical insurance charges.

    **Step 2: Feature Processing**  
    Categorical features such as gender, smoking status, and region are encoded.
    Body Mass Index (BMI) is calculated from height and weight.

    **Step 3: Model Training**  
    A supervised machine learning regression model learns patterns from historical
    insurance data.

    **Step 4: Prediction**  
    User inputs are passed to the trained model to estimate the insurance cost.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# --------------------------------------------------
# INSIGHTS & FACTORS PAGE
# --------------------------------------------------
with selected_tab[3]:
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.header("Key Factors Affecting Insurance Cost")

    st.markdown("""
    Several factors influence healthcare insurance pricing. Understanding these
    factors helps users interpret the estimated cost more effectively.
    """)

    st.markdown("""
    - **Age:** Insurance costs generally increase as age increases  
    - **Smoking Status:** Smoking has a significant impact on insurance charges  
    - **Body Mass Index (BMI):** Higher BMI often correlates with increased healthcare risk  
    - **Number of Dependents:** Additional dependents can raise total coverage cost  
    - **Geographic Region:** Insurance pricing varies across different regions  
    """)

    st.markdown("**Most influential factors:** Smoking status and BMI")
    st.markdown('</div>', unsafe_allow_html=True)

# --------------------------------------------------
# ABOUT PAGE
# --------------------------------------------------
with selected_tab[4]:
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.header("About the Project")

    st.markdown("""
    This project demonstrates the practical application of machine learning techniques
    in predicting healthcare insurance costs based on demographic and lifestyle attributes.
    It is designed for educational, analytical, and portfolio purposes.
    """)

    st.markdown("### Tech Stack")
    st.markdown("""
    - Python  
    - Pandas and NumPy  
    - Scikit-learn  
    - Streamlit  
    - Joblib  
    """)

    st.markdown("### Dataset")
    st.markdown("""
    Healthcare Insurance Dataset  
    [Access the dataset here](https://healthcare-insurance-j6tw5lybbhumwmlrghpvp6.streamlit.app/#medical-insurance-cost-predictor)
    """)

    st.markdown("### Use Case")
    st.markdown("""
    - Educational demonstrations of machine learning  
    - Financial planning and cost estimation  
    - Healthcare analytics use cases  
    """)
    st.markdown('</div>', unsafe_allow_html=True)
