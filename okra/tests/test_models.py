""" Validating function data models 

Trying to do simple things with the data access layer to make
sure it doesn't break before doing more interesting things.
"""
from datetime import datetime
import unittest

from sqlalchemy import func
from okra.models import (DataAccessLayer, Meta, Author,
                         Contrib, CommitFile)

def mock_db(session):
    commit_hash = "12345"
    cm1 = Meta(commit_hash=commit_hash,
                    owner_name="Tyler",
                    project_name="okra")

    ca1 = Author(commit_hash=commit_hash,
                 name="Tyler",
                 email="this_email@email.com",
                 authored = datetime.now())

    cc1 = Contrib(contrib_id = 1,
                  commit_hash=commit_hash,
                  name="Tyler",
                  email=None,
                  contributed=datetime.now())

    cc2 = Contrib(contrib_id = 2,
                  commit_hash=commit_hash,
                  name="Angela",
                  email="angela@email.com",
                  contributed=datetime.now())

    #cf1 = CommitFile
                       

    session.bulk_save_objects([cm1,ca1,cc1,cc2])
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
        query = self.dal.session.query(func.count(Meta.commit_hash)). \
            group_by(Meta.owner_name).one()

        assert query == (1,)

    def test_add_commit_author(self):
        query = self.dal.session.query(func.count(Author.commit_hash)).\
            group_by(Author.name).one()

        assert query == (1,)

    def test_add_commit_contrib(self):
        query = self.dal.session.\
            query(func.count(Contrib.commit_hash)).\
            group_by(Contrib.commit_hash).one()

        assert query == (2,)

        


