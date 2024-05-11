import requests
from bs4 import BeautifulSoup

#IRS III example (extracts weather of new york from weather.gov)
#by Noor Alresaini

#weather
def get_current_weather(location):
    url = f"https://forecast.weather.gov/MapClick.php?lat=40.713&lon=-74.0072&textField1={location}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract current weather
    current_weather_element = soup.find(class_="myforecast-current-lrg")
    if current_weather_element:
        current_weather = current_weather_element.get_text().strip()
    else:
        current_weather = "Current weather information not available."
    
    return current_weather

#weather forecast
def get_weather_forecast(location):
    url = f"https://forecast.weather.gov/MapClick.php?lat=40.713&lon=-74.0072&textField1={location}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract weather forecast information if available
    forecast = soup.find(id="seven-day-forecast")
    if forecast:
        forecast_items = forecast.find_all(class_="tombstone-container")
        weather_forecast = [item.get_text().strip() for item in forecast_items]
    else:
        weather_forecast = "Weather forecast not available."
    
    return weather_forecast


location = "New York"
current_weather = get_current_weather(location)
weather_forecast = get_weather_forecast(location)

print("Current Weather:", current_weather)
print("Weather Forecast:", weather_forecast)
