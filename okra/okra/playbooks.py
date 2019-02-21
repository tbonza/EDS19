""" Playbooks for running full analyses """

from okra.repo_mgmt import (create_parent_dir, clone_repo, update_repo)
from okra.s3_utils import download_prove_file
                            

def get_or_update_github_repo(bucket_name, key, file_path):

    # check s3 bucket for repo

    if download_prove_file(bucket_name, key, file_path):
        # s3 retrieve and unpack repo if it exists

        pass

    else:
        # clone repo if present

        pass

    # fetch new commits in both cases
    assert update_repo(repo_name=key, dirpath)

    # extract data and write to a database
    
    # include only new commits in database update

    # pack repo and send to s3

    # delete repo from local disk

def perform_truck_analysis():
    """ Compute truck factor once all data is present in database. """
    pass

    
