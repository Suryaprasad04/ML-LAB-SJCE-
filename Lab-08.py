from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans

data=load_iris()
X=data.data

model = KMeans(n_clusters=3)
y_kmeans = model.fit_predict(X)

plt.scatter(X[:, 0], X[:, 1], c=y_kmeans)
plt.title("K-Means Clustering")
plt.show()
