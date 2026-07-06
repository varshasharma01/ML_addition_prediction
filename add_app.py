import streamlit as st
import pickle
import numpy as np
from my_lr import MyLR

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="ML Addition Predictor",
    page_icon="☁️",
    layout="wide"
)

# ---------------- LOAD CSS ---------------- #

with open("style.css") as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)

# ---------------- LOAD MODEL ---------------- #

with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# ---------------- TITLE ---------------- #

st.markdown(
    """
    <h1 class="title">
        ☁️ ML Addition Predictor ☁️
    </h1>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <p class="subtitle">
        Enter three numbers and let the ML model predict their sum.
    </p>
    """,
    unsafe_allow_html=True,
)

st.write("")

# ---------------- INPUTS ---------------- #

col1, col2, col3, col4, col5 = st.columns([4, 0.7, 4, 0.7, 4])

with col1:
    st.markdown("<div class='cloud-title'>☁️ Number 1</div>", unsafe_allow_html=True)
    num1 = st.number_input("Number 1", key="n1", value=0.0, )

with col2:
    st.markdown("<div class='plus'>+</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='cloud-title'>☁️ Number 2</div>", unsafe_allow_html=True)
    num2 = st.number_input("Number 2", key="n2", value=0.0, )

with col4:
    st.markdown("<div class='plus'>+</div>", unsafe_allow_html=True)

with col5:
    st.markdown("<div class='cloud-title'>☁️ Number 3</div>", unsafe_allow_html=True)
    num3 = st.number_input("Number 3", key="n3", value=0.0, )

st.write("")
st.write("")

# ---------------- BUTTON ---------------- #

predict = st.button("✨ Predict Sum")

if predict:

    prediction = model.predict(np.array([[num1, num2, num3]]))[0]

    actual = num1 + num2 + num3

    error = abs(actual - prediction)

    st.write("")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
            f"""
            <div class="result-card">
                <h3>🤖 Prediction</h3>
                <h2>{prediction:.2f}</h2>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c2:
        st.markdown(
            f"""
            <div class="result-card">
                <h3>✅ Actual Sum</h3>
                <h2>{actual:.2f}</h2>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c3:
        st.markdown(
            f"""
            <div class="result-card">
                <h3>🎯 Error</h3>
                <h2>{error:.6f}</h2>
            </div>
            """,
            unsafe_allow_html=True,
        )