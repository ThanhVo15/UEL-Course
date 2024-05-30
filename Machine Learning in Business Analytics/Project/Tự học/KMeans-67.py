from flask import Flask
from flask_mysqldb import MySQL
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.cluster import KMeans

app = Flask(__name__)
mysql = MySQL()

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '@Obama123'
app.config['MYSQL_DB'] = 'salesdatabase'

mysql = MySQL(app)

def closeConnect(conn):
    if conn != None:
        conn.close()

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

sql2="select distinct customer.CustomerId, Age, Annual_Income, Spending_Score " \
     "from customer, customer_spend_score " \
     "where customer.CustomerId=customer_spend_score.CustomerID"

df2=queryDataset( sql2)
df2.columns = ['CustomerId', 'Age', 'Annual Income', 'Spending Score']

print(df2)

print(df2.head())

print(df2.describe())



def print_customer_details_to_console(df, cluster_column_name='cluster'):
    for cluster in sorted(df[cluster_column_name].unique()):
        print(f"Cluster {cluster}:")
        customer_ids = df[df[cluster_column_name] == cluster]['CustomerID']
        for customer_id in customer_ids:
            customer_details = get_customer_details(customer_id)
            print(customer_details)
