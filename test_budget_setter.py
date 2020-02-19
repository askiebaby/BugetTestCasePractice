from budget_setter import BugetSetter

import unittest
import os

class TestBugetSetter(unittest.TestCase):
    def setUp(self):
        self.b = BugetSetter('test.db')
    
    def tearDown(self):
        os.remove('test.db')

    def test_insert(self):
        date = '202002'
        self.assertFalse(self.b.check_date_exist(date))

        self.b.create_budget(date, 1000)
        self.assertTrue(self.b.check_date_exist(date))
        self.assertEqual(self.b.get_budget(date), (date, 1000))

        self.b.update_budget(date, 2000)
        self.assertEqual(self.b.get_budget(date), (date, 2000))