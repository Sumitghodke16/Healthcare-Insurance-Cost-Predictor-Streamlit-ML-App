import streamlit as st
import pandas as pd
import joblib

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Medical Insurance Cost Predictor",
    page_icon="🏥",
    layout="wide"
)

# ==================================================
# LOAD MODEL
# ==================================================

model = joblib.load("medical_insurance_model.pkl")

# ==================================================
# CSS
# ==================================================
st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Background */

.stApp{
    background:#FFA896;
}

/* Title */

.main-title{
    text-align:center;
    font-size:58px;
    font-weight:900;
    color:#38000A;
}

.sub-title{
    text-align:center;
    font-size:22px;
    color:#38000A;
    margin-bottom:30px;
}

/* Section Titles */

.section-title{
    color:#9B1313;
    font-size:34px;
    font-weight:800;
    margin-bottom:15px;
}

/* Input Cards */

[data-testid="stNumberInput"]{
    background:#FFE8E2;
    border-radius:18px;
    padding:8px;
    border:2px solid #CD1C18;
}

[data-testid="stSelectbox"]{
    background:#FFE8E2;
    border-radius:18px;
    padding:8px;
    border:2px solid #CD1C18;
}

/* Labels */

label{
    font-size:18px !important;
    font-weight:700 !important;
    color:#9B1313 !important;
}

/* Number Input Text */

input{
    font-size:18px !important;
    font-weight:700 !important;
    color:#38000A !important;
}

/* Select Box */

div[data-baseweb="select"] > div{
    background:#FFE8E2 !important;
    border-radius:12px !important;
    border:2px solid #CD1C18 !important;
    min-height:55px !important;
    color:#38000A !important;
    font-size:18px !important;
}

/* Dropdown Menu */

div[role="listbox"]{
    background:#FFE8E2 !important;
}

div[role="option"]{
    background:#FFE8E2 !important;
    color:#38000A !important;
    font-size:18px !important;
}

div[role="option"]:hover{
    background:#FFA896 !important;
}

/* Button */

.stButton > button{
    width:100%;
    height:75px;
    background:#CD1C18;
    color:white;
    font-size:24px;
    font-weight:800;
    border:none;
    border-radius:18px;
}

.stButton > button:hover{
    background:#38000A;
    color:white;
}

/* Prediction Card */

.prediction-card{
    background:linear-gradient(
        135deg,
        #9B1313,
        #38000A
    );

    border-radius:25px;
    padding:35px;
    min-height:320px;
    text-align:center;
    color:white;
    box-shadow:0px 10px 25px rgba(0,0,0,0.20);
}

/* Info Card */

.info-card{
    background:#FFE8E2;
    border-radius:20px;
    padding:25px;
    margin-top:25px;
    border-left:8px solid #CD1C18;
    box-shadow:0px 4px 15px rgba(0,0,0,0.10);
}

/* Footer */

.footer{
    text-align:center;
    color:#38000A;
    font-size:24px;
    font-weight:800;
    padding:30px;
}

</style>
""", unsafe_allow_html=True)


# ==================================================
# HEADER
# ==================================================

st.markdown("""
<div class='main-title'>
🏥 Medical Insurance Cost Predictor
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='sub-title'>
Predict Healthcare Insurance Charges Using Machine Learning
</div>
""", unsafe_allow_html=True)

st.write("")

# ==================================================
# 3 COLUMNS
# ==================================================

left_col, middle_col, right_col = st.columns([1,1,0.85])

# ==================================================
# LEFT
# ==================================================

with left_col:

    st.markdown(
        "<div class='section-title'>👤 Personal Information</div>",
        unsafe_allow_html=True
    )

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=30
    )

    bmi = st.number_input(
        "BMI",
        min_value=10.0,
        max_value=60.0,
        value=25.0
    )

    children = st.number_input(
        "Children",
        min_value=0,
        max_value=10,
        value=1
    )

# ==================================================
# MIDDLE
# ==================================================

with middle_col:

    st.markdown(
        "<div class='section-title'>🩺 Health Information</div>",
        unsafe_allow_html=True
    )

    sex = st.selectbox(
        "Gender",
        ["male","female"]
    )

    smoker = st.selectbox(
        "Smoker",
        ["yes","no"]
    )

    region = st.selectbox(
        "Region",
        [
            "northeast",
            "northwest",
            "southeast",
            "southwest"
        ]
    )

# ==================================================
# RIGHT
# ==================================================

with right_col:

    st.markdown(
        "<div class='section-title'>💰 Prediction</div>",
        unsafe_allow_html=True
    )

    predict_btn = st.button(
        "🚀 Predict Insurance Cost",
        use_container_width=True
    )

    if predict_btn:

        sex_male = 1 if sex == "male" else 0

        smoker_yes = 1 if smoker == "yes" else 0

        region_northwest = 1 if region == "northwest" else 0
        region_southeast = 1 if region == "southeast" else 0
        region_southwest = 1 if region == "southwest" else 0

        input_df = pd.DataFrame({

            "age":[age],
            "bmi":[bmi],
            "children":[children],

            "sex_male":[sex_male],

            "smoker_yes":[smoker_yes],

            "region_northwest":[region_northwest],
            "region_southeast":[region_southeast],
            "region_southwest":[region_southwest]

        })

        prediction = model.predict(input_df)[0]

        st.markdown(
        f"""
        <div class='prediction-card'>

        <h2>💰 Predicted Charge</h2>

        <h1 style="
        font-size:60px;
        font-weight:900;
        margin-top:40px;
        ">
        ${prediction:,.2f}
        </h1>

        </div>
        """,
        unsafe_allow_html=True
        )

# ==================================================
# INFO SECTION
# ==================================================

st.markdown("""
<div class='info-card'>

<h2 style="color:#38000A;">
📌 Key Factors Affecting Insurance Cost
</h2>

<ul style="
font-size:20px;
color:#38000A;
line-height:2;
">

<li>Smoking Status</li>
<li>Age</li>
<li>BMI</li>
<li>Number of Children</li>
<li>Region</li>

</ul>

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='footer'>
Built by Sumit Naresh Ghodke 🚀
</div>
""", unsafe_allow_html=True)