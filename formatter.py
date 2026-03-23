def format_weather(data: dict, units: str = "metric") -> None:
    """Format and print weather data in a readable way."""
    city        = data["name"]
    country     = data["sys"]["country"]
    description = data["weather"][0]["description"].capitalize()
    temp        = data["main"]["temp"]
    feels_like  = data["main"]["feels_like"]
    humidity    = data["main"]["humidity"]
    wind_speed  = data["wind"]["speed"]

    unit_symbol  = "°C"  if units == "metric" else "°F"
    speed_unit = "km/h" if units == "metric" else "mph"

    if units == "metric":
        wind_speed = round(wind_speed * 3.6, 1)  # m/s → km/h

    print()
    print(f"📍  {city}, {country}")
    print(f"🌤️   {description}")
    print(f"🌡️   {temp}{unit_symbol}  (feels like {feels_like}{unit_symbol})")
    print(f"💨  Wind: {wind_speed} {speed_unit}")
    print(f"💧  Humidity: {humidity}%")
    print()