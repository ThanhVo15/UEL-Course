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
            return True
        except mysql.connector.Error as err:
            self.conn = None
            traceback.print_exc()
            print(f"Error: {err}")
            return False

    def disconnect(self):
        if self.conn:
            self.conn.close()

    def queryDataset(self, sql):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            df = pd.DataFrame(cursor.fetchall())
            if not df.empty:
                df.columns = cursor.column_names
            return df
        except:
            traceback.print_exc()
        return None

    def getTablesName(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SHOW TABLES;")
            results = cursor.fetchall()
            tablesName = [item[0] for item in results]
            return tablesName
        except:
            traceback.print_exc()
        return None
