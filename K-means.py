# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 22:45:47 2019

@author: diana
"""
# import the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#import the dataset
df = pd.read_csv('Mall_Customers.csv')
x = df.iloc[:, [-2,-1]]

#find the ideal number of clusters using WCSS
from sklearn.cluster import KMeans
wcss = []
for i in range (1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)
    
plt.plot(range(1,11), wcss)
plt.title('The elbow methodology')
plt.xlabel('No. clusters')
plt.ylabel('WCRR')
plt.show()

#train the k-means clustering model
model = KMeans(n_clusters = 5, init = "k-means++", random_state = 0)
y = model.fit_predict(x)

# visualize the clusters
plt.scatter(x[y == 0, 0], x[y == 0 , 1], s = 100, c = 'red', label = 'Oyster' )
plt.scatter(x[y == 1, 0], x[y == 1 , 1], s = 100, c = "Orange", label = "Bread n butter" )
plt.scatter(x[y == 2, 0], x[y == 2 , 1], s = 100, c = "Pink", label = "Perla" )
plt.scatter(x[y == 3, 0], x[y == 3 , 1], s = 100, c = "Blue", label = "careless" )
plt.scatter(x[y == 4, 0], x[y == 4 , 1], s = 100, c = "Brown", label = "sensible" )
plt.scatter(model.cluster_centers_[:, 0],model.cluster_centers_[:,1], s = 50, c = 'black', label = 'centroid')
plt.title('Customer types model')
plt.xlabel('Annual income (K$)')
plt.ylabel('Spending score (1-100)')
plt.legend()
plt.show()

