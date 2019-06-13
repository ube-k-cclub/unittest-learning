from unittest import TestCase
from nose.tools import ok_, eq_
import funcs as f

class FuncsTestCase(TestCase):
    def setUp(self):
        print("Starting tests...")
    
    def tearDown(self):
        print("Finished tests!")

    def test_add(self):
        eq_(f.add(1, 2), 3)
        eq_(f.add(5, 10), 15)
        eq_(f.add(-1, 1), 0)

    def test_is_even(self):
        ok_(f.is_even(2))
        ok_(not f.is_even(3))
