from pendulum import datetime, duration
from airflow import DAG
from airflow.sdk import task

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': duration(minutes=5),
}

with DAG(
    dag_id='hello_world_dag',
    default_args=default_args,
    description='A simple Hello World DAG using TaskFlow API',
    schedule='* * * * *',  # Every minute
    start_date=datetime(2023, 1, 1, tz="Europe/Oslo"),
    catchup=False,
    tags=['example'],
) as dag:
    @task
    def hello_world():
        print("Hello, world!")

    hello_world()
