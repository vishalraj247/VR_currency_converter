import streamlit as st
from frankfurter import get_currencies_list, get_latest_rates, get_historical_rate
from currency import reverse_rate, round_rate, format_output
import datetime

# Display the application's main title on the Streamlit web page
st.title("VR Currency Converter")

# Fetch a list of available currency codes from the Frankfurter API
currencies = get_currencies_list()

# Display an error if the list of currencies cannot be fetched
if not currencies:
    st.error("Error fetching available currencies. Please try again later.")
else:
    # Collect user input for the amount they wish to convert
    amount = st.number_input("Enter the amount to be converted", min_value=1.0)

    # Dropdowns for selecting the origin and target currencies for conversion
    from_currency = st.selectbox("From Currency", currencies)
    to_currency = st.selectbox("To Currency", currencies)

    # Fetch and display the latest exchange rate upon button press
    if st.button("Get Latest Rate"):
        date, rate = get_latest_rates(from_currency, to_currency)

        # Display an info message if the fetched exchange rate isn't from the current day
        if date and rate and datetime.datetime.strptime(date, '%Y-%m-%d').date() < datetime.date.today():
            st.info(f"Note: The most recent available data is from {date}. Exchange rates are typically updated on working days only.")
            
        st.text(format_output(date, from_currency, to_currency, rate, amount))

# Capture the current date to use for comparison later
today = datetime.date.today()

# Allow the user to select a date for fetching historical rates, ensuring today and future dates are not selectable
selected_date = st.date_input("Select a date for historical rates", today - datetime.timedelta(days=1), max_value=today - datetime.timedelta(days=1))

# Function to determine the most recent Saturday relative to a given date
def get_previous_saturday(date):
    return date - datetime.timedelta((date.weekday() + 2) % 7)

# Determine which date should be used in the displayed output
display_date = selected_date

# Display an info message if a date from the most recent weekend is selected
if selected_date.weekday() in [5, 6] and get_previous_saturday(today) == get_previous_saturday(selected_date):
    st.info("Note: Exchange rates are typically not updated on weekends. Displaying data from the latest working day (usually Friday).")
    
    # Adjust the display date to point to the previous Friday
    display_date = selected_date - datetime.timedelta(days=selected_date.weekday() - 4)

# Fetch and display historical exchange rate for the selected date upon button press
if st.button("Get Historical Rate"):
    rate = get_historical_rate(from_currency, to_currency, selected_date.strftime('%Y-%m-%d'))
    if rate:
        st.text(format_output(display_date.strftime('%Y-%m-%d'), from_currency, to_currency, rate, amount))