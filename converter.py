# Simple sample exchange rates
# Rates are based on 1 USD

rates = {
    "USD": 1.00,
    "INR": 83.00,
    "EUR": 0.92,
    "GBP": 0.79
}

def convert_currency(amount, from_currency, to_currency):
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")

    if from_currency not in rates or to_currency not in rates:
        raise ValueError("Currency not supported.")

    # First convert the amount to USD
    usd_amount = amount / rates[from_currency]

    # Then convert USD to the target currency
    result = usd_amount * rates[to_currency]

    save_history(amount, from_currency, result, to_currency)

    return result

def save_history(amount, from_currency, result, to_currency):
    with open("history.txt", "a") as file:
        file.write(
            f"{amount:.2f} {from_currency} = "
            f"{result:.2f} {to_currency}\n"
        )
