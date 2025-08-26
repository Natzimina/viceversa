# reverseapp/tests/test_utils.py
import unittest
from reverseapp.utils import reverse_string

class ReverseTests(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(reverse_string("abc"), "cba")