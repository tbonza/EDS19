""" Clone github repositories and fetch updates when available

See: http://janvitek.org/events/NEU/6050/a1.html
"""
import logging
import os

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

def read_repo_list(fpath: str) -> list:
    """ Read list of repos, return list """
    try:
        with open(fpath, "r") as infile:
            data = infile.readlines()
        return data

    except FileNotFoundError:
        logger.error("File not found: {}".format(fpath))
        return []





# Generate N repo cloning tasks

for repo_name in repos:

    pass # maybe clone repo

# https://github.com/apache/airflow/blob/master/airflow/example_dags/example_python_operator.py
    


