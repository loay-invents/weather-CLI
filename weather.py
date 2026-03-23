import sys
import os
import requests
from dotenv import load_dotenv
from formatter import format_weather

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
        print("Usage: python weather.py <city>")
        print("Example: python weather.py Berlin")
        sys.exit(1)

    city = " ".join(sys.argv[1:])
    data = fetch_weather(city)
    format_weather(data, UNITS)


if __name__ == "__main__":
    main()