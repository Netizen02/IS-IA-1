import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


def fit(X):
    # scale the data
    X = np.asarray(X)
    scaler = StandardScaler()
    scaler.fit(X)
    scaled = scaler.transform(X)
    scaled = np.nan_to_num(scaled)
    # fit
    pca = PCA(n_components=3)
    pca.fit(scaled)
    comp = pca.transform(scaled)
    return comp.tolist()
