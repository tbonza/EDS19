""" Solution for DS 6050 Assignment 1 """
from datetime import datetime

import airflow
from airflow.operators.python_operator import PythonOperator
from airflow.models import DAG

from okra.repo_mgmt import read_repos, clone_repo

file_args = {
    'repos' : 'repos.list',
    'data_dir': '/Users/tylerbrown/Downloads/',
}

args = {
    'owner': 'airflow',
    'start_date': airflow.utils.dates.days_ago(1),
    'retries':3,
    'execution_date': datetime(2019, 1, 21),
}

dag = DAG(dag_id='assn1', default_args=args)

repos = read_repos(file_args.get('repos',''))

for repo_name in repos:

    airflow_repo_name = repo_name.replace('/', '_')

    task_clone_repo = PythonOperator(
        task_id='clone_repo_{}'.format(airflow_repo_name),
        python_callable=clone_repo,
        op_kwargs={
            'repo_name': repo_name,
            'dirpath': file_args.get('data_dir', '.'),
        },
        dag=dag,
    )

    task_clone_repo




