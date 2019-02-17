""" Validating data models using in Assignment 4

Mocking up a GitHub project then testing that the computation
works. 
"""
from datetime import datetime
import unittest

from okra.models import (DataAccessLayer, Meta, Author, Contrib,
                         CommitFile, Info)
from okra.assn4 import (total_number_of_files_by_project,
                        author_file_owned,
                        get_truck_factor_by_project)

def mock_github_project_db(session):
    """ 
    Mock up a database that can be used to compute the truck factor
    of a project.
    """

    meta_commits = [
        Meta(commit_hash="1", owner_name="Tyler", project_name="okra"),
        Meta(commit_hash="2", owner_name="Tyler", project_name="okra"),
        Meta(commit_hash="3", owner_name="Tyler", project_name="okra"),
        Meta(commit_hash="4", owner_name="Tyler", project_name="okra"),
        Meta(commit_hash="5", owner_name="Tyler", project_name="okra"),
    ]
    
    session.bulk_save_objects(meta_commits)
    session.commit()

    author_commits = [
        Author(commit_hash="1", name="Tyler", authored=datetime.now()),
        Author(commit_hash="2", name="Tyler", authored=datetime.now()),
        Author(commit_hash="3", name="Chaitya", authored=datetime.now()),
        Author(commit_hash="4", name="Angela", authored=datetime.now()),
        Author(commit_hash="5", name="Chris", authored=datetime.now()),
    ]

    session.bulk_save_objects(author_commits)
    session.commit()

    contrib_commits = [
        Contrib(1, "1", "Tyler", contributed=datetime.now()),
        Contrib(2, "1", "Diego", contributed=datetime.now()),
        Contrib(3, "2", "Tyler", contributed=datetime.now()),
        Contrib(4, "3", "Chaitya", contributed=datetime.now()),
        Contrib(5, "4", "Angela", contributed=datetime.now()),
        Contrib(6, "5", "Chris", contributed=datetime.now()),
    ] # note that truck factor will exclude multiple contributors

    session.bulk_save_objects(contrib_commits)
    session.commit()

    commit_files = [
    ]

class TestModels(unittest.TestCase):
    """ Verifying model behavior. """

    @classmethod
    def setUpClass(cls):
        cls.dal = DataAccessLayer('sqlite:///:memory:')
        cls.dal.connect()
        cls.dal.session = cls.dal.Session()
        mock_github_project_db(cls.dal.session)
        cls.dal.session.close()

    def setUp(self):
        self.dal.session = self.dal.Session()
        
    def tearDown(self):
        self.dal.session.rollback()
        self.dal.session.close()

    # Adding and updating objects

    def test_add_commit_meta(self):
        pass


    
