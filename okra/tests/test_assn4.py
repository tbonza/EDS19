""" Validating data models using in Assignment 4


"""
import unittest

from okra.models import DataAccessLayer, CommitMeta
from okra.assn4 import get_truck_factor_by_project

def mock_db(session):
    c1 = CommitMeta(commit_hash="12345",
                    owner_name="Tyler",
                    project_name="okra")

    session.bulk_save_objects([c1])
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
        pass


    
