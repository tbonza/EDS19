""" Populate SQL database. 

References:
  https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
"""
import logging
from urllib.parse import urljoin

from okra.models import DataAccessLayer
from okra.github import repo_to_objects                         

logger = logging.getLogger(__name__)


def insert_buffer(items: iter, session, buffer_size=1024):
    """ Insert items using a buffer. 

    :param items: sqlalchemy orm database objects
    :param session: DataAccessLayer.Session instance
    :buffer_size: number of items to add before committing a session
    """
    logger.info("STARTED insert buffer")
    count = 0
    for item in items:

        session.add(item)

        if count % buffer_size == 0:
            try:
                session.commit()
                logger.info("Committed db objects: {}".format(count))

            except Exception as exc:
                session.rollback()
                logger.error("Rolled back session")
                logger.exception(exc)
                raise exc

        count += 1

    try:
        session.commit()
        logger.info("Committed db objects: {}".format(count))

    except Exception as exc:
        session.rollback()
        logger.error("Rolled back session")
        logger.exception(exc)
        raise exc

    logger.info("COMPLETED insert buffer")

def populate_db(dburl: str, dirpath: str, repolist:list, buffer_size=1024):
    """ Populate a new or existing database. """

    # Initialize data access layer
    
    dal = DataAccessLayer(dburl)
    dal.connect()
    session = dal.Session()

    for repo_name in repolist:
        
        # TODO: check if repo exists, last commit

        rpath = urljoin(dirpath, repo_name)
        objs = repo_to_objects(repo_name, dirpath)

        if type(objs) != None:
            insert_buffer(objs, session, buffer_size)

    
