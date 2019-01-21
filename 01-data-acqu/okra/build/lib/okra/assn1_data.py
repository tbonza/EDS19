""" Handle the data requirements for Assignment 1 

References:
   Assignment 1: "http://janvitek.org/events/NEU/6050/a1.html"
   Git log formatting: "https://git-scm.com/docs/pretty-formats"
"""
import logging
import os
import subprocess

logger = logging.getLogger(__name__)


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
