import streamlit as st
import joblib
model = joblib.load("house_model.pkl")
st.title("House Price Prediction App")
st.write("Enter house details below to predict the price")

#User Input field

size = st.number_input("House Size (sq ft)")
bedrooms = st.number_input("Number of Bedrooms")
age = st.number_input("House Age")

#Prediction Button
if st.button("Predicted Price"):
    prediction = model.predict([[size, bedrooms, age]])
    st.success(f"Estimated House Price: ${prediction[0]:,.2f}")