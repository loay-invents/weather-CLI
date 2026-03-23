import sys
import os
import requests
from dotenv import load_dotenv
from formatter import format_weather, format_separator

load_dotenv()

API_KEY = os.getenv("API_KEY")
UNITS   = os.getenv("UNITS", "metric")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def fetch_weather(city: str) -> dict:
    """Fetch current weather data for a given city from OpenWeatherMap."""
    if not API_KEY:
        print("Error: API_KEY not found. Please check your .env file.")
        sys.exit(1)

    params = {
        "q":     city,
        "appid": API_KEY,
        "units": UNITS,
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 401:
        print("Error: Invalid API key. Please check your .env file.")
        sys.exit(1)

    if response.status_code == 404:
        print(f"Error: City '{city}' not found.")
        sys.exit(1)

    if response.status_code != 200:
        print(f"Error: Unexpected response ({response.status_code}).")
        sys.exit(1)

    return response.json()


def main():
    if len(sys.argv) < 2:
        print("Usage: python weather.py <city> [city2] [city3] ...")
        print("Example: python weather.py Berlin London Tokyo")
        sys.exit(1)

    cities = sys.argv[1:]

    for i, city in enumerate(cities):
        data = fetch_weather(city)
        if data:
            format_weather(data, UNITS)
        if i < len(cities) - 1:
            format_separator()



if __name__ == "__main__":
    main()