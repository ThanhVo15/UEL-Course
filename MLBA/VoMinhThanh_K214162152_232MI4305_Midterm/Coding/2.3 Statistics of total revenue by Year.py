from flask import Flask
from flask_mysqldb import MySQL
import pandas as pd

mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '@Obama123'
app.config['MYSQL_DB'] = 'retails'

mysql.init_app(app)

def queryDataset(sql):
    try:
        with app.app_context():
            cursor = mysql.connection.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            df = pd.DataFrame(results)
            return df
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == '__main__':
    with app.app_context():
        sql = "SELECT SUBSTRING_INDEX(SUBSTRING_INDEX(o.OrderDate, '/', -1), '/', 1) AS OrderYear, SUM(od.OrderQty * od.UnitPrice) AS TotalRevenue " \
            "FROM orders o " \
            "JOIN orderdetails od ON o.OrderId = od.OrderId " \
            "GROUP BY OrderYear " \
            "ORDER BY OrderYear;"

        df = queryDataset(sql)
        if df is not None:
            df.columns = ['Year', 'Total Revenue']
            print(df)
        else:
            print("Failed to fetch data.")
