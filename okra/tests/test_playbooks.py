""" Validate behaviors from playbooks. 

The playbooks are the last level of abstraction before an application
is run as a pipeline. Each play in the playbook is meant to be chained
together so we can complete a task.
"""
import os
import tempfile
import unittest
from urllib.parse import urljoin

from okra.playbooks import (retrieve_or_clone)

class TestPlaybooks(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        tempfile.mkdtemp()


    def test_temp_directory_roundtrip(self):
        dirname = tempfile.gettempdir()
        fpath = urljoin(dirname, "hello.txt")

        with open(fpath, "w") as outfile:
            outfile.write("hello world\n")

        assert os.path.exists(fpath)

