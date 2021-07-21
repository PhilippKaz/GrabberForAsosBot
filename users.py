import pymysql
from config import host, user, password, database


class Users():
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

    def insert_new_user(self, id_user, username, first_name, language, currency):
        with self.connection.cursor() as cursor:
            script_insert_new_user = "INSERT INTO `users`(`id_user`, `username`, `first_name`, `language`, `currency`) " \
                                     "VALUES ('%s', '%s', '%s', '%s', '%s') ON DUPLICATE KEY UPDATE username = '%s', first_name = '%s', " \
                                     "language = '%s', currency = '%s'" \
                                     % (id_user, username, first_name, language, currency, username, first_name, language, currency)
            cursor.execute(script_insert_new_user)
            self.connection.commit()

