import streamlit as st
from frankfurter import get_currencies_list, get_latest_rates, get_historical_rate
from currency import reverse_rate, round_rate, format_output
import datetime

# Display Streamlit App Title
st.title("VR Currency Converter")

# Get the list of available currencies from Frankfurter
currencies = get_currencies_list()

if not currencies:
    st.error("Error fetching available currencies. Please try again later.")
else:
    amount = st.number_input("Enter the amount to be converted", min_value=1.0)
    from_currency = st.selectbox("From Currency", currencies)
    to_currency = st.selectbox("To Currency", currencies)
    if st.button("Get Latest Rate"):
        date, rate = get_latest_rates(from_currency, to_currency, amount)
        if date and rate:
            st.text(format_output(date, from_currency, to_currency, rate, amount))
    
    selected_date = st.date_input("Select a date for historical rates", datetime.date.today())
    if st.button("Get Historical Rate"):
        rate = get_historical_rate(from_currency, to_currency, selected_date.strftime('%Y-%m-%d'), amount)
        if rate:
            st.text(format_output(selected_date.strftime('%Y-%m-%d'), from_currency, to_currency, rate, amount))