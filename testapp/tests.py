from django.test import TestCase

# Create your tests here.
import random
try:
    import unittest2 as unittest
except ImportError:
    import unittest

class SimpleTest(unittest.TestCase):
    @unittest.skip("demonstrating skipping")
    def test_skipped(self):
        self.fail("shouldn't happen")

    def test_pass(self):
        self.assertEqual(10, 7 + 3)

    '''def test_fail(self):
        self.assertEqual(11, 7 + 3)'''
