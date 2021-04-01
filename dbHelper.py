"""
    This file is to assist the flask application with reading and writing the database.
    It will increase the readability of the flask file.
"""

import sqlite3
from sqlite3 import Error


class Main:
    """
        This main class of the database helper is:
            - to execute all types of queries
            - read a table in the database
            - delete an entry in a table in the database
    """

    def execute_query(self, query_list, commit=False, fetchAll=False, fetchOne=False):
        try:
            conn = sqlite3.connect("comments.db")
            c = conn.cursor()
            result = None
            if type(query_list) == str:
                c.execute(query_list)
            elif isinstance(query_list, tuple):
                c.execute(query_list[0], query_list[1])
            else:
                for query in query_list:
                    if isinstance(query, tuple):
                        c.execute(query[0], query[1])
                    else:
                        c.execute(query)
            if commit:
                conn.commit()
            if fetchAll:
                result = [row for row in c.fetchall()]
            if fetchOne:
                result = c.fetchone()
            c.close()
            conn.close()
            return result

        except Error as e:
            print(e)

    def read_database(self, db_name):
        return self.execute_query(query_list=f"SELECT * FROM {db_name}", fetchAll=True)

    def read_columns(self, db_name):
        data = self.execute_query(query_list=f"PRAGMA table_info({db_name})", fetchAll=True)
        return [x[1] for x in data]

    def del_comment(self, id, db_name):
        self.execute_query(query_list=f'DELETE FROM {db_name} WHERE id = {id}', commit=True)


class Comment(Main):
    """
        This child class is to add and delete comments in the comments table.
    """

    def __init__(self, comment_arg, type_arg, written_arg, math_arg, programming_arg, grade_of_excellence_arg):
        self.comment = comment_arg
        self.type_comment = type_arg
        self.written = written_arg
        self.math = math_arg
        self.programming = programming_arg
        self.grade_of_excellence = grade_of_excellence_arg

    def to_string(self):
        return f"{self.comment}, {self.type_comment}, {int(self.written)}, {int(self.math)}, {int(self.programming)}, {self.grade_of_excellence}."

    def add_comment(self):
        query1 = """CREATE TABLE IF NOT EXISTS comments (id INTEGER PRIMARY KEY AUTOINCREMENT, comment TEXT NOT NULL, type_comment TEXT NOT NULL, written INTEGER NOT NULL, math INTEGER NOT NULL, programming INTEGER NOT NULL, grade_of_excellence TEXT NOT NULL)"""
        query2 = "INSERT INTO comments (comment, type_comment, written, math, programming, grade_of_excellence) VALUES (?,?,?,?,?,?)", (
            self.comment, self.type_comment, int(self.written), int(self.math), int(self.programming),
            self.grade_of_excellence)
        self.execute_query(query_list=[query1, query2], commit=True)

    def update_comment(self, id):
        self.execute_query(query_list=[('UPDATE comments SET comment = ? WHERE id = ?', (self.comment, id))],
                           commit=True)
        self.execute_query(query_list=[('UPDATE comments SET type_comment = ? WHERE id = ?', (self.type_comment, id))],
                           commit=True)
        self.execute_query(query_list=[('UPDATE comments SET written = ? WHERE id = ?', (self.written, id))],
                           commit=True)
        self.execute_query(query_list=[('UPDATE comments SET math = ? WHERE id = ?', (self.math, id))], commit=True)
        self.execute_query(query_list=[('UPDATE comments SET programming = ? WHERE id = ?', (self.programming, id))],
                           commit=True)
        self.execute_query(
            query_list=[('UPDATE comments SET grade_of_excellence = ? WHERE id = ?', (self.grade_of_excellence, id))],
            commit=True)


class Requirements(Main):
    """
        This child class is to add and delete requirements in the requirements table.
    """

    def __init__(self, requirement_arg, best_arg, good_arg, bad_arg, worst_arg, written_arg, programming_arg, math_arg,
                 type_arg):
        self.requirement = requirement_arg
        self.best = best_arg
        self.good = good_arg
        self.bad = bad_arg
        self.worst = worst_arg
        self.written = written_arg
        self.programming = programming_arg
        self.math = math_arg
        self.template_type = type_arg

    def add_requirement(self):
        query1 = """CREATE TABLE IF NOT EXISTS requirements (id INTEGER PRIMARY KEY AUTOINCREMENT, requirement TEXT NOT NULL, best TEXT NOT NULL, good TEXT NOT NULL, bad TEXT NOT NULL, worst TEXT NOT NULL, written INTEGER NOT NULL, math INTEGER NOT NULL, programming INTEGER NOT NULL, type TEXT NOT NULL)"""
        query2 = "INSERT INTO requirements (requirement, best, good, bad, worst, written, math, programming, type) VALUES (?,?,?,?,?,?,?,?,?)", (
            self.requirement, self.best, self.good, self.bad, self.worst, int(self.written), int(self.math),
            int(self.programming), self.template_type)
        self.execute_query(query_list=[query1, query2], commit=True)

    def update_requirement(self, id):
        self.execute_query(
            query_list=[('UPDATE requirements SET requirement = ? WHERE id = ?', (self.requirement, id))], commit=True)
        self.execute_query(query_list=[('UPDATE requirements SET best = ? WHERE id = ?', (self.best, id))], commit=True)
        self.execute_query(query_list=[('UPDATE requirements SET good = ? WHERE id = ?', (self.good, id))], commit=True)
        self.execute_query(query_list=[('UPDATE requirements SET bad = ? WHERE id = ?', (self.bad, id))], commit=True)
        self.execute_query(query_list=[('UPDATE requirements SET worst = ? WHERE id = ?', (self.worst, id))],
                           commit=True)
        self.execute_query(query_list=[('UPDATE requirements SET written = ? WHERE id = ?', (self.written, id))],
                           commit=True)
        self.execute_query(query_list=[('UPDATE requirements SET math = ? WHERE id = ?', (self.math, id))], commit=True)
        self.execute_query(
            query_list=[('UPDATE requirements SET programming = ? WHERE id = ?', (self.programming, id))], commit=True)
        self.execute_query(query_list=[('UPDATE requirements SET type = ? WHERE id = ?', (self.template_type, id))],
                           commit=True)
