""" Handle the requirements for Assignment 1 

References:
   Assignment 1: "http://janvitek.org/events/NEU/6050/a1.html"
   Git log formatting: "https://git-scm.com/docs/pretty-formats"
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

def clone_repos(repos: list, dirpath: str) -> bool:
    """ Clone repos if they do not already exist. """
    
    for repo_name in repos:

        repo_path = "https://github.com/{}.git".format(repo_name)
        rpath = dirpath + repo_name.split("/")[-1]
        
        if not os.path.exists(rpath):

            logger.info("Started clone{}".format(repo_name))
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
    c1 = "git fetch"
    c2 = "git merge origin/master"

    return True

########################################################################
## Everything below here is related to parsing data from git logs
########################################################################

def parse_commits_csv() -> str:
    """ 

    commits.csv collects basic information about 
    commits and contains the following columns:

    hash
    author
    author email
    author timestamp
    committer
    committer email
    committer timestamp
    """
    c1 = ["git", "log",
          """--pretty=format:'"%H","%an","%ae","%ad","%cn","%ce","%ct"'"""]
    res = subprocess.run(c1, capture_output=True)

    if res.returncode == 0:
        logger.info("SUCCESS -- extracted commits_csv info")
        return res.stdout

    else:
        logger.error("FAIL -- unable to extract commits_csv")
        return ""

def parse_messages_csv():
    """

    messages.csv collects commit messages and their 
    subject as follows:

    hash
    subject
    message
    """
    c1 = ["git", "log",
          """--pretty=format:'"%H","%s","%b"'"""]
    res = subprocess.run(c1, capture_output=True)

    if res.returncode == 0:
        logger.info("SUCCESS -- extracted messages_csv info")
        return res.stdout

    else:
        logger.error("FAIL -- unable to extract messages_csv")
        return ""

def parse_files_csv():
    """

    files.csv informs which files were modified by 
    commits. If a commit modifies multiple files, 
    files.csv will contain multiple lines referencing 
    that commit’s hash (one per modified file).

    hash
    file path
    """
    c1 = ["git", "log",
          '--pretty=format:"^|^%n%H"',
          '--numstat']
    res = subprocess.run(c1, capture_output=True)

    if res.returncode == 0:
        logger.info("SUCCESS -- extracted files_csv info")
        return res.stdout

    else:
        logger.error("FAIL -- unable to extract files_csv")
        return ""

def parse_assn1_data():
    pass
