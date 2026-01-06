import streamlit as st
import joblib
import numpy as np

model = joblib.load("wheat_seed_model.pkl")

st.title("Wheat Seed Type Prediction")

st.write("Enter the features of the seed to predict its type.")

area = st.number_input("area ")
perimeter = st.number_input("perimter ")
compactness = st.number_input("compactness ")
kernel_length = st.number_input("kernel_length ")
kernel_width = st.number_input("kernel_width")
asymmetry_coeff = st.number_input("asymmetry_coeff ")
kernel_groove_length = st.number_input("kernel_groove_length ")

st.write("Enter the features of the seed to predict its type.")

if st.button("Predict"):
    input_data = np.array([[area, perimeter, compactness, kernel_length,kernel_width,asymmetry_coeff,kernel_groove_length]])  # reshape as 2D array
    prediction = model.predict(input_data)
    st.success(f"The predicted seed type is: {prediction[0]}")