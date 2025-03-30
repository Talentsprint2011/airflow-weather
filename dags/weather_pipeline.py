from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import fetch_weather
import process_weather

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 3, 28),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'weather_data_pipeline',
    default_args=default_args,
    schedule_interval='* * * * *',
    catchup=False
)

fetch_task = PythonOperator(
    task_id='fetch_weather_data',
    python_callable=fetch_weather.fetch_weather,
    dag=dag
)

process_task = PythonOperator(
    task_id='process_weather_data',
    python_callable=process_weather.process_weather,
    dag=dag
)

fetch_task >> process_task  # Define execution order
