""" Load redis queue. 

Based on the redis work queue.

Reference:
https://kubernetes.io/docs/tasks/job/fine-parallel-processing-work-queue/
"""
import logging
import os
import re
from urllib.parse import urljoin
import uuid

import redis

from okra.gcloud_utils import read_gcloud_blob, repo_list_gcloud_bucket

logger = logging.getLogger(__name__)

class RedisLoader(object):

    reference = 100

    def __init__(self, name, **redis_kwargs):
        self._db = redis.StrictRedis(**redis_kwargs)
        self._main_q_key = bytes(name, encoding='utf8')
        self._session = str(uuid.uuid4())

    def sessionID(self):
        """ Return the ID for this session. """
        return self._session

    def _load_queue(self, data: list):
        """ Load redis queue. 

        :param data: list of string values for redis queue
        :return: loaded items into redis queue
        :rtype: None
        """
        try:
            logger.info("STARTED loading data in queue '{}'".\
                        format(self._main_q_key))
            count = 0
            for item in data:

                bitem = bytes(item, encoding='utf8')
                
                self._db.rpush(self._main_q_key, bitem)

                if count % self.reference == 0:
                    logger.info("Loaded {} items in queue '{}'".\
                                format(count, self._main_q_key))
                count += 1

            logger.info("Loaded {} items in queue '{}'".\
                        format(count, self._main_q_key))
            logger.info("FINISHED loading data in queue '{}'".\
                        format(self._main_q_key))

        except Exception as exc:
            logger.error("Failed to finish loading queue '{}'".\
                         format(self._main_q_key))
            logger.exception(exc)

                

    def read_repolist(self, fpath):
        """ Read the 'GitHub repo list' format and load queue.

        Regular expression pertains to ghtorrent api strings
        that they use to define the location of each repo.

        :param fpath: str, file path to repo list text file
        :return: loaded redis queue
        :rtype: None
        """
        pat = re.compile(r".*repos/(\w+/\w+)|(\w+/\w+)")
        try:
            data = []
            with open(fpath, "r") as infile:
                for line in infile.readlines():

                    matchy = pattern.match(line)

                    if matchy:
                        matched = matchy.groups()
                        if matched[0] is not None:
                            data.append(matched[0])

                        elif matched[1] is not None:
                            data.append(matched[1])
                            
                        else:
                            logger.error("Unable to parse: {}".format(line))
            
            logger.info("Retrieved file '{}', loading queue '{}'".\
                        format(fpath, self._main_q_key))
            self._load_queue(data)

        except Exception as exc:
            logger.error("Unable to read file '{}'".format(fpath))
            logger.exception(exc)

    def read_gcloud_repolist(self, bucket_id, prefix):
        """ Read the 'GitHub repo list' format from gcloud, load queue.

        :param bucket_id: bucket name of gcloud storage
        :param prefix: specify load files; ex. 'repo_list/results_'
        :return: loads repolist to redis finite queue
        :rtype: None
        """
        cache = os.getenv("CACHE")
        dirpath = "repo_list/"
        repo_list_dir = urljoin(cache, dirpath)
        try:
            if not os.path.exists(repo_list_dir):
                os.mkdir(repo_list_dir)

            for gpath in repo_list_gcloud_bucket(bucket_id, prefix):

                fpath = urljoin(cache, gpath)
                read_gcloud_blob(bucket_id, gpath, fpath)
                self.read_repolist(fpath)

        except Exception as exc:
            logger.error("Unable to read file '{}' from gcloud".\
                         format(gpath))
            logger.exception(exc)
