import requests
import tkinter as tk
from tkinter import messagebox

API_KEY = "1e1cc925ab6783b40351708f315e6234"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showwarning("Warning", "Please enter a valid city name.")
        return

    request_url = f"{BASE_URL}?appid={API_KEY}&q={city}&units=metric"

    try:
        response = requests.get(request_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        data = response.json()

        weather = data['weather'][0]['description']
        temperature = data['main']['temp']

        result_label.config(text=f"Weather: {weather.capitalize()}\nTemperature: {temperature}°C")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    except KeyError:
        messagebox.showerror("Error", "Failed to parse weather data. Please check the city name.")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

root = tk.Tk()
root.title("Weather App")

# Create and place widgets
label = tk.Label(root, text="Enter a city for weather data: ")
label.pack(pady=10)

city_entry = tk.Entry(root)
city_entry.pack(pady=10)

get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()