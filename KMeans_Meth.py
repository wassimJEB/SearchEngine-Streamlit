import numpy as np
from sklearn.cluster import KMeans


from PIL import Image
from io import BytesIO

import numpy as np
import time
def calcDistance(pic1, pic2):
    result = float(0)
    for i in range(0, len(pic1)):
        result += (float(pic1[i]) - float(pic2[i])) ** 2

    return result

def chi2_distance(histA, histB, eps = 1e-10):
	# compute the chi-squared distance
    d=0
    for i in range(0,len(histA)):
        a= float(histA[i])
        b= float(histB[i])
        d+= ((a - b) ** 2) / (a + b + eps)
    d= 0.5*d
    return d
def load_image_into_numpy_array(data):
    return np.array(Image.open(BytesIO(data)))


def Reading(collection):


    l = []
    n=10
    path='C:/Users/21622/PycharmProjects/Index_Recherche/eh_descriptors'
    for k in range(1,n+1,1):
        print('reading_images'+str(k))
        print(str(k)+'###################"')
        with open(path+'/eh'+str(k)+'.txt','r') as f :
            lines=f.readline()

        #print(lines)
        for i in lines:

            l.append(i.split(' '))

        answers=np.array(l)
        print('Finish')
    Kmeans=KMeans(n_clusters=200).fit(answers)
    Clusters = Kmeans.predict(answers)
    centroids=Kmeans.cluster_centers_
    print('finished clustering ')
    for k in range(0,10000):
        cluster=str(Clusters[k])
        line_DB = {"index": k, "edge_value": l[k], "cluster": cluster}
        collection.insert_one(line_DB)
        print(str(k) + "is added")


def Annoy():





    return L