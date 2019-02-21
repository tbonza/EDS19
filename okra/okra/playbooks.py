""" Playbooks for running full analyses """
import logging

from okra.repo_mgmt import (create_parent_dir, clone_repo, update_repo,
                            compress_repo, decompress_repo)
from okra.s3_utils import download_prove_file


logger = logging.getLogger(__name__)

def retrieve_or_clone(repo_name: str, dirpath: str) -> bool:
    
    # check s3 bucket for repo

    if download_prove_file(repo_name, dirpath):
    
        # s3 retrieve and unpack repo if it exists
        
        d2 = decompress_repo(repo_name, dirpath)
        return d2

    else:
        # clone repo if present

        d3 = clone_repo(repo_name, dirpath)
        return d3



def get_or_update_github_repo(bucket_name, key, file_path):

    #retrieve_or_clone()

    # fetch new commits in both cases
    #assert update_repo(repo_name=key, dirpath)

    # extract data and write to a database
    
    # include only new commits in database update

    # pack repo and send to s3

    # delete repo from local disk
    pass

def perform_truck_analysis():
    """ Compute truck factor once all data is present in database. """
    pass

    
