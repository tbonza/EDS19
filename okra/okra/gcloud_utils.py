""" Utilities associated with google cloud. 

Google cloud is the supported cloud provider for
okra. 
"""
import logging

from google.cloud import storage
from google.cloud.storage import Blob
from google.cloud.exceptions import NotFound

logger = logging.getLogger(__name__)

def read_gcloud_blob(bucket_id: str, gpath: str, fpath:str):
    """ Read blob from Google Cloud Storage. 

    References:
      https://pypi.org/project/google-cloud-storage/

    :param bucket_id: id for google cloud bucket
    :param gpath: file path of item within bucket
    :param fpath: file path of item to disk
    :return: file blob from bucket
    :rtype: file
    """
    logger.info("Reading '{}' at '{}'".format(bucket_id, gpath))
    try:
        client = storage.Client()
        bucket = client.get_bucket(bucket_id)

        blob = bucket.get_blob(gpath)
    
        with open(fpath, 'wb') as outfile:
            blob.download_to_file(outfile)

        logger.info("SUCCESS -- downloaded '{}' to '{}' from '{}'".\
                    format(gpath, fpath, bucket_id))

    except NotFound:
        logger.warning("gcloud object not found: {}".format(gpath))

    except Exception as exc:
        logger.error("Unable to download '{}' to '{}' from '{}'".\
                     format(gpath, fpath, bucket_id))
        logger.exception(exc)

def write_gcloud_blob(bucket_id: str, gpath: str, fpath:str):
    """ Write blob from Google Cloud Storage.

    References:
      https://pypi.org/project/google-cloud-storage/

    :param bucket_id: id for google cloud bucket
    :param gpath: file path of item within bucket
    :param fpath: file path of item from disk
    :return: upload file blob from disk
    :rtype: None
    """
    logger.info("Writing '{}' to '{}' at '{}'".\
                format(fpath, bucket_id, gpath))
    try:
        client = storage.Client()
        bucket = client.get_bucket(bucket_id)
        blob = Blob(gpath, bucket)
        with open(fpath, 'rb') as infile:
            blob.upload_from_file(infile)
        
        logger.info("SUCCESS -- uploaded '{}' to '{}' using '{}'".\
                    format(fpath, gpath, bucket_id))

    except Exception as exc:
        logger.error("Unable to upload '{}' to '{}' using '{}'".\
                     format(fpath, gpath, bucket_id))
        logger.exception(exc)
