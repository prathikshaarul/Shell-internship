import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler

# -----------------------
# Load Model and Scaler
# -----------------------
model = pickle.load(open("crop_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# -----------------------
# Streamlit UI
# -----------------------
st.title("🌱 AI-Powered Crop Recommendation System")
st.write("Enter soil and climate parameters to get the best crop suggestion")

# User inputs
N = st.number_input("Nitrogen (N)", min_value=0, max_value=200, value=50)
P = st.number_input("Phosphorus (P)", min_value=0, max_value=200, value=50)
K = st.number_input("Potassium (K)", min_value=0, max_value=200, value=50)
temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=50.0, value=25.0)
humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=60.0)
ph = st.number_input("pH", min_value=0.0, max_value=14.0, value=6.5)
rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=300.0, value=100.0)

# Predict button
if st.button("Recommend Crop"):
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    scaled_data = scaler.transform(input_data)
    prediction = model.predict(scaled_data)
    st.success(f"🌾 The best crop to grow is: **{prediction[0].capitalize()}**")
import pickle

model = pickle.load(open("crop_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
