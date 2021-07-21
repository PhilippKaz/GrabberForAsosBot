import pymysql
from config import host, user, password, database


class Currency():
    def __init__(self):
        try:
            self.connection = pymysql.connect(host=host,
                                              port=3307,
                                              user=user,
                                              password=password,
                                              database=database,
                                              cursorclass=pymysql.cursors.DictCursor)
        except Exception:
            pass

    def get_list_currency(self):
        pass
