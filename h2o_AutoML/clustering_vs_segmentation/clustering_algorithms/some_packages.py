from sklearn.cluster import KMeans, DBSCAN, MiniBatchKMeans, Birch, AgglomerativeClustering, AffinityPropagation, MeanShift, OPTICS, SpectralClustering
from sklearn.mixture import GaussianMixture
from hdbscan import HDBSCAN
from collections import Counter
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

def fit_and_plot_clusters(X, y, n_clusters=3, seed=42):
    """
        Since the method to obtain the labels is difference (.fit vs .predict) 
        hence I didnt use loop on the algo-names
    """
    # Standard scaling
    X_scale = StandardScaler().fit_transform(X)
    # PCA to first 2 components
    X_scale = PCA(n_components=3).fit_transform(X_scale)
    
    # Initialize algorithms then fit to data
    kmeans = KMeans(n_clusters=n_clusters, random_state=seed).fit(X_scale)
    dbscan = DBSCAN(eps=0.5, min_samples=5).fit(X_scale)
    hdbscan = HDBSCAN(min_cluster_size=8,  max_cluster_size=50, 
                      leaf_size=10, min_samples=5, cluster_selection_epsilon=0.05).fit(X_scale)
    mnbkmeans = MiniBatchKMeans(n_clusters=n_clusters, batch_size=10).fit(X_scale)
    agglom = AgglomerativeClustering(n_clusters=n_clusters, linkage='ward').fit(X_scale)
    birch = Birch(threshold=0.03, n_clusters=n_clusters).fit(X_scale)
    affine = AffinityPropagation(preference=-50,damping=0.8, max_iter=500).fit(X_scale)
    mshift = MeanShift(bandwidth=1).fit(X_scale)
    optics = OPTICS(eps=0.25, min_samples=10, xi=0.1).fit(X_scale)
    spectral = SpectralClustering(  n_clusters=n_clusters, assign_labels='discretize',
                                    random_state=seed,
                                    affinity='rbf',
                                    ).fit(X_scale)
    gauss_mixmo = GaussianMixture(n_components=n_clusters).fit(X_scale)
    # for prediction labels
    y_preds = {}
    y_preds['Ground Truth'] = y
    y_preds['KMeans'] = [f"cluster_{k+1}" for k in kmeans.labels_]
    y_preds['Mini batch-KMeans'] = [f"cluster_{k+1}" for k in mnbkmeans.labels_]
    y_preds['DBSCAN'] = [f"cluster_{k+1}" for k in dbscan.labels_]
    y_preds['Hierarchical-DBSCAN'] = [f"cluster_{k+1}" for k in hdbscan.labels_]
    y_preds['Agglomerative Clustering'] = [f"cluster_{k+1}" for k in agglom.labels_]
    y_preds['Birch'] = [f"cluster_{k+1}" for k in birch.predict(X_scale)]
    y_preds['OPTICS'] = [f"cluster_{k+1}" for k in optics.labels_]
    y_preds['Mean shift'] = [f"cluster_{k+1}" for k in mshift.predict(X_scale)]
    y_preds['Affinity-Propagation'] = [f"cluster_{k+1}" for k in affine.predict(X_scale)]
    y_preds['Gaussian-mixture-models'] = [f"cluster_{k+1}" for k in gauss_mixmo.predict(X_scale)]
    y_preds['Spectral Clustering'] = [f"cluster_{k+1}" for k in spectral.labels_]
    
    # Plot predictions vs. ground truth
    fig, axes = plt.subplots(nrows=6, ncols=2, figsize=(20, 20))
    axes = axes.ravel()
    for i, name in enumerate(y_preds.keys()):
        ax = axes[i]
        sns.scatterplot(x=X[:, 0], y=X[:, 1], hue=y_preds[name], ax=ax, legend=True, palette='bright')
        if type(y_preds[name]) == list:
            notes = Counter(y_preds[name])
        else:
            notes = Counter(y_preds[name].to_list())
        ax.set_title(f"{name}\n{dict(notes)}", fontsize=9)
        ax.legend(loc='lower right', fontsize=9)
        ax.set_ylabel("petal_wid")
        ax.set_xlabel("petal_len")
    plt.tight_layout()
    plt.show()