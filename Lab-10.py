from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.datasets import load_iris
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
def lda():
    data=load_iris()
    X=data.data
    y=data.target
    lda=LinearDiscriminantAnalysis(n_components=2)
    X_lda=lda.fit_transform(X,y)

    plt.scatter(X_lda[:, 0], X_lda[:, 1], c=y)
    plt.title("LDA Projection")
    plt.show()

lda()

from sklearn.decomposition import PCA
def pca():
    data=load_iris()
    X=data.data
    y=data.target
    pca=PCA(n_components=2)
    X_pca=pca.fit_transform(X)

    plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y)
    plt.title("PCA Projection")
    plt.show()
pca()
