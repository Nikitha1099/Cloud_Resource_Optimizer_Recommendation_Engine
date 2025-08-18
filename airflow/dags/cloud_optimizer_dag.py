from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
import os

# Add project root to PYTHONPATH so optimizer.py is found
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from optimizer import recommend_config

def run_optimizer():
    recommend_config()

with DAG(
    dag_id="cloud_optimizer",
    start_date=datetime(2025, 1, 1),
    schedule_interval="@daily",
    catchup=False,
) as dag:
    optimize = PythonOperator(
        task_id="optimize_resources",
        python_callable=run_optimizer
    )
