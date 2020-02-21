import sqlite3
from datetime import datetime, timedelta
from calendar import monthrange


class BudgetManager(object):
    STATUS_CODE_CREATED = 0
    STATUS_CODE_UPDATED = 1

    def __init__(self, db_path='my.db'):
        self._db_path = db_path
        conn = sqlite3.connect(self._db_path)
        conn.execute('''
            CREATE TABLE IF NOT EXISTS BUDGET
            (DATE TEXT PRIMARY KEY     NOT NULL,
            AMOUNT           INT    NOT NULL
                );''')

    def check_date_exist(self, date):
        with sqlite3.connect(self._db_path) as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM BUDGET WHERE DATE=:DATE", {"DATE": date})
            return bool(cur.fetchone())

    def create_budget(self, date, amount):
        with sqlite3.connect(self._db_path) as con:
            cur = con.cursor()
            cur.execute("INSERT INTO BUDGET (DATE, AMOUNT) VALUES (?,?)", (date, amount))
            con.commit()

    def update_budget(self, date, amount):
        with sqlite3.connect(self._db_path) as con:
            cur = con.cursor()
            cur.execute("UPDATE BUDGET SET AMOUNT=? WHERE DATE=?", (amount, date))
            con.commit()

    def get_budget(self, date):
        with sqlite3.connect(self._db_path) as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM BUDGET WHERE DATE=:DATE", {"DATE": date})
            return cur.fetchone()

    def fetch_all(self):
        with sqlite3.connect(self._db_path) as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM BUDGET")
            return cur.fetchall()

    def query_budget(self, start_date, end_date):

        amount_list = self.fetch_all()
        if not amount_list:
            return 0

        amount_table = dict()  # datetime: YYMM -> amount
        for t in amount_list:
            amount_table[t[0]] = t[1]

        start_dt = datetime.strptime(start_date, '%Y%m%d')
        end_dt = datetime.strptime(end_date, '%Y%m%d')

        d = start_dt
        total_amount = 0
        while d <= end_dt:
            amount = amount_table.get(d.strftime('%Y%m'), 0)
            amount_per_day = amount / self.month_day(d.year, d.month)
            total_amount += amount_per_day
            d += timedelta(days=1)

        return total_amount

    def month_day(self, year, month):
        return monthrange(year, month)[1]
