""" Playbooks for running full analyses """
import os
import logging
from urllib.parse import urljoin

from okra.assn4 import get_truck_factor_by_project
from okra.models import DataAccessLayer
from okra.populate_db import populate_db
from okra.error_handling import NetworkError
from okra.repo_mgmt import (create_parent_dir, clone_repo, update_repo,
                            compress_repo, decompress_repo)

logger = logging.getLogger(__name__)

def simple_version_truck_factor(repos: list, dirpath: str, dburl: str, b:int):
    """ Simple version of the truck factor analysis.

    This is a basic version of the truck factor which 
    does not attempt to run the analysis at scale. It's
    just a proof of concept version. Writes out a csv file with
    the truck factor of each repository. You can use this csv file
    to do further analysis in R.

    :param repos: repo queue with value format '<repo owner>/<repo name>'
    :param dirpath: path to working directory to store git repos
    :param dburl: database url (ex. 'sqlite:///:memory')
    :param b: batch size (ex. 1024)
    :return: outputs truck factor analysis as csv file 
    :rtype: None, writes out csv file
    """
    logger.info("STARTED -- simple-version truck factor")

    # Retrieve or update git repos
    
    for repo_name in repos:

        rpath = urljoin(dirpath, repo_name)
        create_parent_dir(repo_name, dirpath)

        if os.path.exists(rpath):
            update_repo(repo_name, dirpath)

        else:
            clone_repo(repo_name, dirpath)

    # Populate database

    populate_db(dburl, dirpath, repos, b)

    # Compute truck factor for each project

    dal = DataAccessLayer(dburl)
    dal.connect()
    dal.session = dal.Session()

    results = []
    for repo_name in repos:

        owner, project = repo_name.split("/")
        truck_factor, _ = get_truck_factor_by_project(owner, project, dal)

        results.append((repo_name, truck_factor))

    dal.session.close()
    logger.info("COMPLETED -- simple-version truck factor")
    return results
    

def retrieve_or_clone(repo_name: str, dirpath: str) -> bool:
    
    # check s3 bucket for repo
    repopath = urljoin(dirpath, repo_name)

    if os.path.exists(repopath): # may already exist
        return True

    else:
        # clone repo if present

        d3 = clone_repo(repo_name, dirpath)
        return d3

def get_or_update_github_repo(bucket_name, dirpath, bucket="ds6050"):

    if not retrieve_or_clone(repo_name, dirpath):
        logger.error("Unable to retrieve or clone {} to {}".\
                     format(repo_name, dirpath))
        raise NetworkError(repo_name, "Unable to retrieve or clone")

    if not update_repo(repo_name, dirpath):
        logger.error("Unable to fetch new commits {}".format(repo_name))
        raise NetworkError(repo_name, "Unable to fetch new commits")
    return True

def persist_repo_data(dirpath, urlstring):
    # extract data and write to a database
    # include only new commits in database update

    # pack repo and send to s3

    # delete repo from local disk
    pass

def perform_truck_analysis():
    """ Compute truck factor once all data is present in database. """
    pass

    
