# Weather CLI 🌤️

A simple command-line tool that fetches and displays current weather data for any city using the OpenWeatherMap API.

---

## Features

- Get current temperature, weather condition and wind speed for any city
- Displays results in a clean, readable format
- Configurable units (metric / imperial)

---

## Requirements

- Python 3.8+
- A free OpenWeatherMap API key ([sign up here](https://openweathermap.org/api))

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/loay-invents/weather-CLI
   cd weather-cli
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create your `.env` file:
   ```bash
   cp .env.example .env
   ```

4. Add your API key to `.env`:
   ```
   API_KEY=your_openweathermap_key_here
   UNITS=metric
   ```

---

## Usage

```bash
python weather.py Berlin
python weather.py "New York"
python weather.py Tokyo
```

**Example output:**
```
📍 Berlin, DE
🌤️  Partly Cloudy
🌡️  18°C  (feels like 16°C)
💨  Wind: 12 km/h
💧  Humidity: 65%
```

---

## Project Structure

```
weather-cli/
├── weather.py        ← Main entry point
├── formatter.py      ← Output formatting
├── .env              ← Your API key (never commit this!)
├── .env.example      ← Safe template to share
├── .gitignore        ← Excludes .env from git
├── README.md
└── requirements.txt
```

---

## Important

> ⚠️ Never commit your `.env` file to Git.  
> Your API key is a secret — keep it out of version control.  
> This project includes a `.gitignore` that excludes `.env` automatically.

---

## License

MIT
