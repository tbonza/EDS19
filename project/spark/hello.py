"""
Testing out a basic example
"""
import logging

from pyspark import SparkContext


logger = logging.getLogger(__name__)

def enable_cloud_log():
    """ Enable logs using default StreamHandler """
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)s %(message)s')


if __name__ == "__main__":

    enable_cloud_log()
    sc = SparkContext(appName='helloWorld')
    logger.info("Hello world")
    sc.stop()
