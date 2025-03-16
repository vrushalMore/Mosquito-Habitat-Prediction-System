import streamlit as st
import joblib
import numpy as np

model = joblib.load("deployment/random_forest.pkl")

mapping = {
    "Low": {"daily_avg_temp": 22.53, "total_precipitation": 25.08, "relative_humidity": 52.70, "population_density": 2565.32, "day_length": 11.00},
    "Medium": {"daily_avg_temp": 27.41, "total_precipitation": 50.14, "relative_humidity": 65.38, "population_density": 5030.63, "day_length": 11.99},
    "High": {"daily_avg_temp": 32.31, "total_precipitation": 75.06, "relative_humidity": 77.69, "population_density": 7514.82, "day_length": 12.99},
    "Yes": 1,
    "No": 0,
    "Urban": 1,
    "Rural": 0
}

st.set_page_config(page_title="Disease Prediction Chatbot", page_icon="⚠️", layout="centered")
st.title("Disease Outbreak Risk Assessment Chatbot")
st.write("This chatbot will help you assess the risk of disease outbreaks in a locality based on various environmental factors.")
st.markdown("---")

st.markdown(
    """
    <style>
        body { background-color: white; color: black; font-family: Arial; }
        div.stButton > button:first-child { background-color: #87CEEB; color: black; border-radius: 5px; }
    </style>
    """,
    unsafe_allow_html=True
)

questions = [
    "What is the daily average temperature?",
    "How much total precipitation is there?",
    "What is the relative humidity level?",
    "Are there any water bodies in the area?",
    "What is the population density?",
    "How long is the day?",
    "Is the area urban or rural?",
    "Is the area forested?",
    "Is there a crop-growing area?",
    "Is there a grazing land area?"
]

options = [
    ["Low", "Medium", "High"],
    ["Low", "Medium", "High"],
    ["Low", "Medium", "High"],
    ["Yes", "No"],
    ["Low", "Medium", "High"],
    ["Low", "Medium", "High"],
    ["Urban", "Rural"],
    ["Yes", "No"],
    ["Yes", "No"],
    ["Yes", "No"]
]

if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.answers = []

if st.session_state.step < len(questions):
    answer = st.selectbox(questions[st.session_state.step], options[st.session_state.step])
    if st.button("Next", key=f"next_{st.session_state.step}"):
        st.session_state.answers.append(answer)
        st.session_state.step += 1
        st.rerun()
else:
    input_features = np.array([
        22.53, 
        32.31, 
        mapping[st.session_state.answers[0]]["daily_avg_temp"],
        mapping[st.session_state.answers[1]]["total_precipitation"],
        mapping[st.session_state.answers[2]]["relative_humidity"],
        mapping[st.session_state.answers[3]],
        mapping[st.session_state.answers[4]]["population_density"],
        mapping[st.session_state.answers[5]]["day_length"],
        mapping[st.session_state.answers[6]],
        mapping[st.session_state.answers[7]],
        mapping[st.session_state.answers[8]],
        mapping[st.session_state.answers[9]]
    ]).reshape(1, -1)
    
    prediction = model.predict(input_features)[0]
    
    if prediction == 1:
        st.error("🚨Warning! This locality is at risk of disease outbreaks.")
    else:
        st.success("✅ This locality is safe from disease outbreaks.")
    
    if st.button("Restart"):
        st.session_state.step = 0
        st.session_state.answers = []
        st.rerun()
