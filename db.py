import sqlite3
import os.path


def check_value(value):
    """
    This function add ' before and after value, if value type is str and return 'value'.
    If incoming value type is int, function return given value.
    """
    if type(value) != int:
        value = '\'' + value + '\''
        return value
    return value


def add_data_article(table, value):
    success = False, 'error'
    try:
        db = sqlite3.connect('learning.db')
        c = db.cursor()
        record_tuple = (value['full_text'], value['field'], value['question'],)
        mysql_query = f"INSERT INTO {table} VALUES (?, ?, ?)"

        c.execute(mysql_query, record_tuple)
        db.commit()
        c.close()
        success = True, ''
    except sqlite3.Error as error:
        print("Error while working with SQLite", error)
        success = False, error
    finally:
        if db:
            db.close()
            return success


def add_data_user(table, value):
    try:
        db = sqlite3.connect('learning.db')
        c = db.cursor()
        record_tuple = (value['article_id'], value['counter'], value['next_show'],)
        mysql_query = f"INSERT INTO {table} VALUES (?, ?, ?)"

        c.execute(mysql_query, record_tuple)
        db.commit()
        c.close()
    except sqlite3.Error as error:
        print("Error while working with SQLite", error)
    finally:
        if db:
            db.close()


def update_data(table, request_dict, condition):
    result = (False, 'Error')
    try:
        db = sqlite3.connect('learning.db')
        c = db.cursor()
        request_str_1 = f"UPDATE {table} SET "
        request_str_2 = ''
        for key in request_dict:
            request_str_2 += key + '=' + str(check_value(request_dict[key])) + ','
        request_str_2 = request_str_2[:-1] + ' '
        request_str_3 = f" WHERE {condition[0]}={check_value(condition[1])}"
        c.execute(request_str_1 + request_str_2 + request_str_3)
        db.commit()
        c.close()
        result = (True, '')
    except sqlite3.Error as error:
        print("Error while working with SQLite", error)
        result = (False, error)
    finally:
        if db:
            db.close()
            return result


def select_data(table):
    returned = None
    try:
        db = sqlite3.connect('learning.db')
        c = db.cursor()
        c.execute(f"SELECT rowid, * FROM {table}")
        returned = c.fetchall()
        c.close()
    except sqlite3.Error as error:
        print("Error while working with SQLite", error)
    finally:
        if db:
            db.close()
    return returned


def delete_data(table, condition):
    try:
        db = sqlite3.connect('learning.db')
        c = db.cursor()
        c.execute(f"DELETE FROM {table} WHERE {condition[0]}={condition[1]};")
        db.commit()
        c.close()
        result = (True, '')
    except sqlite3.Error as error:
        print("Error while working with SQLite", error)
        result = (False, error)
    finally:
        if db:
            db.close()
            return result


def get_data(table, condition):
    returned = None
    try:
        db = sqlite3.connect('learning.db')
        c = db.cursor()
        c.execute(f"SELECT * FROM {table} WHERE {condition[0]}={check_value(condition[1])}")
        returned = c.fetchone()
        c.close()
    except sqlite3.Error as error:
        print("Error while working with SQLite", error)
    finally:
        if db:
            db.close()
    return returned


class Database:

    def __init__(self):
        if not os.path.exists('learning.db'):
            self.create_table()
        else:
            self.db = sqlite3.connect('learning.db')
            self.c = self.db.cursor()

    def create_table(self):
        self.db = sqlite3.connect('learning.db')
        self.c = self.db.cursor()
        self.c.execute(""" CREATE TABLE article (
                    full_text TEXT,
                    field TEXT,
                    question TEXT
                    )""")
        self.c.execute(""" CREATE TABLE user (
                            article_id INTEGER UNIQUE,
                            counter INTEGER,
                            next_show timestamp
                            )""")
        self.db.commit()
        self.c.close()
        if self.db:
            self.db.close()
