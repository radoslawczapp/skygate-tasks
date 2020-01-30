from django.test import TestCase
import sqlite3


class DB(object):
    def __init__(self, db_name):
        self.db_name = db_name

    def execute_query(self, query, fetch=False):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()
        cur.execute(query)
        if fetch:
            return cur.fetchall()
        conn.commit()
        conn.close()


db = DB('../db.sqlite3')
print(db.execute_query("SELECT score FROM exams_result WHERE user_id_id == (SELECT id FROM exams_user WHERE id == 1)",
                       fetch=True)[0][0])
