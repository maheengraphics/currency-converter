pip install streamlit requests
import streamlit as st
import requests

# Function to fetch conversion rate and perform conversion
def convert_currency(amount, from_currency, to_currency):
    if from_currency == to_currency:
        return f"{amount:.2f} {to_currency}"

    try:
        response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{from_currency}")
        response.raise_for_status()
        data = response.json()

        if to_currency in data['rates']:
            conversion_rate = data['rates'][to_currency]
            converted_amount = amount * conversion_rate
            return f"{converted_amount:.2f} {to_currency}"
        else:
            return f"Currency {to_currency} not available"
    except requests.exceptions.RequestException as e:
        return f"Error fetching conversion rates: {e}"

# Streamlit App
st.title("Currency Converter")

# User input
amount = st.number_input("Amount", min_value=0.0, step=0.01)
from_currency = st.selectbox("From Currency", ["USD", "EUR", "GBP", "JPY", "INR", "CAD", "AUD", "PKR"], index=0)
to_currency = st.selectbox("To Currency", ["USD", "EUR", "GBP", "JPY", "INR", "CAD", "AUD", "PKR"], index=1)

# Convert button
if st.button("Convert"):
    if amount > 0:
        result = convert_currency(amount, from_currency, to_currency)
        st.success(result)
    else:
        st.error("Please enter a valid amount")

