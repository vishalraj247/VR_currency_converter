import requests

def get_url(url: str) -> (int, str):
    """
    Fetches data from a given URL using a GET request.
    
    Parameters:
    -----------
    url : str
        The URL of the API endpoint or resource to fetch.
        
    Returns:
    --------
    (int, str)
        A tuple where the first item is the HTTP status code 
        and the second item is the response content as text.
        In case of an error during the request, it returns 
        the status code and error message.

    Example:
    --------
    >>> get_url("https://api.frankfurter.app/currencies")
    (200, '{"AED": "United Arab Emirates Dirham", "AFN": ...}')
    """
    
    try:
        response = requests.get(url)
        # Ensure the response status code indicates success (2xx)
        response.raise_for_status()
        return response.status_code, response.text
    except requests.RequestException as e:
        # Handle any exceptions raised during the request and return 
        # the status code along with an error message.
        return response.status_code, str(e)