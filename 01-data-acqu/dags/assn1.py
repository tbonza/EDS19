""" Solution for DS 6050 Assignment 1 """
from datetime import datetime

from airflow.operators import PythonOperator
from airflow.models import DAG

from okra.repo_mgmt import read_repos


args = {
    'owner': 'airflow',
}

dag = DAG(dag_id='assn1')


