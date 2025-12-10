import streamlit as st
import requests
import pygame
 
# -----------------------------------------------------------
# ULTRA-MODERN FUTURISTIC CSS
# -----------------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;500;700&display=swap');

/* -----------------------------------------------------------
   ANIMATED GRADIENT BACKGROUND WITH PARTICLES
----------------------------------------------------------- */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(-45deg, #0a0e27, #1a1a2e, #16213e, #0f3460);
    background-size: 400% 400%;
    animation: gradientFlow 15s ease infinite;
    position: relative;
    overflow: hidden;
}

@keyframes gradientFlow {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Animated particles overlay */
[data-testid="stAppViewContainer"]::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-image: 
        radial-gradient(circle at 20% 30%, rgba(0, 234, 255, 0.1) 0%, transparent 50%),
        radial-gradient(circle at 80% 70%, rgba(138, 43, 226, 0.1) 0%, transparent 50%),
        radial-gradient(circle at 40% 80%, rgba(255, 0, 128, 0.1) 0%, transparent 50%);
    animation: particleFloat 20s ease-in-out infinite;
    pointer-events: none;
    z-index: 1;
}

@keyframes particleFloat {
    0%, 100% { transform: translate(0, 0) scale(1); }
    33% { transform: translate(30px, -30px) scale(1.1); }
    66% { transform: translate(-20px, 20px) scale(0.9); }
}

/* Floating geometric shapes */
[data-testid="stAppViewContainer"]::after {
    content: "";
    position: fixed;
    top: -50%;
    left: -50%;
    right: -50%;
    bottom: -50%;
    background: 
        repeating-linear-gradient(90deg, transparent 0px, rgba(0, 234, 255, 0.03) 1px, transparent 2px, transparent 80px),
        repeating-linear-gradient(0deg, transparent 0px, rgba(138, 43, 226, 0.03) 1px, transparent 2px, transparent 80px);
    animation: gridMove 30s linear infinite;
    pointer-events: none;
    z-index: 1;
}

@keyframes gridMove {
    0% { transform: translate(0, 0); }
    100% { transform: translate(80px, 80px); }
}

/* Main content wrapper */
.block-container {
    position: relative;
    z-index: 2;
    padding-top: 3rem !important;
}

/* -----------------------------------------------------------
   GLASSMORPHIC TITLE WITH NEON GLOW
----------------------------------------------------------- */
.title-container {
    background: rgba(255, 255, 255, 0.03);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 30px;
    padding: 30px;
    margin-bottom: 40px;
    box-shadow: 
        0 8px 32px rgba(0, 0, 0, 0.3),
        inset 0 1px 0 rgba(255, 255, 255, 0.1),
        0 0 60px rgba(0, 234, 255, 0.2);
    animation: titlePulse 4s ease-in-out infinite;
}

@keyframes titlePulse {
    0%, 100% { box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3), inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 0 60px rgba(0, 234, 255, 0.2); }
    50% { box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3), inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 0 100px rgba(138, 43, 226, 0.4); }
}

.title {
    font-family: 'Orbitron', sans-serif;
    font-size: 56px;
    font-weight: 900;
    text-align: center;
    background: linear-gradient(135deg, #00eaff 0%, #8a2be2 50%, #ff0080 100%);
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: gradientShift 3s linear infinite;
    letter-spacing: 4px;
    margin: 0;
    text-transform: uppercase;
    position: relative;
}

@keyframes gradientShift {
    0% { background-position: 0% center; }
    100% { background-position: 200% center; }
}

.title::before {
    content: attr(data-text);
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(135deg, #00eaff 0%, #8a2be2 50%, #ff0080 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    filter: blur(15px);
    opacity: 0.5;
    animation: gradientShift 3s linear infinite;
}

/* -----------------------------------------------------------
   MODERN INPUT FIELDS
----------------------------------------------------------- */
.stNumberInput > div > div > input {
    background: rgba(0, 0, 0, 0.3) !important;
    backdrop-filter: blur(10px);
    border: 2px solid rgba(0, 234, 255, 0.3) !important;
    border-radius: 15px !important;
    color: #00eaff !important;
    font-family: 'Rajdhani', sans-serif;
    font-size: 24px !important;
    font-weight: 700 !important;
    padding: 15px 20px !important;
    transition: all 0.3s ease;
    box-shadow: inset 0 2px 10px rgba(0, 0, 0, 0.3);
}

.stNumberInput > div > div > input:focus {
    border-color: #00eaff !important;
    box-shadow: 
        inset 0 2px 10px rgba(0, 0, 0, 0.3),
        0 0 30px rgba(0, 234, 255, 0.5) !important;
    transform: scale(1.02);
}

.stNumberInput label {
    color: #00eaff !important;
    font-family: 'Rajdhani', sans-serif !important;
    font-size: 18px !important;
    font-weight: 600 !important;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 10px !important;
}

/* -----------------------------------------------------------
   MODERN SELECTBOX
----------------------------------------------------------- */
.stSelectbox > div > div {
    background: rgba(0, 0, 0, 0.3) !important;
    backdrop-filter: blur(10px);
    border: 2px solid rgba(138, 43, 226, 0.3) !important;
    border-radius: 15px !important;
    transition: all 0.3s ease;
}

.stSelectbox > div > div:hover {
    border-color: rgba(138, 43, 226, 0.6) !important;
    box-shadow: 0 0 30px rgba(138, 43, 226, 0.3);
}

.stSelectbox label {
    color: #8a2be2 !important;
    font-family: 'Rajdhani', sans-serif !important;
    font-size: 18px !important;
    font-weight: 600 !important;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 10px !important;
}

.stSelectbox [data-baseweb="select"] > div {
    color: #8a2be2 !important;
    font-family: 'Rajdhani', sans-serif !important;
    font-size: 22px !important;
    font-weight: 700 !important;
}

/* -----------------------------------------------------------
   3D HOLOGRAM BUTTON
----------------------------------------------------------- */
.stButton {
    display: flex;
    justify-content: center;
    margin: 30px 0;
}

.stButton > button {
    background: linear-gradient(135deg, #00eaff 0%, #8a2be2 50%, #ff0080 100%);
    background-size: 200% auto;
    padding: 20px 60px;
    border-radius: 50px;
    border: none;
    color: white;
    font-size: 26px;
    font-weight: 900;
    font-family: 'Orbitron', sans-serif;
    letter-spacing: 3px;
    text-transform: uppercase;
    box-shadow: 
        0 10px 30px rgba(0, 0, 0, 0.5),
        0 0 60px rgba(0, 234, 255, 0.4),
        inset 0 1px 0 rgba(255, 255, 255, 0.3);
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    cursor: pointer;
    position: relative;
    overflow: hidden;
}

.stButton > button::before {
    content: "";
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
    transition: left 0.5s;
}

.stButton > button:hover::before {
    left: 100%;
}

.stButton > button:hover {
    transform: translateY(-5px) scale(1.05);
    box-shadow: 
        0 15px 40px rgba(0, 0, 0, 0.6),
        0 0 80px rgba(138, 43, 226, 0.6),
        inset 0 1px 0 rgba(255, 255, 255, 0.4);
    background-position: 100% center;
}

.stButton > button:active {
    transform: translateY(-2px) scale(1.02);
    box-shadow: 
        0 5px 20px rgba(0, 0, 0, 0.4),
        0 0 40px rgba(0, 234, 255, 0.4);
}

/* -----------------------------------------------------------
   HOLOGRAM RESULT BOX
----------------------------------------------------------- */
.result {
    margin-top: 0.5px;
    padding: 35px;
    border-radius: 25px;
    text-align: center;
    font-size: 32px;
    font-family: 'Orbitron', sans-serif;
    font-weight: 900;
    background: rgba(0, 234, 255, 0.05);
    backdrop-filter: blur(20px);
    border: 2px solid rgba(0, 234, 255, 0.4);
    box-shadow: 
        0 8px 32px rgba(0, 0, 0, 0.4),
        0 0 60px rgba(0, 234, 255, 0.3),
        inset 0 1px 0 rgba(255, 255, 255, 0.2);
    animation: resultGlow 2s ease-in-out infinite alternate;
    position: relative;
    overflow: hidden;
}

.result::before {
    content: "";
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: linear-gradient(45deg, transparent 30%, rgba(0, 234, 255, 0.1) 50%, transparent 70%);
    animation: shimmer 3s linear infinite;
}

@keyframes shimmer {
    0% { transform: translateX(-100%) translateY(-100%) rotate(45deg); }
    100% { transform: translateX(100%) translateY(100%) rotate(45deg); }
}

@keyframes resultGlow {
    0% { 
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4), 0 0 40px rgba(0, 234, 255, 0.3), inset 0 1px 0 rgba(255, 255, 255, 0.2);
    }
    100% { 
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4), 0 0 80px rgba(0, 234, 255, 0.6), inset 0 1px 0 rgba(255, 255, 255, 0.3);
    }
}

.result-text {
    position: relative;
    z-index: 1;
    background: linear-gradient(135deg, #00eaff 0%, #8a2be2 50%, #ff0080 100%);
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: gradientShift 3s linear infinite;
}

/* -----------------------------------------------------------
   ERROR MESSAGE STYLING
----------------------------------------------------------- */
.stAlert {
    background: rgba(255, 0, 80, 0.1) !important;
    backdrop-filter: blur(20px);
    border: 2px solid rgba(255, 0, 80, 0.5) !important;
    border-radius: 20px !important;
    color: #ff0080 !important;
    font-family: 'Rajdhani', sans-serif !important;
    font-size: 20px !important;
    font-weight: 700 !important;
    padding: 20px !important;
    box-shadow: 0 8px 32px rgba(255, 0, 80, 0.3);
}

/* -----------------------------------------------------------
   HIDE STREAMLIT BRANDING
----------------------------------------------------------- */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------
# TITLE WITH GLASSMORPHIC CONTAINER
# -----------------------------------------------------------
st.markdown("""
<div class="title-container">
    <h1 class="title" data-text="◈ SIMPLE CALCULATOR ◈">SIMPLE CALCULATOR</h1>
</div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------
# CALCULATOR PANEL
# -----------------------------------------------------------


col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("⚡ Enter first number", value=0.0, key="num1")

with col2:
    num2 = st.number_input("⚡ Enter second number", value=0.0, key="num2")

operation = st.selectbox(
    "🎯 Choose Operation",
    ("Add ➕", "Subtract ➖", "Multiply ✖️", "Divide ➗")
)

compute = st.button("COMPUTE")

st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------------------------------------
# CALC LOGIC
# -----------------------------------------------------------
if compute:
    if operation.startswith("Add"):
        result = num1 + num2
        text = f"{num1} + {num2} = {result}"

    elif operation.startswith("Subtract"):
        result = num1 - num2
        text = f"{num1} - {num2} = {result}"

    elif operation.startswith("Multiply"):
        result = num1 * num2
        text = f"{num1} × {num2} = {result}"

    elif operation.startswith("Divide"):
        if num2 == 0:
            st.error("⌛ ERROR: Cannot divide by zero!")
            st.stop()
        result = num1 / num2
        text = f"{num1} ÷ {num2} = {result}"

    st.markdown(f'<div class="result"><span class="result-text">RESULT: {text}</span></div>', unsafe_allow_html=True)
