# Name: Vo Minh Thanh
# StudentID: K214162152

from flask import Flask
from flask_mysqldb import MySQL
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.cluster import KMeans

mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '@Obama123'
app.config['MYSQL_DB'] = 'sakila'

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
    
if __name__ == '__main__':
    with app.app_context():
        sql = "SELECT c.customer_id, c.first_name, c.last_name, COUNT(DISTINCT r.rental_id) AS rental_count, SUM(p.amount) AS total_spent, f.film_id, f.title, COUNT(DISTINCT i.inventory_id) AS inventory_count " \
      "FROM customer c " \
      "JOIN rental r ON c.customer_id = r.customer_id " \
      "JOIN inventory i ON r.inventory_id = i.inventory_id " \
      "JOIN film f ON i.film_id = f.film_id " \
      "JOIN payment p ON r.rental_id = p.rental_id " \
      "GROUP BY c.customer_id, f.film_id, c.first_name, c.last_name, f.title " \
      "ORDER BY c.customer_id, rental_count DESC;"

        df = queryDataset(sql)
        df.columns = ['CustomerId', 'FirstName', 'LastName', 'RentalCount', 'TotalSpent', 'FilmId', 'Title', 'InventoryCount']
        if df is not None:
            print(df)
        else:
            print("Failed to fetch data.")


print(df.info())
print(df.describe())
df['TotalSpent'] = df['TotalSpent'].astype(float)

def showHistogram(df, columns):
    plt.figure(figsize=(7, 8))
    n = 0
    for column in columns:
        n += 1
        plt.subplot(len(columns), 1, n) 
        plt.subplots_adjust(hspace=0.5, wspace=0.5)
        sns.histplot(df[column], bins=32)
        plt.title(f'Histogram of {column}')
    plt.show()

columns = ['RentalCount', 'TotalSpent', 'InventoryCount']
showHistogram(df, columns)

def elbowMethod(df, columnsForElbow):
    X = df.loc[:, columnsForElbow].values
    inertia = []

    for n in range(1, 11):
        model = KMeans(n_clusters=n, init='k-means++', max_iter=500, random_state=42)
        model.fit(X)
        inertia.append(model.inertia_)

    plt.figure(1, figsize=(15,6))
    plt.plot(np.arange(1, 11), inertia, 'o')
    plt.plot(np.arange(1, 11), inertia, '-', alpha=0.5)
    plt.xlabel('Number of Clusters')
    plt.ylabel('Cluster sum of squared distances')
    plt.show()

columns = ['RentalCount', 'TotalSpent', 'InventoryCount']
elbowMethod(df, columns)

def runKMeans(X, n_clusters):
    model = KMeans(n_clusters=n_clusters, init='k-means++', max_iter=500, random_state=42)
    model.fit(X)
    labels = model.labels_
    centroids = model.cluster_centers_
    y_kmeans = model.fit_predict(X)
    return y_kmeans, centroids, labels


X = df.loc[:, columns].values
cluster = 3
colors = ['red', 'green', 'blue', 'purple', 'black', 'pink', 'orange']

y_kmeans, centroids, labels = runKMeans(X, cluster)

print(y_kmeans)
print(centroids)
print(labels)

df['cluster'] = labels

import plotly.express as px

def visualize3DKmeans(df, columns, hover_data, n_clusters):
    fig = px.scatter_3d(df, x=columns[0], y=columns[1], z=columns[2],
                        color='cluster', hover_data=hover_data,
                        category_orders={'cluster': range(0, n_clusters)})
    fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
    fig.show()

hover_data = df.columns
visualize3DKmeans(df, columns, hover_data, cluster)



