""" Validating function data models 

Trying to do simple things with the data access layer to make
sure it doesn't break before doing more interesting things.
"""
from datetime import datetime
import unittest

from sqlalchemy import func
from okra.models import (DataAccessLayer, CommitMeta, CommitAuthor)

def mock_db(session):
    commit_hash = "12345"
    cm1 = CommitMeta(commit_hash=commit_hash,
                    owner_name="Tyler",
                    project_name="okra")

    ca1 = CommitAuthor(commit_hash=commit_hash,
                       author_name="Tyler",
                       author_email="this_email@email.com",
                       authored_datetime = datetime.now())
                       

    session.bulk_save_objects([cm1,ca1])
    session.commit()

class TestModels(unittest.TestCase):
    """ Verifying model behavior. """

    @classmethod
    def setUpClass(cls):
        cls.dal = DataAccessLayer('sqlite:///:memory:')
        cls.dal.connect()
        cls.dal.session = cls.dal.Session()
        mock_db(cls.dal.session)
        cls.dal.session.close()

    def setUp(self):
        self.dal.session = self.dal.Session()
        
    def tearDown(self):
        self.dal.session.rollback()
        self.dal.session.close()

    # Adding and updating objects

    def test_add_commit_meta(self):
        query = self.dal.session.query(func.count(CommitMeta.commit_hash)). \
            group_by(CommitMeta.owner_name).one()

        assert query == (1,)

    def test_add_commit_author(self):
        query = self.dal.session.query(func.count(CommitAuthor.commit_hash)).\
            group_by(CommitAuthor.author_name).one()

        assert query == (1,)

        


