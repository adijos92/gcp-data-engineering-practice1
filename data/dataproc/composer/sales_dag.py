from airflow import DAG
from airflow.operators.bash import BashOperator

from datetime import datetime

with DAG(
    "sales_etl",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False
) as dag:

    run_etl = BashOperator(
        task_id="run_sales_etl",
        bash_command="echo Running ETL"
    )