""" Run redis worker. """
import logging
import time
import okra.rediswq as rediswq

import redis


logger = logging.getLogger(__name__)

#host="redis"
# Uncomment next two lines if you do not have Kube-DNS working.
# import os
# host = os.getenv("REDIS_SERVICE_HOST")

def redis_worker(job="job2", host="localhost"):
  """ Run redis worker. 

  :param job: job name <default: job2>
  :param host: host name <default: redis>
  :return: Completes specified jobs
  :rtype: void
  """
  q = rediswq.RedisWQ(name=job, host=host)

  logger.info("Worker with sessionID: {}".format(q.sessionID()))
  logger.info("Initial queue state: empty= {}".format(str(q.empty())))
  while not q.empty():
    
    item = q.lease(lease_secs=10, block=True, timeout=2)
    
    if item is not None:
      itemstr = item.decode("utf=8")
      logger.info("Working on {}".format(itemstr))
      if itemstr == "EOF":
        break
      time.sleep(10) # Put your actual work here instead of sleep.
      q.complete(item)
    else:
      logger.info("Waiting for work")
  logger.info("Queue empty, exiting")


