""" Assignment 4 using okra """
import csv
import logging

from okra.playbooks import simple_version_truck_factor
from okra.logging_utils import enable_log

logger = logging.getLogger(__name__)

enable_log("db-test.log")

logger.info("STARTED assn4 simple version")

with open("repos.list", "r") as infile: 
    repos = [i.strip() for i in infile.readlines()]

dirpath = "/Users/tylerbrown/code/smoketest/"
dburl = "sqlite:///assn4.db"
csvpath = "truck_factor_assn4.csv"
b = 1024 * 50

results = simple_version_truck_factor(repos, dirpath, dburl, b)

fieldnames = ["repo_name", "truck_factor"]
with open(csvpath, "w") as outfile:
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in results:
        i = {
            "repo_name"    : row[0],
            "truck_factor" : row[1],
        }
        writer.writerow(i)


logger.info("FINISHED assn4 simple version")

