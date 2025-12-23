import streamlit as st
import pandas as pd
import joblib

# PAGE CONFIG
st.set_page_config(
    page_title="InsureSense | Insurance Cost Estimator",
    layout="wide"
)

# LOAD MODEL
model = joblib.load("model.joblib")

# CUSTOM CSS
st.markdown("""
<style>
/* Full page background */
body, .main, .block-container {
    background-color: #ffd6e8; /* soft light pink */
    color: #333333; 
}

/* Sidebar color */
[aria-label="Sidebar"] {
    background-color: #ffb3d1;
}

/* Section cards */
.section {
    background-color: #ffffff;
    padding: 2rem;
    border-radius: 12px;
    margin-bottom: 2rem;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.08);
}

/* Headings - remove default Streamlit box */
.custom-h1 {
    text-align: center;
    color: #c2185b;
    font-size: 3rem;
    font-weight: 700;
    margin: 1rem 0 0.5rem 0;
    background: none !important;
}

.custom-h2 {
    color: #c2185b;
    font-size: 2rem;
    font-weight: 600;
    margin: 1rem 0 0.5rem 0;
    background: none !important;
}

.custom-h3 {
    color: #c2185b;
    font-size: 1.5rem;
    font-weight: 500;
    margin: 0.8rem 0 0.5rem 0;
    background: none !important;
}

/* Buttons */
.stButton>button {
    background-color: #ff66b2;
    color: white;
    font-size: 16px;
    padding: 0.7rem 1.5rem;
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
</style>
""", unsafe_allow_html=True)

# SESSION STATE
if "page" not in st.session_state:
    st.session_state.page = "Home"

# SIDEBAR NAVIGATION
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

# ----------------- HOME PAGE -----------------
if page == "Home":
    st.markdown('<div class="section">', unsafe_allow_html=True)

    st.markdown('<h1 class="custom-h1">InsureSense</h1>', unsafe_allow_html=True)
    st.markdown('<h3 class="custom-h3">Medical Insurance Cost Estimation using Machine Learning</h3>', unsafe_allow_html=True)

    st.markdown("""
    Healthcare insurance costs are influenced by a combination of personal characteristics,
    health metrics, and lifestyle habits. Accurately estimating these costs can be challenging
    for individuals planning their healthcare expenses.

    InsureSense uses a machine learning model trained on real-world healthcare insurance data
    to provide an estimated annual insurance cost based on user-provided inputs.
    """)

    st.markdown('<h2 class="custom-h2">Why this matters</h2>', unsafe_allow_html=True)
    st.markdown("""
    - Healthcare costs continue to rise globally  
    - Lifestyle choices such as smoking and body mass index strongly influence insurance pricing  
    - Data-driven cost estimates support informed financial and healthcare planning  
    """)

    st.markdown('<h3 class="custom-h3">Get Started</h3>', unsafe_allow_html=True)
    if st.button("Estimate Your Insurance Cost"):
        st.session_state.page = "Cost Estimator"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# ----------------- COST ESTIMATOR PAGE -----------------
elif page == "Cost Estimator":
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown('<h2 class="custom-h2">Medical Insurance Cost Estimator</h2>', unsafe_allow_html=True)
    st.markdown("""
    Enter your personal, health, and lifestyle details below. The system will process
    this information and generate an estimated annual insurance cost.
    """)

    st.markdown('<h3 class="custom-h3">User Information</h3>', unsafe_allow_html=True)
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

    region = st.selectbox("Residential Region", ["northeast", "northwest", "southeast", "southwest"])

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

    st.markdown('<h3 class="custom-h3">Generate Estimate</h3>', unsafe_allow_html=True)
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

# ----------------- HOW IT WORKS PAGE -----------------
elif page == "How It Works":
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown('<h2 class="custom-h2">How the System Works</h2>', unsafe_allow_html=True)
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

# ----------------- INSIGHTS PAGE -----------------
elif page == "Insights & Factors":
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown('<h2 class="custom-h2">Key Factors Affecting Insurance Cost</h2>', unsafe_allow_html=True)
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

# ----------------- ABOUT PAGE -----------------
elif page == "About the Project":
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown('<h2 class="custom-h2">About the Project</h2>', unsafe_allow_html=True)
    st.markdown("""
    This project demonstrates the practical application of machine learning techniques
    in predicting healthcare insurance costs based on demographic and lifestyle attributes.
    It is designed for educational, analytical, and portfolio purposes.
    """)
    st.markdown('<h3 class="custom-h3">Tech Stack</h3>', unsafe_allow_html=True)
    st.markdown("""
    - Python  
    - Pandas and NumPy  
    - Scikit-learn  
    - Streamlit  
    - Joblib  
    """)
    st.markdown('<h3 class="custom-h3">Dataset</h3>', unsafe_allow_html=True)
    st.markdown("""
    Healthcare Insurance Dataset  
    [Access the dataset here](https://healthcare-insurance-j6tw5lybbhumwmlrghpvp6.streamlit.app/#medical-insurance-cost-predictor)
    """)
    st.markdown('<h3 class="custom-h3">Use Case</h3>', unsafe_allow_html=True)
    st.markdown("""
    - Educational demonstrations of machine learning  
    - Financial planning and cost estimation  
    - Healthcare analytics use cases  
    """)
    st.markdown('</div>', unsafe_allow_html=True)
