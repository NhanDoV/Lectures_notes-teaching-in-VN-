The main difference between the two is that 
- clustering is generally driven by machine learning algorithms, and 
- segmentation is human-driven.

### Comparison some clustering-algorithms

| Partition clustering (e.g, `K-Means, K-medians`) |	Hierarchical clustering |	Spectral clustering|
|-|-|-|
|Works on data with Euclidean feature spaces|Works on pairwise distance functions in a bottom-up fashion and recursive partitional clustering in a top-down fashion|Works on similarity graphs where each node represents an entity and weight on the edge|
|Complixity of k-Means is linear O(n) <br> this will be faster with `MinibatchKmeans`|Complixity is quardratic O(n^2)|Complixity is is linear O(n)|
|**Prior knowledge of number of clusters is necessary**.<br> We also using `silhouette score or dendrogram` to find the most optimal number of clusters before|Number of clusters can be interpreted after clustering is done| Prior knowledge of number of clusters is necessary |