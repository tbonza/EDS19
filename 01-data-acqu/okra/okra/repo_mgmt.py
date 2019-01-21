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
                         stdout=subprocess.PIPE)

    if res.returncode == 0 and os.path.exists(rpath):
        return True
    else:
        return False

def update_repo(repo_name: str, dirpath: str) -> bool:
    """ Update repo with new code. """
    c1 = ["git", "fetch"]
    return True


