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
        sql = "SELECT c.Name AS CategoryName, " \
            "SUBSTRING_INDEX(SUBSTRING_INDEX(o.OrderDate, '/', -1), '/', 1) AS OrderYear, " \
            "SUM(od.OrderQty * od.UnitPrice) AS TotalRevenue " \
            "FROM category c " \
            "JOIN subcategory sc ON sc.CategoryID = c.CategoryID " \
            "JOIN product p ON p.ProductSubcategoryID = sc.SubCategoryID " \
            "JOIN orderdetails od ON p.ProductID = od.ProductID " \
            "JOIN orders o ON od.OrderId = o.OrderId " \
            "GROUP BY CategoryName, OrderYear " \
            "ORDER BY CategoryName, OrderYear;"

        df = queryDataset(sql)
        if df is not None:
            df.columns = ['CategoryName', 'Year', 'Total Revenue']
            print(df)
        else:
            print("Failed to fetch data.")

