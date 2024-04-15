import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.cluster import KMeans
import numpy as np

from Models.PurchaseMLModel import PurchaseMLModel


class PurchaseKMeans(PurchaseMLModel):
    def __init__(self,connector=None):
        super().__init__(connector=connector)

    def showHistogram(self,df, columns):
        plt.figure(1, figsize=(7, 8))
        n = 0
        for column in columns:
            n += 1
            plt.subplot(3, 1, n)
            plt.subplots_adjust(hspace=0.5, wspace=0.5)
            sns.distplot(df[column], bins=32)
            plt.title(f'Histogram of {column}')
        plt.show()

    # showHistogram(df2,df2.columns[1:])

    def elbowMethod(self,df, columnsForElbow):
        X = df.loc[:, columnsForElbow].values
        inertia = []
        for n in range(1, 11):
            model = KMeans(n_clusters=n,
                           init='k-means++',
                           max_iter=500,
                           random_state=42)
            model.fit(X)
            inertia.append(model.inertia_)

        plt.figure(1, figsize=(15, 6))
        plt.plot(np.arange(1, 11), inertia, 'o')
        plt.plot(np.arange(1, 11), inertia, '-', alpha=0.5)
        plt.xlabel('Number of Clusters'), plt.ylabel('Cluster sum of squared distances')
        plt.show()

    def runKMeans(self,X, cluster):
        model = KMeans(n_clusters=cluster,
                       init='k-means++',
                       max_iter=500,
                       random_state=42)
        model.fit(X)
        labels = model.labels_
        centroids = model.cluster_centers_
        y_kmeans = model.fit_predict(X)
        return y_kmeans, centroids, labels

    def visualizeKMeans(self,X, y_kmeans, cluster, title, xlabel, ylabel, colors):
        plt.figure(figsize=(10, 10))
        for i in range(cluster):
            plt.scatter(X[y_kmeans == i, 0],
                        X[y_kmeans == i, 1],
                        s=100,
                        c=colors[i],
                        label='Cluster %i' % (i + 1))
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.legend()
        plt.show()

    def visualize3DKmeans(self, df, columns, hover_data, cluster):
        fig = px.scatter_3d(df,
                            x=columns[0],
                            y=columns[1],
                            z=columns[2],
                            color='cluster',
                            hover_data=hover_data,
                            category_orders={"cluster": range(0, cluster)},
                            )
        fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
        fig.show()