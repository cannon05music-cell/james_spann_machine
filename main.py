import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

coordinates = os.getenv("COORDINATES") 
# Fetch point metadata
response = requests.get(
    f"https://api.weather.gov/points/{coordinates}",
    headers={"User-Agent": "Morning Briefing App"}
)

def pretty_print(json_data):
    return json.dumps(json_data, indent=4)

contents = response.json()
print(pretty_print(contents))

# Extract forecast URL
forecast_url = contents['properties']['forecast']
print(f"Forecast URL: {forecast_url}")

# Fetch forecast data
forecast_data = requests.get(
    forecast_url,
    headers={"User-Agent": "Morning Briefing App"}
).json()

print(pretty_print(forecast_data))

# Print detailed forecast with lowercase first letter
periods = forecast_data['properties']['periods']

for period in periods:
    df = period['detailedForecast']
    df = df[0].lower() + df[1:] if df else df
    print(f"{period['name']} it will be {df}")
