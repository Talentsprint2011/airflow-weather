import requests
import csv
from datetime import datetime

API_URL = "https://api.open-meteo.com/v1/forecast?latitude=40.71&longitude=-74.01&current_weather=true"

def fetch_weather():
    response = requests.get(API_URL)
    data = response.json()

    weather_info = [
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "New York",
        data["current_weather"]["temperature"]
    ]
# /workspaces/airflow-weather/output
    file_path = "/opt/airflow/output/weather_data.csv"
    
    # Write headers if the file doesn't exist
    write_headers = False
    try:
        with open(file_path, "r") as f:
            pass
    except FileNotFoundError:
        write_headers = True

    with open(file_path, "a", newline="") as file:
        writer = csv.writer(file)
        if write_headers:
            writer.writerow(["Timestamp", "City", "Temperature (°C)"])
        writer.writerow(weather_info)

    print("✅ Weather data saved:", weather_info)
