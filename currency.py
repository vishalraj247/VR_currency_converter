def round_rate(rate: float) -> float:
    """
    Round a given rate to 4 decimal places.

    Parameters:
    - rate (float): The rate to be rounded.

    Returns:
    - float: The rate rounded to 4 decimal places.
    """
    return round(rate, 4)

def reverse_rate(rate: float) -> float:
    """
    Compute the inverse of a given rate. 
    If the provided rate is zero, return zero as its inverse to prevent division by zero.

    Parameters:
    - rate (float): The rate whose inverse needs to be calculated.

    Returns:
    - float: The inverse of the rate rounded to 4 decimal places or zero if the rate is zero.
    """
    if rate != 0:
        return round_rate(1/rate)
    else:
        return 0

def format_output(date: str, from_currency: str, to_currency: str, rate: float, amount: float) -> str:
    """
    Format the conversion details into a readable string output.
    
    Parameters:
    - date (str): The date of the conversion rate.
    - from_currency (str): The source currency code.
    - to_currency (str): The target currency code.
    - rate (float): The conversion rate from the source to target currency.
    - amount (float): The amount in the source currency to be converted.

    Returns:
    - str: A formatted string detailing the conversion rate, amount in source currency, 
           converted amount in target currency, and the inverse rate.
    """
    converted_amount = round(amount * rate, 2)
    inverse_rate = reverse_rate(rate)
    return (f"The conversion rate on {date} from {from_currency} to {to_currency} was {round_rate(rate)}. \n"
            f"So {amount} in {from_currency} correspond to {converted_amount} in {to_currency}. "
            f"The inverse rate was {inverse_rate}.")