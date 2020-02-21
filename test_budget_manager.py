from budget_manager import BudgetManager

import unittest
import os


class TestBugetSet(unittest.TestCase):
    def setUp(self):
        self.b = BudgetManager('test_set.db')

    def tearDown(self):
        os.remove('test_set.db')

    def test_insert(self):
        date = '202002'
        self.assertFalse(self.b.check_date_exist(date))

        self.b.create_budget(date, 1000)
        self.assertTrue(self.b.check_date_exist(date))
        self.assertEqual(self.b.get_budget(date), (date, 1000))

        self.b.update_budget(date, 2000)
        self.assertEqual(self.b.get_budget(date), (date, 2000))


class TestBugetQuery(unittest.TestCase):
    def setUp(self):
        self.b = BudgetManager('test_query.db')

    def tearDown(self):
        os.remove('test_query.db')

    def test_non_exist(self):
        self.assertEqual(self.b.query_budget('20190801', '20191031'), 0)

    def test_query_not_exist_2(self):
        self.b.create_budget('201912', 62000)
        self.b.create_budget('202001', 31000)
        self.b.create_budget('202002', 29)
        self.assertEqual(self.b.query_budget('20000101', '20000102'), 0)

    def test_query_full_1_month(self):
        self.b.create_budget('202002', 29000)
        self.assertEqual(self.b.query_budget('20200201', '20200229'), 29000)

    def test_query_full_2_month(self):
        self.b.create_budget('202002', 29000)
        self.b.create_budget('202003', 31000)
        self.assertEqual(self.b.query_budget('20200201', '20200331'), 60000)

    def test_query_one_day(self):
        self.b.create_budget('202003', 31000)
        self.assertEqual(self.b.query_budget('20200301', '20200301'), 1000)

    def test_query_partial_cross_month(self):
        self.b.create_budget('202001', 31000)
        self.b.create_budget('202002', 29)
        self.assertEqual(self.b.query_budget('20200131', '20200202'), 1002)

    def test_query_partial_cross_3_month(self):
        self.b.create_budget('202001', 31000)
        self.b.create_budget('202002', 29)
        self.b.create_budget('202003', 62000)
        self.assertEqual(self.b.query_budget('20200131', '20200301'), 3029)

    def test_query_partial_cross_year(self):
        self.b.create_budget('201912', 62000)
        self.b.create_budget('202001', 31000)
        self.b.create_budget('202002', 29)
        self.assertEqual(self.b.query_budget('20191231', '20200101'), 3000)
