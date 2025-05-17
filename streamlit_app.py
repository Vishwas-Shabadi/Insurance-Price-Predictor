import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load model and scaler
with open('gb_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

# Streamlit page config
st.set_page_config(page_title="Insurance Premium Predictor", layout="centered")

# Title
st.title("💰 Insurance Premium Predictor")

# Input fields
Age = st.number_input("Age", 18, 100)
Diabetes = st.selectbox("Diabetes", [0, 1])
BloodPressureProblems = st.selectbox("Blood Pressure Problems", [0, 1])
AnyTransplants = st.selectbox("Any Transplants", [0, 1])
AnyChronicDiseases = st.selectbox("Any Chronic Diseases", [0, 1])
Height = st.number_input("Height (in cm)", 100, 220)
Weight = st.number_input("Weight (in kg)", 30, 180)
KnownAllergies = st.selectbox("Known Allergies", [0, 1])
HistoryOfCancerInFamily = st.selectbox("History of Cancer in Family", [0, 1])
NumberOfMajorSurgeries = st.number_input("Number of Major Surgeries", 0, 10)

if st.button("Predict Premium"):
    # Derived / Imputed features
    BMI = Weight / ((Height / 100) ** 2)
    MultipleSurgeries = 1 if NumberOfMajorSurgeries > 2 else 0
    OtherHealthConditions = Diabetes + BloodPressureProblems + KnownAllergies + HistoryOfCancerInFamily

    # Categorical features from rules
    AgeGroup_Senior = 1 if Age >= 50 else 0
    AgeGroup_Young = 1 if Age < 30 else 0
    BMIGroup_Obese = 1 if BMI >= 30 else 0
    BMIGroup_Overweight = 1 if 25 <= BMI < 30 else 0
    BMIGroup_Underweight = 1 if BMI < 18.5 else 0

    # Create DataFrame with the required order
    input_data = pd.DataFrame({
        'Age': [Age],
        'AnyTransplants': [AnyTransplants],
        'AnyChronicDiseases': [AnyChronicDiseases],
        'BMI': [BMI],
        'MultipleSurgeries': [MultipleSurgeries],
        'OtherHealthConditions': [OtherHealthConditions],
        'AgeGroup_Senior': [AgeGroup_Senior],
        'AgeGroup_Young': [AgeGroup_Young],
        'BMIGroup_Obese': [BMIGroup_Obese],
        'BMIGroup_Overweight': [BMIGroup_Overweight],
        'BMIGroup_Underweight': [BMIGroup_Underweight]
    })

    # Scaling
    input_scaled = scaler.transform(input_data)

    # Prediction
    premium = model.predict(input_scaled)[0]

    # Display result
    st.success(f"Estimated Premium Price: ₹{premium:,.2f}")