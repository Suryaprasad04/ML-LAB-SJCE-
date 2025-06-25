from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

def agglomerative_clustering():
    data = load_iris()
    X = data.data

    # Complete linkage clustering
    model_complete = AgglomerativeClustering(n_clusters=3, linkage='complete')
    labels_complete = model_complete.fit_predict(X)

    # Single linkage clustering
    model_single = AgglomerativeClustering(n_clusters=3, linkage='single')
    labels_single = model_single.fit_predict(X)

    # Plot both side by side
    plt.figure(figsize=(12, 5))

    # Complete linkage plot
    plt.subplot(1, 2, 1)
    plt.scatter(X[:, 0], X[:, 1], c=labels_complete, cmap='viridis')
    plt.title("Complete Linkage")

    # Single linkage plot
    plt.subplot(1, 2, 2)
    plt.scatter(X[:, 0], X[:, 1], c=labels_single, cmap='plasma')
    plt.title("Single Linkage")

    plt.tight_layout()
    plt.show()

agglomerative_clustering()
