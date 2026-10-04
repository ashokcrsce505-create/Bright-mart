import streamlit as st
import joblib
import pandas as pd

# Load the saved linear regression model
model = joblib.load('linear.sav')

# App title and description
st.title("Advertising Sales Predictor")
st.write("Enter the advertising budgets below to predict the estimated Sales.")

# Create input fields for features
tv = st.number_input("TV Advertising Budget ($)", min_value=0.0, value=100.0, step=1.0)
radio = st.number_input("Radio Advertising Budget ($)", min_value=0.0, value=20.0, step=1.0)
newspaper = st.number_input("Newspaper Advertising Budget ($)", min_value=0.0, value=10.0, step=1.0)

# Predict button
if st.button("Predict Sales"):
    # Create a DataFrame matching the model's feature structure to avoid name warnings
    input_data = pd.DataFrame([[tv, radio, newspaper]], columns=['TV', 'Radio', 'Newspaper'])
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Sales: {prediction:.2f} units")
