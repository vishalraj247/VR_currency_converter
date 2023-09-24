# Currency Converter Web App

Author: Vishal Raj<br />
Student ID: 14227627

## Project Description
This project is a Streamlit web application designed to fetch real-time and historical currency conversion rates from the Frankfurter API. Users can select two currencies, input an amount, and receive the current conversion rate, the converted amount, and the inverse conversion rate. Additionally, users have the capability to specify a historical date to fetch the conversion rate for that day.

### Challenges Faced:
* API Limitations: The Frankfurter API, while robust and reliable, has its own rate limits and constraints. Ensuring our application does not exceed these rate limits required implementing error checks and handling.
* Environment Setup: Getting Streamlit to run consistently across different operating systems and Python versions presented a few hitches. Especially when dealing with different Python installations on MacOS. Also added a feature where if any date is selected from future it won't show any conversion information and will provide a warning.
* Date Handling: As the API provides historical data up until September 2013, verifying the correctness of fetched historical rates and handling non-business days added an extra layer of complexity.
* The Frankfurter API provides exchange rates that are sourced from the European Central Bank and they typically updates its rates once every working day, around 16:00 CET. Therefore, if today is Sunday, then the most recent available data would be from Friday, as financial institutions typically don't operate and therefore don't update rates over the weekend.

### Future Implementations:
* Graphical Representation: In the future, we aim to integrate graphical representations to show the fluctuation of currency rates over a span of time. This would give users a more visual understanding of the currency trends.
* Notification Feature: We are looking to implement a notification system where users can set a threshold for a specific currency. Once the currency rate crosses that threshold, the user will be notified, aiding in investment and currency exchange decisions.
* User Profiles and History: To enhance user experience, we are planning to introduce user profiles. This feature will allow users to save their preferences, frequently used currency pairs, and maintain a history of their past conversions.

## Python Functions Overview:
1.	In api.py:
*   get_url(url: str) -> (int, str): Connects to an API endpoint and retrieves response data.
2.	In frankfurter.py:
*	get_currencies_list() -> list: Fetches a list of available currencies from the API.
*	get_latest_rates(from_currency: str, to_currency: str, amount: float) -> (str, float): Fetches the latest conversion rate between two specified currencies.
*	get_historical_rate(from_currency: str, to_currency: str, from_date: str, amount: float) -> float: Fetches the conversion rate for a specified date between two currencies.
3.	In currency.py:
*	round_rate(rate: float) -> float: Rounds a given rate to four decimal places.
*	reverse_rate(rate: float) -> float: Calculates the inverse of a given rate.
*	format_output(date: str, from_currency: str, to_currency: str, rate: float, amount: float) -> str: Formats the output to display conversion details.

## Instructions to Run on MacOS:
1.	Setup Python Environment:
*	If you don't have Python installed, you can install it using Homebrew. If you don't have Homebrew, install it first with:
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
*	Then, install Python using(Note: I used Python 3.11.5):
brew install python
2.	Clone/Download Project:
*	If you have git installed, you can clone the repository using:
git clone https://github.com/vishalraj247/VR_currency_converter.git
*	Alternatively, download the zip file of the project and extract it.
3.	Navigate to Project Directory:
*	Open the terminal.
*	Change directory to where the project files are located using:
cd path_to_directory
4.	Install and Run Streamlit(Note: I used Streamlit 1.27.0):
a. Standard Installation:
*	Install Streamlit using:
python3 -m pip install streamlit
*	Run the Streamlit app with:
python3 -m streamlit run app.py
b. Using Virtual Environment (Recommended):
*	First, install the virtual environment package if you haven't:
python3 -m pip install virtualenv
*	Create a virtual environment named 'venv' or any name you prefer:
python3 -m virtualenv venv
*	Activate the virtual environment:
source venv/bin/activate
*	Within the activated environment, install Streamlit:
pip install streamlit
*	Run the Streamlit app:
streamlit run app.py
*	Once done, you can deactivate the virtual environment using:
deactivate
5.	Access Web App:
*	A new window should open in your default web browser with the app running. If not, the terminal will display a local URL (typically http://localhost:8501/) which you can enter in your web browser to access the app.

## Using the App:
*	Enter the amount you wish to convert.
*	Select the "from" and "to" currencies from the dropdown menus.
*	Click "Get Latest Rate" to see the current conversion rate and converted amount.
*	Alternatively, select a date and click "Get Historical Rate" to fetch conversion rates for that specific date.

## Project Structure:

Below is the structure and brief description of each folder and file in the project:

* app.py:
This is the main Streamlit application script. It manages user inputs, interacts with the backend functions, and displays the results to the user.
* api.py:
Contains functions related to direct API interactions. It has the primary function to make GET requests to the specified API endpoint and handle the response.
* frankfurter.py:
Dedicated to the Frankfurter API endpoints. It contains functions to fetch the list of available currencies, get the latest exchange rates, and retrieve historical exchange rates.
* currency.py:
Houses utility functions for the currency conversion process. It includes functions for rounding rates, calculating the inverse rate, and formatting the output for display.
* README.md:
A markdown file that provides an overview of the project, instructions on how to run the application, and additional documentation about challenges, future enhancements, and project structure.

## Citations
* Documentation. Frankfurter Exchange rates and currency data API. (n.d.). https://www.frankfurter.app/docs/