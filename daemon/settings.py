import sys
import psycopg2

class DBManager:
    _hostname = "localhost"
    _database = "icanhazinternet"
    _username = "postgres"
    _password = ""
    _port = 5432
    _conn = None

    def _createDBConnection(self):
        try:
            connect_str = "dbname='{}' user='{}' host='{}' password='{}'".format(self._database, self._username, self._hostname, self._password)
            self._conn = psycopg2.connect(connect_str)
        except Exception as e:
            print(e, file=sys.stderr)

    def executeQuery(self, queryString):
        if self._conn == None:
            self._createDBConnection()
        cursor = self._conn.cursor()
        cursor.execute(queryString)
        return cursor.fetchall()

a = DBManager()
a.executeQuery("SELECT * FROM visited_sites")
