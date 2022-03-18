import sqlite3

class FilesWrapper:
    def __init__(self, db_file):
        self._db_file = db_file
        self._conn = sqlite3.connect(self._db_file)

    def add_file(self, filename):
        cur = self._conn.cursor()

        sql_stmt = '''
            INSERT INTO files (name)
            VALUES (?)
        '''

        cur.execute(sql_stmt, (filename,))
        self._conn.commit()

    
    def get_files(self):
        cur = self._conn.cursor()

        sql_stmt = "SELECT name FROM files;"
        cur.execute(sql_stmt)

        result = cur.fetchall()

        return result