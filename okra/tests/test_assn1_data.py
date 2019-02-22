""" Validate assignment 1 data processing. """
import unittest

from okra.assn1_data import parse_file_format

FILE_INFO = b"""
^|^
48998029e313b9206daa2d49f55aeb810242361e

6       4       tensorflow/lite/experimental/micro/README.md
^|^
4f1b0ee65a652743ede11d95a33513588ba7f772

26      12      tensorflow/python/keras/engine/training_arrays.py
^|^
eb17145a7e8f8d50418d0238e8dbd445ea2bd1d7

14      1       tensorflow/lite/models/speech_test.cc
36      54      tensorflow/lite/models/testdata/g3doc/README.md
^|^
329bd829d234165d235d2a7d47c3b2d8c8ca114f

4       4       tensorflow/lite/experimental/micro/README.md
^|^
12e86468e2a9b57e636c1d0afcdf3f657f6df0b6

1       1       tensorflow/python/compat/compat.py
^|^
d28aabb83228524df1b906c66b35bdb5657a59b5

262     0       tensorflow/compiler/xla/service/algebraic_simplifier.cc
80      0       tensorflow/compiler/xla/service/algebraic_simplifier_test.cc
7       10      tensorflow/compiler/xla/service/gather_expander.cc
6       6       tensorflow/compiler/xla/service/hlo_creation_utils.cc
6       6       tensorflow/compiler/xla/service/hlo_creation_utils.h
4       6       tensorflow/compiler/xla/service/hlo_creation_utils_test.cc
4       6       tensorflow/compiler/xla/service/scatter_expander.cc
^|^
f52351444551016d7dd949a5aa599da489a97045

1       1       tensorflow/python/compat/compat.py
"""

class TestAssn1Data(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_parse_file_format_single_file(self):

        # added, deleted

        result = next(parse_file_format(FILE_INFO))
        assert result.hash_val == \
            "48998029e313b9206daa2d49f55aeb810242361e"
        assert result.file_path == \
            "tensorflow/lite/experimental/micro/README.md"
        assert result.added == '6'
        assert result.deleted == '4'

    def test_parse_file_format_two_files(self):
        results = [i for i in parse_file_format(FILE_INFO)][2:4]
        r1 = results[0]
        r2 = results[1]
        hash_val = "eb17145a7e8f8d50418d0238e8dbd445ea2bd1d7"

        assert r1.hash_val == hash_val
        assert r2.hash_val == hash_val

    def test_parse_file_format_many_files(self):
        pass

        
