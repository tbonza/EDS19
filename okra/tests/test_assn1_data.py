""" Validate assignment 1 data processing. """
import os
import shutil
import tempfile
import unittest
from urllib.parse import urljoin

from okra.assn1_data import (parse_file_format, parse_commits, parse_messages)
from okra.playbooks import retrieve_or_clone

class TestAssn1Data(unittest.TestCase):

    repo_name = "tbonza/tiny_dancer"

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

    def test_parse_commits(self):

        print(self.tmpdir.name)
        print(self.repo_path)
        
        results = [i for i in parse_commits(self.repo_path)]
        
        assert len(results) == 3

        r = results[0]

        assert r.hash_val == 'ed4dd8e797db7d6c1ce23980c24d94228d66b1d6'
        assert r.author == 'tbonza'
        assert r.author_email == 'tylers.pile@gmail.com'
        assert r.author_timestamp == '2019-02-26T09:55:26-05:00'
        assert r.committer == 'tbonza'
        assert r.committer_email == 'tylers.pile@gmail.com'
        assert r.committer_timestamp == '2019-02-26T09:55:26-05:00'

    def test_new_parse_commits(self):
        """ Parse from last commit """
        pass

    def test_parse_messages(self):
        pass

    def test_parse_file_format_single_file(self):

        pass
    
    def test_parse_file_format_two_files(self):

        pass

    def test_parse_file_format_many_files(self):
        pass

        
