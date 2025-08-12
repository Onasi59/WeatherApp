import requests

def get_weather(city, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Celsius; use "imperial" for Fahrenheit
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
        return weather
    else:
        print(f"Error: Received response code {response.status_code}")
        print("Response content:", response.text)
        return None

def main():
    api_key = "23b2963b25b8bd73e1bd6a021feb82f1"  # <-- Put your valid API key here!
    print(f"Using API key: {api_key}")  # Verify API key prints correctly
    city = input("Enter city name: ").strip()

    weather = get_weather(city, api_key)

    if weather:
        print(f"\nWeather in {weather['city']}:")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Condition: {weather['description'].capitalize()}")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Wind Speed: {weather['wind_speed']} m/s")
    else:
        print("Could not retrieve weather data. Check the city name or API key.")

if __name__ == "__main__":
    main()
