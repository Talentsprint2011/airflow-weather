import pandas as pd

def process_weather():
    file_path = "/workspaces/airflow-weather/output/weather_data.csv"

    try:
        df = pd.read_csv(file_path)
        avg_temp = df["Temperature (°C)"].mean()
        print(f"📊 Average Temperature: {avg_temp:.2f}°C")
    except Exception as e:
        print(f"⚠️ Error processing data: {e}")
