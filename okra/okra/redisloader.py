""" Load redis queue. 

Based on the redis work queue.

Reference:
https://kubernetes.io/docs/tasks/job/fine-parallel-processing-work-queue/
"""
import logging
import uuid

import redis


logger = logging.getLogger(__name__)

class RedisLoader(object):

    reference = 100

    def __init__(self, name, **redis_kwargs):
        self._db = redis.StrictRedis(**redis_kwargs)
        self._main_q_key = name
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
                self._db.set(self._main_q_key, item)

                if count % self.reference == 0:
                    logger.info("Loaded {} items in queue '{}'".\
                                format(self._main_q_key))
                count += 1

            logger.info("Loaded {} items in queue '{}'".\
                        format(self._main_q_key))
            logger.info("FINISHED loading data in queue '{}'".\
                        format(self._main_q_key))

        except Exception as exc:
            logger.error("Failed to finish loading queue '{}'".\
                         format(self._main_q_key))
            logger.exception(exc)

                

    def read_repolist(self, fpath):
        """ Read the 'GitHub repo list' format and load queue.

        :param fpath: str, file path to repo list text file
        :return: loaded redis queue
        :rtype: None
        """
        try:
            with open(fpath, "r") as infile:
                data = [i.strip() for i in infile.splitlines()]

            logger.info("Retrieved file '{}', loading queue '{}'".\
                        format(fpath, self.name))
            self._load_queue(data)

        except Exception as exc:
            logger.error("Unable to read file '{}'".format(fpath))
            logger.exception(exc)

            
