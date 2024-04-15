from Connectors.Connector import Connector
from Models.PurchaseKMeans import PurchaseKMeans

connector=Connector(server="localhost",port=3306,database="lecturer_retails",username="root",password="@Obama123")
connector.connect()
purchaseKm=PurchaseKMeans(connector=connector)
purchaseKm.execPurchaseHistory()
df=purchaseKm.processAgeSalesAmount()
purchaseKm.processTransformByColumns(df,["payment_method"])
print(df.columns)

columns=['age','payment_method','sales_amount']
purchaseKm.showHistogram(df,columns)
purchaseKm.elbowMethod(df,columns)
cluster=3
colors=["red","green","blue","purple","black","pink","orange"]

X = df.loc[:, columns].values
y_kmeans,centroids,labels=purchaseKm.runKMeans(X,cluster)
print(labels)
df["cluster"]=labels
for i in range(cluster):
    dfCluster=df[df["cluster"]==i]
    print("Customer in cluster %s:"%i)
    print(dfCluster)
#
# purchaseKm.visualizeKMeans(X,
#                 y_kmeans,
#                 cluster,
#                 "Clusters of Customers - Age X sales_amount",
#                 "age",
#                 "sales_amount",
#                 colors)
hover_data=df.columns
purchaseKm.visualize3DKmeans(df,columns,hover_data,cluster)
