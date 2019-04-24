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

