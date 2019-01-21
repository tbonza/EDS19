""" GitHub Repo Managment

Related to downloading and updating GitHub repos. 
"""
import logging
import os
import subprocess

logger = logging.getLogger(__name__)

def read_repos(fpath: str) -> list:
    """ Read list of repos from disk """
    try:
        with open(fpath, "r") as infile:
            data = infile.readlines()

        data = [i.strip() for i in data]
        return data

    except FileNotFoundError:
        logger.error("File not found: {}".format(fpath))
        return []

def clone_repo(repo_name: str, dirpath: str) -> bool:
    """ Clone GitHub repo. """
    repo_path = "https://github.com/{}.git".format(repo_name)
    rpath = dirpath + repo_name.split("/")[-1]

    res = subprocess.run(["git", "clone", repo_path, rpath],
                         capture_output = True)

    if res.returncode == 0 and os.path.exists(rpath):
        return True
    else:
        return False



def clone_repos(repos: list, dirpath: str) -> bool:
    """ Clone repos if they do not already exist. """
    
    for repo_name in repos:

        repo_path = "https://github.com/{}.git".format(repo_name)
        rpath = dirpath + repo_name.split("/")[-1]
        
        if not os.path.exists(rpath):

            logger.info("Started clone '{}'".format(repo_name))
            res = subprocess.run(["git", "clone", repo_path, rpath],
                                 capture_output = True)

            if res.returncode == 0:
                logger.info("Successful clone: {}".format(repo_name))
            else:
                logger.error("Unsuccessful clone: {}".format(repo_name))
                logger.error("{} error, {}".format(repo_name,
                                                   res.stdout))

        else:
            logger.info("Repo {} already exists".format(repo_name))

    return True

def update_repos(repos: list, dirpath: str) -> bool:
    """ Drop into each repo and update code with new commits. """

    # cd into directory
    c1 = ["git", "fetch"]
    c2 = ["git", "merge", "origin/master"]

    for repo_name in repos:

        repo = repo_name.split("/")[-1]
        dpath = dirpath + repo

        s1 = subprocess.run(["git", "fetch"], cwd=dpath)
        if s1.returncode == 0:

            s2 = subprocess.run(["git", "merge", "origin/master"], cwd=dpath)

            if s2.returncode == 0:
                logger.info("SUCCESS - updated '{}'".format(repo_name))

            else:
                logger.error("Unable to merge upstream: {}".\
                             format(repo_name))
        else:
            logger.error("Unable to fetch '{}'".format(repo_name))
            
    return True
