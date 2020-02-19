import sqlite3

class BugetSetter(object):
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