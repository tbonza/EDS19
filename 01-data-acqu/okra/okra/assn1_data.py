""" Handle the data requirements for Assignment 1 

References:
   Assignment 1: "http://janvitek.org/events/NEU/6050/a1.html"
   Git log formatting: "https://git-scm.com/docs/pretty-formats"
"""
import csv
import logging
import os
import subprocess

from okra.protobuf.assn1_pb2 import Commit, Message, File

logger = logging.getLogger(__name__)


def parse_commits(rpath: str):
    """ Yields a protocol buffer of git commit information.

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
          "--pretty=%H^|^%an^|^%ae^|^%ad^|^%cn^|^%ce^|^%ct"]
    res = subprocess.run(c1, cwd=rpath, capture_output=True)

    if res.returncode == 0:
        logger.info("SUCCESS -- extracted commits_csv info")

        rows = res.stdout.splitlines()

        for row_num, row in enumerate(rows):

            items = row.decode('utf-8', 'ignore').split("^|^")

            if len(items) == 7:
                commit = Commit()

                commit.hash_val = items[0]
                commit.author = items[1]
                commit.author_email = items[2]
                commit.author_timestamp = items[3]
                commit.committer = items[4]
                commit.committer_email = items[5]
                commit.committer_timestamp = items[6]
                
                yield commit

            else:
                logger.error("Issue with row {}, repo '{}'".\
                             format(row_num, rpath))            
    else:
        logger.error("FAIL -- unable to extract commits_csv")

def write_line_commits(parsed_commits):
    """ Generate a line for each git commit message. """
    for commit in parsed_commits:

        row = [
            commit.hash_val,
            commit.author,
            commit.author_email,
            commit.author_timestamp,
            commit.committer,
            commit.committer_email,
            commit.committer_timestamp,
        ]
        yield row

def parse_messages(rpath: str):
    """ Yields a protocol buffer of a git commit message.
    
    messages.csv collects commit messages and their 
    subject as follows:

    hash
    subject
    message
    """
    c1 = ["git", "log",
          "--pretty=^^!^^%H^|^%s^|^%b"]
    res = subprocess.run(c1, cwd=rpath, capture_output=True)

    if res.returncode == 0:
        logger.info("SUCCESS -- extracted messages_csv info")

        rows = res.stdout.decode('utf-8', 'ignore').split("^^!^^")

        for row_num, row in enumerate(rows):

            items = row.split("^|^")

            if len(items) == 3:

                message = Message()

                message.hash_val = items[0]
                message.subject = items[1]
                message.message_body = items[2]

                yield message
                
            else:
                logger.error("Issue with row {}, repo '{}'".\
                             format(row_num, rpath))
    else:
        logger.error("FAIL -- unable to extract messages_csv")

def write_line_messages(parsed_messages):
    """ Generate a line for each git commit message. """

    for message in parsed_messages:

        row = [
            message.hash_val,
            message.subject,
            message.message_body,
        ]
        yield row

def parse_files(rpath: str):
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
    res = subprocess.run(c1, cwd=rpath, capture_output=True)

    if res.returncode == 0:
        logger.info("SUCCESS -- extracted files_csv info")
        return res.stdout

    else:
        logger.error("FAIL -- unable to extract files_csv")
        return ""

def write_bulk_csv(fpath: str, dirpath: str, repos:list, write_line,
                   delim=",", quotechar='"'):
    """ Write a bulk csv file.

    This is honestly going to get corrupted no matter what
    so I'm just doing this because the assignment requests 
    it.

    :param fpath: file path to csv output file
    :param dirpath: directory path containing git repos
    :param repos: list of repo names
    :param write_line: function, used to write line for 
        a specific row type.
    :return: writes csv file to disk
    :rtype: None
    """
    row_count = 0
    try:
        logger.info("STARTED writing csv file: {}".format(fpath))
        with open(fpath, "w") as outfile:
            writer = csv.writer(outfile, delimiter=delim,
                                quotechar=quotechar,
                                quoting=csv.QUOTE_MINIMAL)
            
            for row in write_line(repos, dirpath):

                try:
                    writer.writerow(row)

                except Exception as exc:
                    logger.exception(exc)

                if row_count % 10000 == 0:
                    logger.info("Wrote {} rows to {}".\
                                format(row_count, fpath))

                row_count += 1

        logger.info("Wrote {} rows to {}".format(row_count, fpath))
        logger.info("FINISHED writing csv file: {}".format(fpath))

    except Exception as exc:
        logger.exception(exc)

def extract_data_main(fpath: str, dirpath: str):
    pass
