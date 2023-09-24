from api import get_url
import json

BASE_URL = "https://api.frankfurter.app"

def get_currencies_list() -> list:
    url = f"{BASE_URL}/currencies"
    status, response = get_url(url)
    if status == 200:
        return list(json.loads(response).keys())
    else:
        return None

def get_latest_rates(from_currency: str, to_currency: str, amount: float) -> (str, float):
    url = f"{BASE_URL}/latest?from={from_currency}&to={to_currency}&amount={amount}"
    status, response = get_url(url)
    if status == 200:
        data = json.loads(response)
        return data['date'], data['rates'][to_currency]
    else:
        return None, None

def get_historical_rate(from_currency: str, to_currency: str, from_date: str, amount: float) -> float:
    url = f"{BASE_URL}/{from_date}?from={from_currency}&to={to_currency}&amount={amount}"
    status, response = get_url(url)
    if status == 200:
        data = json.loads(response)
        return data['rates'][to_currency]
    else:
        return None