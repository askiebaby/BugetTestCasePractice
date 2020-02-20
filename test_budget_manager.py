from budget_manager import BugetManager

import unittest
import os


class TestBugetSet(unittest.TestCase):
    def setUp(self):
        self.b = BugetManager('test_set.db')

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
        self.b = BugetManager('test_query.db')

    def tearDown(self):
        os.remove('test_query.db')

    def test_non_exist(self):
        self.assertEqual(self.b.query_budget('20190801', '20191031'), 0)


class TestBugetQuery2(unittest.TestCase):
    def setUp(self):
        self.b = BugetManager('test_query2.db')
        self.b.create_budget('202002', 29000)

    def tearDown(self):
        os.remove('test_query2.db')

    def test_query_full_month(self):
        self.assertEqual(self.b.query_budget('20200201', '20200229'), 29000)


class TestBugetQuery3(unittest.TestCase):
    def setUp(self):
        self.b = BugetManager('test_query3.db')
        self.b.create_budget('202002', 29000)
        self.b.create_budget('202003', 31000)

    def tearDown(self):
        os.remove('test_query3.db')

    def test_query_full_2_month(self):
        self.assertEqual(self.b.query_budget('20200201', '20200331'), 60000)


class TestBugetQuery4(unittest.TestCase):
    def setUp(self):
        self.b = BugetManager('test_query4.db')
        self.b.create_budget('202003', 31000)

    def tearDown(self):
        os.remove('test_query4.db')

    def test_query_one_day(self):
        self.assertEqual(self.b.query_budget('20200301', '20200301'), 1000)


class TestBugetQuery5(unittest.TestCase):
    def setUp(self):
        self.b = BugetManager('test_query5.db')
        self.b.create_budget('202001', 31000)
        self.b.create_budget('202002', 29)

    def tearDown(self):
        os.remove('test_query5.db')

    def test_query_partial_cross_month(self):
        self.assertEqual(self.b.query_budget('20200131', '20200202'), 1002)


class TestBugetQuery6(unittest.TestCase):
    def setUp(self):
        self.b = BugetManager('test_query6.db')
        self.b.create_budget('202001', 31000)
        self.b.create_budget('202002', 29)
        self.b.create_budget('202003', 62000)

    def tearDown(self):
        os.remove('test_query6.db')

    def test_query_partial_cross_3_month(self):
        self.assertEqual(self.b.query_budget('20200131', '20200301'), 3029)


class TestBugetQuery7(unittest.TestCase):
    def setUp(self):
        self.b = BugetManager('test_query7.db')
        self.b.create_budget('201912', 62000)
        self.b.create_budget('202001', 31000)
        self.b.create_budget('202002', 29)

    def tearDown(self):
        os.remove('test_query7.db')

    def test_query_partial_cross_year(self):
        self.assertEqual(self.b.query_budget('20191231', '20200101'), 3000)


class TestBugetQuery8(unittest.TestCase):
    def setUp(self):
        self.b = BugetManager('test_query8.db')
        self.b.create_budget('201912', 62000)
        self.b.create_budget('202001', 31000)
        self.b.create_budget('202002', 29)

    def tearDown(self):
        os.remove('test_query8.db')

    def test_query_not_exist(self):
        self.assertEqual(self.b.query_budget('20000101', '20000102'), 0)
