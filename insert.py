import numpy as np
from pymongo import MongoClient
from sklearn.cluster import KMeans

#MongoDB
client=MongoClient('mongodb://localhost:27017/')
try:
    conn=MongoClient()
    print('Connected Succ')
except:
    print('Could Not print')
db=client.Index
collection=db.Index
path_col='C:/Users/21622/PycharmProjects/Index_Recherche/Color_descp/output1.txt'
L=[]
with open(path_col,'r') as f:
    lines = f.readlines()
for i in lines:
    table.append(i.split())
array_edge=np.array(table)
path='C:/Users/21622/PycharmProjects/Index_Recherche/eh_descriptors'
table=[]
with open(path+ '/'+'eh'+str(1)+'.txt','r') as f:
    lines = f.readlines()
for i in lines:
    table.append(i.split())
array_edge=np.array(table)
Kmeans=KMeans(n_clusters=20).fit(array_edge)
Clusters=Kmeans.predict(array_edge)
centroids = Kmeans.cluster_centers_
for k in range(10,10000):
    cluster=str(Clusters[k])
    line_DB={"index":k,"edge_value":table[k],"cluster":cluster}


    collection.insert_one(line_DB)
print ('Done')