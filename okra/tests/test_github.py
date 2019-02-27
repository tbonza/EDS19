""" Validate log parsing to database model objects conversion. """
import os
import shutil
import tempfile
import unittest
from urllib.parse import urljoin

from okra.github import repo_to_objects
from okra.playbooks import retrieve_or_clone

class TestGithub(unittest.TestCase):

    repo_name = "tbonza/tiny_dancer"
    total_commits = 4

    @classmethod
    def setUpClass(cls):
        cls.tmpdir = tempfile.TemporaryDirectory()
        cls.repo_path = urljoin(cls.tmpdir.name, cls.repo_name)

    @classmethod
    def tearDownClass(cls):

        cls.tmpdir.cleanup()
        if os.path.exists(cls.tmpdir.name):
            shutil.rmtree(cls.tmpdir.name)

        #if os.path.exists(cls.repo_path):
        #    shutil.rmtree(cls.repo_path)
        # caching repo path for time being, faster tests, less network

    def setUp(self):
        retrieve_or_clone(self.repo_name, self.tmpdir.name)

    def test_repo_to_objects_last_commit(self):
        last_commit = "ed4dd8e797db7d6c1ce23980c24d94228d66b1d6"

        results = [i for i in repo_to_objects(self.repo_name,
                                              self.tmpdir.name,
                                              last_commit=last_commit)]

        assert len(results) == 6


