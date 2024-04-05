import unittest
from tests.test_utils import *

class TestPostgreSQL(unittest.TestCase):

    def test_can_connect(self):
        version = get_rest_call(self, 'http://127.0.0.1:5000/manage/version')
        self.assertTrue(version[0].startswith('PostgreSQL'))