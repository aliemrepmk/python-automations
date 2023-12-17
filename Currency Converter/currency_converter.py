import tkinter as tk
from tkinter import ttk
import requests

API_KEY = 'fca_live_3Hmy9m6TLPQJckoxmjVoPDTCrtHkfcPDwJWl1XZg'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD", "EUR", "CAD", "AUD", "GBP", "RUB", "TRY", "JPY", "CNY"]

def convert_currency(base, amount_var, result_label):
    amount = amount_var.get()
    result_label.config(text="Converting...")

    data = convert_currency_api(base, amount)
    if not data:
        result_label.config(text="Error making API request")
        return

    del data[base]

    result_label.config(text="")
    for currency in CURRENCIES:
        if currency in data:
            converted_value = data[currency] * float(amount)
            result_label.config(text=result_label.cget("text") + f"{currency}: {converted_value:.4f}\n")

def convert_currency_api(base, amount):
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

def main():
    root = tk.Tk()
    root.title("Currency Converter")

    amount_label = ttk.Label(root, text="Enter amount:")
    amount_label.pack(pady=10)

    amount_var = tk.StringVar()
    amount_entry = ttk.Entry(root, textvariable=amount_var)
    amount_entry.pack(pady=10)

    base_label = ttk.Label(root, text="Enter base currency:")
    base_label.pack(pady=10)

    base_var = tk.StringVar()
    base_entry = ttk.Entry(root, textvariable=base_var)
    base_entry.pack(pady=10)

    result_label = ttk.Label(root, text="")
    result_label.pack(pady=10)

    convert_button = ttk.Button(root, text="Convert", command=lambda: convert_currency(base_var.get(), amount_var, result_label))
    convert_button.pack(pady=10)

    quit_button = ttk.Button(root, text="Quit", command=root.destroy)
    quit_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
