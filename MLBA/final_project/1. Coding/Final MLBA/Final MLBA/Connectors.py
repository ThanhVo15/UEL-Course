import mysql.connector
import traceback
import pandas as pd

class Connector:
    def __init__(self, server=None, port=None, database=None, username=None, password=None):
        self.server = server
        self.port = port
        self.database = database
        self.username = username
        self.password = password
        self.conn = None

    def connect(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.server,
                port=self.port,
                database=self.database,
                user=self.username,
                password=self.password)
            return self.conn
        except:
            self.conn = None
            traceback.print_exc()
        return None

    def disConnect(self):
        if self.conn is not None:
            self.conn.close()

    def queryDataset(self, sql, params=None):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, params)
            df = pd.DataFrame(cursor.fetchall())
            if not df.empty:
                df.columns = cursor.column_names
            return df
        except:
            traceback.print_exc()
        return None

    def executeNonQuery(self, sql, params=None):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, params)
            self.conn.commit()
            return True
        except:
            traceback.print_exc()
            return False

    def getTablesName(self):
        cursor = self.conn.cursor()
        cursor.execute("SHOW TABLES;")
        results = cursor.fetchall()
        tablesName = []
        for item in results:
            tablesName.append([tableName for tableName in item][0])
        return tablesName