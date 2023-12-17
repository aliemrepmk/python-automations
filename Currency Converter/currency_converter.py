import requests

API_KEY = 'fca_live_3Hmy9m6TLPQJckoxmjVoPDTCrtHkfcPDwJWl1XZg'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD", "EUR", "CAD", "AUD", "GBP", "RUB", "TRY", "JPY", "CNY"]

def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data["data"]
    except requests.RequestException as e:
        print(f"Error making API request: {e}")
        return None
    
def extract_numeric_and_letter_parts(input):
    numeric_part = ''
    letter_part = ''

    for char in input:
        if char.isdigit():
            numeric_part += char
        elif char.isalpha():
            letter_part += char

    return {'numeric_part': int(numeric_part) if numeric_part else None,
            'letter_part': letter_part if letter_part else None}

def main():
    while True:
        base = input("Enter the amount and the base currency for conversion (q for quit): ").upper()

        if base == "Q":
            break
        else:
            result = extract_numeric_and_letter_parts(base)
            amount = result['numeric_part']
            currency = result['letter_part']

        data = convert_currency(currency)
        if not data:
            continue

        del data[currency]

        for currency in CURRENCIES:
            if currency in data:
                converted_value = data[currency] * amount
                print(f"{currency}: {converted_value:.4f}")

if __name__ == "__main__":
    main()