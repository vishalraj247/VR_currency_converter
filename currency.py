def round_rate(rate: float) -> float:
    return round(rate, 4)

def reverse_rate(rate: float) -> float:
    if rate != 0:
        return round_rate(1/rate)
    else:
        return 0

def format_output(date: str, from_currency: str, to_currency: str, rate: float, amount: float) -> str:
    converted_amount = round(amount * rate, 2)
    inverse_rate = reverse_rate(rate)
    return (f"The conversion rate on {date} from {from_currency} to {to_currency} was {round_rate(rate)}. \n"
            f"So {amount} in {from_currency} correspond to {converted_amount} in {to_currency}. "
            f"The inverse rate was {inverse_rate}.")