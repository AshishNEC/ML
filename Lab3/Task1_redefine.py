import pandas as pd
import numpy as np
import random as rd
import matplotlib.pyplot as plt


dataset = pd.read_csv('inc_vs_rent.csv')
print(dataset)

X = dataset.iloc[:, [3, 4]].values
print(X)
dataset.describe()

m = X.shape[0]  # number of training examples
n = X.shape[1]  # number of features. Here n=2
n_iter = 100

K=3 # number of clusters


Centroids=np.array([]).reshape(n,0)

for i in range(K):
    rand=rd.randint(0,m-1)
    Centroids=np.c_[Centroids,X[rand]]


Output = {}

for i in range(n_iter):
    # step 2.a
    EuclidianDistance = np.array([]).reshape(m, 0)
    for k in range(K):
        tempDist = np.sum((X - Centroids[:, k]) ** 2, axis=1)
        EuclidianDistance = np.c_[EuclidianDistance, tempDist]
    C = np.argmin(EuclidianDistance, axis=1) + 1
    # step 2.b
    Y = {}
    for k in range(K):
        Y[k + 1] = np.array([]).reshape(2, 0)
    for i in range(m):
        Y[C[i]] = np.c_[Y[C[i]], X[i]]

    for k in range(K):
        Y[k + 1] = Y[k + 1].T

    for k in range(K):
        Centroids[:, k] = np.mean(Y[k + 1], axis=0)
    Output = Y

print(Output)

plt.scatter(X[:, 0], X[:, 1], c='black', label='uncluttered data')
plt.xlabel('Annual rent sqm')
plt.ylabel('Avg yearly inc KSEK')
plt.legend()
plt.title('Plot of data points')
plt.show()


color=['red','blue','green','cyan','magenta']
labels=['cluster1','cluster2','cluster3','cluster4','cluster5']
for k in range(K):
    plt.scatter(Output[k+1][:,0],Output[k+1][:,1],c=color[k],label=labels[k])
plt.scatter(Centroids[0,:],Centroids[1,:],s=300,c='yellow',label='Centroids')
plt.xlabel('Annual rent sqm')
plt.ylabel('Avg yearly inc KSEK')
plt.legend()
plt.show()
