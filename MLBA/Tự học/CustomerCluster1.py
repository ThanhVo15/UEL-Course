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

if __name__ == '__main__':
    with app.app_context():
        sql1 = "SELECT * FROM customer"
        df1 = queryDataset(sql1)
        if df1 is not None:
            print(df1)
        else:
            print("Failed to fetch data.")


sql2="select distinct customer.CustomerId, Age, Annual_Income, Spending_Score " \
     "from customer, customer_spend_score " \
     "where customer.CustomerId=customer_spend_score.CustomerID"

df2=queryDataset( sql2)
df2.columns = ['CustomerId', 'Age', 'Annual Income', 'Spending Score']

print(df2)

print(df2.head())

print(df2.describe())


def showHistogram(df, columns):
    plt.figure(1, figsize=(7,8))
    n = 0
    for column in columns:
        n += 1
        plt.subplot(3, 1, n)
        plt.subplots_adjust(hspace=0.5, wspace=0.5)
        sns.histplot(df[column], bins=32)
        plt.title(f'Histogram of {column}')
    plt.show()

showHistogram(df2, df2.columns[1:])


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

columns = ['Age', 'Spending Score']
elbowMethod(df2, columns)

def runKMeans(X, n_clusters):
    model = KMeans(n_clusters=n_clusters,
                   init='k-means++',
                   max_iter=500,
                   random_state=42)
    model.fit(X)

    labels = model.labels_
    centroids = model.cluster_centers_
    y_kmeans = model.fit_predict(X)

    return y_kmeans, centroids, labels


def runKMeans(X, n_clusters):
    model = KMeans(n_clusters=n_clusters, init='k-means++', max_iter=500, random_state=42)
    model.fit(X)
    labels = model.labels_
    centroids = model.cluster_centers_
    y_kmeans = model.fit_predict(X)
    return y_kmeans, centroids, labels

X = df2.loc[:, columns].values
cluster = 4
colors = ['red', 'green', 'blue', 'purple', 'black', 'pink', 'orange']

y_kmeans, centroids, labels = runKMeans(X, cluster)

print(y_kmeans)
print(centroids)
print(labels)

df2['cluster'] = labels

def visualizeKMeans(X, y_kmeans, n_clusters, title, xlabel, ylabel, colors):
    plt.figure(figsize=(10, 10))
    for i in range(n_clusters):
        plt.scatter(X[y_kmeans == i, 0], X[y_kmeans == i, 1], s=100, c=colors[i], label=f'Cluster {i+1}')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()

visualizeKMeans(X, y_kmeans, cluster, "Clusters of Customers - Age X Spending Score", "Age", "Spending Score", colors)

# Function to run KMeans and return the labels, centroids, and inertia
def runKMeans(X, n_clusters):
    model = KMeans(n_clusters=n_clusters, init='k-means++', max_iter=500, random_state=42)
    model.fit(X)
    labels = model.labels_
    centroids = model.cluster_centers_
    y_kmeans = model.fit_predict(X)
    return y_kmeans, centroids, labels

# Function to calculate and plot the elbow method
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

# Function to visualize the clusters in 2D
def visualizeKMeans2D(X, y_kmeans, n_clusters, title, xlabel, ylabel, colors):
    plt.figure(figsize=(10, 10))
    for i in range(n_clusters):
        plt.scatter(X[y_kmeans == i, 0], X[y_kmeans == i, 1], s=100, c=colors[i], label=f'Cluster {i+1}')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()

# Function to visualize the clusters in 3D
def visualize3DKmeans(df, columns, hover_data, cluster):
    fig = px.scatter_3d(df, x=columns[0], y=columns[1], z=columns[2],
                        color='cluster', hover_data=hover_data,
                        category_orders={'cluster': range(0, cluster)})
    fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
    fig.show()

# Assuming df2 is a pandas DataFrame that contains the data
columns = ['Age', 'Annual Income', 'Spending Score']
cluster = 6

# Running the elbow method to determine the optimal number of clusters
elbowMethod(df2, columns)

# Running KMeans with the specified number of clusters
X = df2.loc[:, columns].values
y_kmeans, centroids, labels = runKMeans(X, cluster)

# Adding the cluster labels to the original DataFrame
df2['cluster'] = labels

# Print the output from KMeans
print(y_kmeans)
print(centroids)
print(labels)
print(df2)

colors = ['red', 'green', 'blue', 'purple', 'black', 'pink', 'orange']
visualizeKMeans2D(X, y_kmeans, cluster, "Clusters of Customers - Annual Income X Spending Score", "Annual Income", "Spending Score", colors)
visualize3DKmeans(df2, columns, df2.columns, cluster)

hover_data = df2.columns
visualize3DKmeans(df2, columns, hover_data, cluster)

def print_customer_details_to_console(df, cluster_column_name='cluster'):
    for cluster in sorted(df[cluster_column_name].unique()):
        print(f"Cluster {cluster}:")
        customer_ids = df[df[cluster_column_name] == cluster]['CustomerID']
        for customer_id in customer_ids:
            customer_details = get_customer_details(customer_id)
            print(customer_details)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/cluster/<int:cluster_id>')
def show_customers(cluster_id):
    customer_ids = df2[df2['cluster'] == cluster_id]['CustomerID'].tolist()
    customer_details = [get_customer_details(cid) for cid in customer_ids]
    return render_template('cluster_customers.html', customers=customer_details, cluster_id=cluster_id)

if __name__ == '__main__':
    app.run(debug=True)

def get_customer_details(customer_id):
    query = "SELECT * FROM Customer WHERE CustomerID = %s"
    cursor = mysql_connection.cursor()
    cursor.execute(query, (customer_id,))
    customer_details = cursor.fetchall()
    cursor.close()
    return customer_details

df2['cluster'] = KMeans(n_clusters=5).fit_predict(X)
print_customer_details_to_console(df2)


