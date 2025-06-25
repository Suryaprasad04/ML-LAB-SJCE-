from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

def kmeans_clustering():
    data = load_iris()
    X = data.data

    model = KMeans(n_clusters=3)
    y_kmeans = model.fit_predict(X)

    plt.scatter(X[:, 0], X[:, 1], c=y_kmeans)
    plt.title("K-Means Clustering")
    plt.show()

kmeans_clustering()
