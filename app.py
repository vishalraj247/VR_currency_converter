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
            # Inform the user if the latest data is not from today
            if datetime.datetime.strptime(date, '%Y-%m-%d').date() < datetime.date.today():
                st.info(f"Note: The most recent available data is from {date}. Exchange rates are typically updated on working days only.")
            st.text(format_output(date, from_currency, to_currency, rate, amount))
    
# Get today's date
today = datetime.date.today()

# Allow user to select a date for historical rates but prevent selection of today's date or any future dates
selected_date = st.date_input("Select a date for historical rates", today - datetime.timedelta(days=1), max_value=today - datetime.timedelta(days=1))

# Define a function to get the previous Saturday
def get_previous_saturday(date):
    return date - datetime.timedelta((date.weekday() + 2) % 7)

# Display date is the date shown in the output
display_date = selected_date

# When the user selects a Saturday or Sunday
if selected_date.weekday() in [5, 6]:  
    # If the selected weekend is the current weekend
    if get_previous_saturday(today) == get_previous_saturday(selected_date):
        st.info("Note: Exchange rates are typically not updated on weekends. Displaying data from the latest working day (usually Friday).")
        if selected_date.weekday() == 5: # if it's Saturday
            display_date = selected_date - datetime.timedelta(days=1)
        else: # if it's Sunday
            display_date = selected_date - datetime.timedelta(days=2)

if st.button("Get Historical Rate"):
    rate = get_historical_rate(from_currency, to_currency, selected_date.strftime('%Y-%m-%d'), amount)
    if rate:
        st.text(format_output(display_date.strftime('%Y-%m-%d'), from_currency, to_currency, rate, amount))