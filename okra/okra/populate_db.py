""" Populate SQL database. 

References:
  https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
"""
import itertools
import logging
from urllib.parse import urljoin

from okra.models import DataAccessLayer, Inventory
from okra.github import repo_to_objects                         

logger = logging.getLogger(__name__)


def insert_buffer(items: iter, dal, invobj, buffer_size=1024):
    """ Insert items using a buffer. 

    :param items: sqlalchemy orm database objects
    :param dal: okra.models.DataAccessLayer
    :param invobj: okra.models.Inventory object, to be updated
    :buffer_size: number of items to add before committing a session
    """
    logger.info("STARTED insert buffer")
    count = 0
    for item in items:

        dal.session.add(item)

        if count % buffer_size == 0:
            try:
                dal.session.commit()
                logger.info("Committed db objects: {}".format(count))

            except Exception as exc:
                dal.session.rollback()
                logger.error("Rolled back session")
                logger.exception(exc)
                raise exc

        count += 1

    # update inventory
    invobj.last_commit = item.commit_hash
    dal.session.add(invobj)

    try:
        dal.session.commit()
        logger.info("Committed db objects: {}".format(count))

    except Exception as exc:
        dal.session.rollback()
        logger.error("Rolled back session")
        logger.exception(exc)
        raise exc

    logger.info("COMPLETED insert buffer")

def populate_db(dburl: str, dirpath: str, repolist:list, buffer_size=1024):
    """ Populate a new or existing database. """

    # Initialize data access layer
    
    dal = DataAccessLayer(dburl)
    dal.connect()
    dal.session = dal.Session()

    for repo_name in repolist:
        
        # TODO: check if repo exists, last commit
        owner, project = repo_name.split("/")
        invobj = dal.session.query(
            Inventory.project_name, Inventory.owner_name,
            Inventory.last_commit).first() # unique value

        invobj.owner_name = owner
        invobj.project_name = project
        print(invobj.last_commit)

        rpath = urljoin(dirpath, repo_name)
        objs = repo_to_objects(repo_name, dirpath, invobj.last_commit)

        insert_buffer(objs, dal, invobj, buffer_size)

    
