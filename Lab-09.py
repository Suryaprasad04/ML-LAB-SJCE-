from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

data=load_iris()
X=data.data

model_simple=AgglomerativeClustering(n_clusters=3,linkage='single')
labels_simple=model_simple.fit_predict(X)

model_complete=AgglomerativeClustering(n_clusters=3,linkage='complete')
labels_complete=model_complete.fit_predict(X)

plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.scatter(X[:,0],X[:,1],c=labels_simple)
plt.title('Single Linkage')

plt.subplot(1,2,2)
plt.scatter(X[:,0],X[:,1],c=labels_complete)
plt.title('Complete Linkage')
plt.show()
