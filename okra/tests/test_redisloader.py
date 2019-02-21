""" Validate redis queue loading """
import unittest

import redis

from okra.redisloader import RedisLoader

class TestRedisLoader(unittest.TestCase):
    """ Redis must be running or tests will fail. """

    def setUp(self):
        self.rl = RedisLoader(name="job2", host="localhost")
        self.rd = redis.StrictRedis(host="localhost")

    def tearDown(self):
        self.rl = None
        self.rd.flushall()

    def test_load_queue(self):
        items = ["apple", "pear", "banana"]
        self.rl._load_queue(items)

        assert self.rd.llen(b"job2") == 3
        
