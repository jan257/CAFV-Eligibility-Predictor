import streamlit as st
import pandas as pd
import joblib

# Load the trained pipeline
model = joblib.load("model/cafv_eligibility_model.pkl")

# Title
st.set_page_config(page_title="CAFV Eligibility Predictor", layout="centered")
st.title("🚗 Clean Alternative Fuel Vehicle (CAFV) Eligibility Predictor")
st.caption("Powered by a Machine Learning model trained on US electric vehicle data")


st.markdown("---")

# User Input Form
with st.form("prediction_form"):
    st.subheader("Enter Vehicle Details:")

    age = st.number_input("Vehicle Age", min_value=0, max_value=30, value=4)
    electric_range = st.number_input("Electric Range (miles)", min_value=0, value=150)
    msrp = st.number_input("Base MSRP ($)", min_value=0, value=37000)

    make = st.selectbox("Make", options=["TESLA", "NISSAN", "CHEVROLET", "TOYOTA", "KIA", "FORD", "BMW", "VOLKSWAGEN", "VOLVO", "AUDI", "Other"])
    model_name = st.text_input("Model", value="MODEL 3")

    price_category = st.selectbox("Price Category", options=["Low", "Mid", "High", "Luxury", "Unknown"])
    ev_type = st.selectbox("Electric Vehicle Type", options=["BEV", "PHEV"])

    submit = st.form_submit_button("Predict Eligibility")

# Predict
if submit:
    # Prepare input as a DataFrame
    input_dict = {
        "Vehicle Age": age,
        "Electric Range": electric_range,
        "Base MSRP": msrp,
        "Make_Top10": make,
        "Model": model_name,
        "Price Category": price_category,
        "Electric Vehicle Type": ev_type
    }

    input_df = pd.DataFrame([input_dict])
    prediction = model.predict(input_df)[0]
    label = "✅ Eligible" if prediction == 1 else "❌ Not Eligible"

    st.markdown("### Result:")
    st.success(f"The vehicle is **{label}** for CAFV incentives.")

    st.markdown("---")
    st.json(input_dict)



