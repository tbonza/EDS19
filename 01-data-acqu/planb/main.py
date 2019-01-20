""" Main file for executing scripts. """
import argparse
import logging

from assn1 import read_repos, clone_repos
logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser()
parser.add_argument("repo_list")
parser.add_argument("directory_path")

args = parser.parse_args()

def enable_log(log_name):
    """ Enable logs written to file """
    logging.basicConfig(filename= log_name + ".log",
                        level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(message)s')

def repo_clone_main(fpath="repos.list", dirpath="/dev/sdf/"):
    repos = read_repos(fpath)
    clone_repos(repos, dirpath)

if __name__ == "__main__":

    enable_log("assignment_1")
    logger.info("Started process")
    repo_clone_main(args.repo_list, args.directory_path)
    logger.info("Completed process")
