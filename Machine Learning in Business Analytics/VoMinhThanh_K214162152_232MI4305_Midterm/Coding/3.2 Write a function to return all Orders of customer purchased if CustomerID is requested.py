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

def get_customer_orders(customer_id):
    try:
        with app.app_context():
            sql = f"""
                SELECT o.CustomerID, o.OrderID, o.OrderDate, od.ProductID, od.OrderQty, od.UnitPrice
                FROM orders o
                JOIN orderdetails od ON o.OrderID = od.OrderID
                WHERE o.CustomerID = {customer_id};
            """
            df = queryDataset(sql)
            if df is not None and not df.empty:
                df.columns = ['CustomerID', 'OrderID', 'OrderDate', 'ProductID', 'OrderQty', 'UnitPrice']
                return df
            else:
                print(f"No orders found for CustomerID: {customer_id}")
                return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == '__main__':
    while True:
        customer_id = input("Enter CustomerID (or 'exit' to quit): ")
        if customer_id.lower() == 'exit':
            break
        else:
            customer_orders = get_customer_orders(customer_id)
            if customer_orders is not None:
                print("Customer Orders:")
                print(customer_orders)
