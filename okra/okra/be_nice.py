""" A nice approach to to downloading GitHub repos.

Previous approaches to downloading GitHub repositories
were set up in parallel on Kubernetes using Redis. This
approach was considered too aggressive by both GitHub and
Google. This approach is meant to be nice.
"""
import csv
import logging
import os
import time
from urllib.parse import urljoin

from okra.repo_mgmt import create_parent_dir, gcloud_clone_or_fetch_repo
from okra.populate_db import populate_db
from okra.playbooks import local_persistance
from okra.error_handling import (MissingEnvironmentVariableError,
                                 NetworkError,
                                 DirectoryNotCreatedError)



logger = logging.getLogger(__name__)


def parse_bigquery_csv(fpath: str):

    repos = []
    with open(fpath, "r") as infile:
        reader = csv.DictReader(fpath)

        for row in reader:

            cln = row.get('url', None)
            cln = cln.replace("https://api.github.com/repos/","")
            repos.append(cln)

    return repos

def okay_benice(qpath: str):

    cache = os.getenv("CACHE")
    buffer_size = int(os.getenv("BUFFER_SIZE"))

    logger.info("Cache {}, buffer size {}".format(cache, buffer_size))
    if cache is None or buffer_size is None:
        raise MissingEnvironmentVariableError(
            expression = "cache or buffer size missing",
            message = "cache {}, buffer size {}".format(cache, buffer_size)
        )

    #repos = parse_bigquery_csv(qpath)
    repos = [i.strip().replace("https://api.github.com/repos/","")
             for i in open(qpath, "r").readlines()]
    logger.info("Found {} repos".format(len(repos)))
    

    # Retrieve, update, then persist repos

    count = 0
    for repo_name in repos:

        time.sleep(10)

        logger.info("STARTED processing {}".format(repo_name))
        rpath = urljoin(cache, repo_name)

        try:
            create_parent_dir(repo_name, dirpath=cache)
            gcloud_clone_or_fetch_repo(repo_name, ssh=True)

            # Update repo db

            repodb = "__REPODB__".join(repo_name.split("/"))
            dburl = "sqlite:///" + cache + repodb + ".db"
            populate_db(dburl, cache, repo_name, buffer_size)
            logger.info("FINISHED processing {}".format(repo_name))

        except Exception as exc:

            logger.exception(exc)

        if count % 100 == 0:
            logger.info("Processed {} repos".format(count))
        count += 1

    logger.info("Processed {} total repos".format(count))
    


        

        

