import requests

def get_url(url: str) -> (int, str):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.status_code, response.text
    except requests.RequestException as e:
        return response.status_code, str(e)