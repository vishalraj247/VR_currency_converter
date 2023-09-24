from api import get_url
import datetime
import json

BASE_URL = "https://api.frankfurter.app"

def get_currencies_list() -> list:
    """
    Fetch the list of available currencies from the Frankfurter API.
    
    Returns:
    --------
    list:
        A list of available currency codes. Returns None if there's an error in fetching.
    """
    url = f"{BASE_URL}/currencies"
    status, response = get_url(url)
    if status == 200:
        return list(json.loads(response).keys())
    else:
        return None

def get_latest_rates(from_currency: str, to_currency: str, amount: float) -> (str, float):
    """
    Fetch the latest exchange rate for the given currency pair and amount from the Frankfurter API.
    
    Parameters:
    -----------
    from_currency : str
        The source currency code.
    to_currency : str
        The target currency code.
    amount : float
        The amount in source currency to be converted.
        
    Returns:
    --------
    tuple:
        A tuple containing the date of the rate and the converted amount in target currency. 
        Returns (None, None) if there's an error in fetching.
    """
    # Check if the source and target currencies are the same
    if from_currency == to_currency:
        return datetime.date.today().strftime('%Y-%m-%d'), 1.0

    url = f"{BASE_URL}/latest?from={from_currency}&to={to_currency}&amount={amount}"
    status, response = get_url(url)
    if status == 200:
        data = json.loads(response)
        return data['date'], data['rates'][to_currency]
    else:
        return None, None

def get_historical_rate(from_currency: str, to_currency: str, from_date: str, amount: float) -> float:
    """
    Fetch the historical exchange rate for the given currency pair, date, and amount from the Frankfurter API.
    
    Parameters:
    -----------
    from_currency : str
        The source currency code.
    to_currency : str
        The target currency code.
    from_date : str
        The date for which the historical rate is required.
    amount : float
        The amount in source currency to be converted.
        
    Returns:
    --------
    float:
        The converted amount in target currency. Returns None if there's an error in fetching.
    """
    # Check if the source and target currencies are the same
    if from_currency == to_currency:
        return 1.0

    url = f"{BASE_URL}/{from_date}?from={from_currency}&to={to_currency}&amount={amount}"
    status, response = get_url(url)
    if status == 200:
        data = json.loads(response)
        return data['rates'][to_currency]
    else:
        return None