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
# CUSTOM CSS FOR THEME, NAVIGATION & LAYOUT
# --------------------------------------------------
st.markdown("""
<style>
/* Whole page background */
body {
    background-color: #ffe6f0; /* soft pink background */
    color: #333333;
}

/* Page container padding */
.block-container {
    max-width: 1000px;
    padding-top: 1rem; /* reduced top padding */
    padding-bottom: 1rem;
}

/* Headings without colored background */
h1, h2, h3 {
    background-color: #ffffff !important;
    box-shadow: none !important;
    padding: 0.2rem 0 !important;
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
    background-color: #ffe6f0;
    color: #333333;
    border-radius: 8px;
    padding: 1rem;
}

/* Right align tabs */
.css-1v3fvcr.e16nr0p31 { 
    justify-content: flex-end;
    margin-bottom: 0.5rem;
}

/* Reduce gap between navigation tabs and content */
.css-12w0qpk { 
    padding-top: 0.5rem; 
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# TOP NAVIGATION TABS
# --------------------------------------------------
tabs = ["Home", "Cost Estimator", "How It Works", "Insights & Factors", "About the Project"]
selected_tab = st.tabs(tabs)

# --------------------------------------------------
# HOME PAGE
# --------------------------------------------------
with selected_tab[0]:
    st.markdown('<div class="section">', unsafe_allow_html=True)

    st.markdown("<h1>InsureSense</h1>", unsafe_allow_html=True)
    st.markdown("<h3>Medical Insurance Cost Estimation using Machine Learning</h3>", unsafe_allow_html=True)

    st.markdown("""
    Planning healthcare expenses can be confusing. Insurance costs depend on age, lifestyle, health metrics, and location.
    Many individuals either overestimate or underestimate their insurance expenses due to lack of clear guidance.

    InsureSense uses a trained machine learning model to predict your annual insurance cost
    based on your personal, health, and lifestyle data. This helps you make informed decisions and plan finances efficiently.
    """)

    st.markdown("## Why This Matters")
    st.markdown("""
    - Healthcare costs are continuously rising globally.  
    - Lifestyle choices like smoking and body mass index heavily influence insurance pricing.  
    - Data-driven cost estimates allow better financial and health planning.  
    """)

    st.markdown("### Get Started")
    if st.button("Estimate Your Insurance Cost"):
        st.experimental_rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --------------------------------------------------
# COST ESTIMATOR PAGE
# --------------------------------------------------
with selected_tab[1]:
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.header("Medical Insurance Cost Estimator")
    st.markdown("""
    Enter your personal, health, and lifestyle details below. The system will generate an estimated annual insurance cost.
    """)

    st.markdown("### Your Details")
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
    The model is trained on a healthcare insurance dataset including demographic, lifestyle, and regional information with historical charges.

    **Step 2: Feature Processing**  
    Categorical features like gender, smoking status, and region are encoded. BMI is calculated from height and weight.

    **Step 3: Model Training**  
    A supervised regression model learns patterns from historical insurance data.

    **Step 4: Prediction**  
    User inputs are passed to the trained model to generate an estimated insurance cost.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# --------------------------------------------------
# INSIGHTS & FACTORS PAGE
# --------------------------------------------------
with selected_tab[3]:
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.header("Key Factors Affecting Insurance Cost")

    st.markdown("""
    Understanding the factors influencing insurance cost helps users interpret
    the estimated values more effectively.

    - **Age:** Costs increase with age due to higher health risks.  
    - **Smoking Status:** Smokers typically face higher charges.  
    - **Body Mass Index (BMI):** Higher BMI increases healthcare risk.  
    - **Number of Dependents:** More dependents increase total coverage cost.  
    - **Geographic Region:** Insurance pricing varies by region.  
    """)

    st.markdown("**Most influential factors:** Smoking and BMI")
    st.markdown('</div>', unsafe_allow_html=True)

# --------------------------------------------------
# ABOUT PAGE
# --------------------------------------------------
with selected_tab[4]:
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.header("About the Project")

    st.markdown("""
    InsureSense demonstrates practical application of machine learning for
    predicting healthcare insurance costs based on demographics and lifestyle.
    This app is designed for educational, analytical, and portfolio purposes.
    """)

    st.markdown("### Tech Stack")
    st.markdown("""
    - Python  
    - Pandas & NumPy  
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
    - Educational demonstrations of ML applications  
    - Financial planning and cost estimation  
    - Healthcare analytics and insights  
    """)
    st.markdown('</div>', unsafe_allow_html=True)
