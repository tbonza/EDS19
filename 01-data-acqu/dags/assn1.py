""" Solution for DS 6050 Assignment 1 """
from datetime import datetime

from airflow.operators.python_operator import PythonOperator
from airflow.models import DAG

from okra.repo_mgmt import read_repos, clone_repo


args = {
    'owner': 'airflow',
}

dag = DAG(dag_id='assn1')

#repo_names = PythonOperator(
#)



