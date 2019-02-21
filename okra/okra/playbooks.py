""" Playbooks for running full analyses """
import os
import logging
from urllib.parse import urljoin

from okra.error_handling import NetworkError
from okra.repo_mgmt import (create_parent_dir, clone_repo, update_repo,
                            compress_repo, decompress_repo)
from okra.s3_utils import download_prove_file


logger = logging.getLogger(__name__)

def retrieve_or_clone(repo_name: str, dirpath: str) -> bool:
    
    # check s3 bucket for repo
    repopath = urljoin(dirpath, repo_name)

    if os.path.exists(repopath): # may already exist
        return True

    elif download_prove_file(repo_name, dirpath):
    
        # s3 retrieve and unpack repo if it exists
        
        d2 = decompress_repo(repo_name, dirpath)
        return d2

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

    
