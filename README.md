# Currency Converter Web App

Author: Vishal Raj
Student ID: 14227627

## Project Description
This project is a Streamlit web application designed to fetch real-time and historical currency conversion rates from the Frankfurter API. Users can select two currencies, input an amount, and receive the current conversion rate, the converted amount, and the inverse conversion rate. Additionally, users have the capability to specify a historical date to fetch the conversion rate for that day.

## Python Functions Overview:
1.	In api.py:
o	get_url(url: str) -> (int, str): Connects to an API endpoint and retrieves response data.
2.	In frankfurter.py:
o	get_currencies_list() -> list: Fetches a list of available currencies from the API.
o	get_latest_rates(from_currency: str, to_currency: str, amount: float) -> (str, float): Fetches the latest conversion rate between two specified currencies.
o	get_historical_rate(from_currency: str, to_currency: str, from_date: str, amount: float) -> float: Fetches the conversion rate for a specified date between two currencies.
3.	In currency.py:
o	round_rate(rate: float) -> float: Rounds a given rate to four decimal places.
o	reverse_rate(rate: float) -> float: Calculates the inverse of a given rate.
o	format_output(date: str, from_currency: str, to_currency: str, rate: float, amount: float) -> str: Formats the output to display conversion details.

## Instructions to Run on MacOS:
1.	Setup Python Environment:
o	If you don't have Python installed, you can install it using Homebrew. If you don't have Homebrew, install it first with:
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
o	Then, install Python using:
brew install python
2.	Clone/Download Project:
o	If you have git installed, you can clone the repository using:
git clone [repository-url]
o	Alternatively, download the zip file of the project and extract it.
3.	Navigate to Project Directory:
o	Open the terminal.
o	Change directory to where the project files are located using:
cd path_to_directory
4.	Install and Run Streamlit:
a. Standard Installation:
o	Install Streamlit using:
python3 -m pip install streamlit
o	Run the Streamlit app with:
python3 -m streamlit run app.py
b. Using Virtual Environment (Recommended):
o	First, install the virtual environment package if you haven't:
python3 -m pip install virtualenv
o	Create a virtual environment named 'venv' or any name you prefer:
python3 -m virtualenv venv
o	Activate the virtual environment:
source venv/bin/activate
o	Within the activated environment, install Streamlit:
pip install streamlit
o	Run the Streamlit app:
streamlit run app.py
o	Once done, you can deactivate the virtual environment using:
deactivate
5.	Access Web App:
o	A new window should open in your default web browser with the app running. If not, the terminal will display a local URL (typically http://localhost:8501/) which you can enter in your web browser to access the app.

## Using the App:
o	Enter the amount you wish to convert.
o	Select the "from" and "to" currencies from the dropdown menus.
o	Click "Get Latest Rate" to see the current conversion rate and converted amount.
o	Alternatively, select a date and click "Get Historical Rate" to fetch conversion rates for that specific date.