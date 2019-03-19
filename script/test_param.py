import unittest
from parameterized import parameterized

def add(x, y):
    return x+y

def build_data():
    return [(1, 1, 2), (0, 1, 1), (0, 0, 0)]


class TestAdd(unittest.TestCase):
    @parameterized.expand(build_data)
    def test_add(self, x, y, expect):
       result = add(x, y)
       self.assertEqual(expect, result)