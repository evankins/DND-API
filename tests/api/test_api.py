import unittest
from tests.test_utils import *


class TestExample(unittest.TestCase):

    def setUp(self):  
        """Initialize DB using API call"""
        post_rest_call(self, 'http://127.0.0.1:5000/manage/init')
        print("DB Should be reset now")