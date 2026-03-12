plt.figure()

plt.scatter(
    X_pca[:,0],
    X_pca[:,1],
    c=df['Cluster']
)

plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("PCA Cluster Visualization (2D)")

plt.show()

from mpl_toolkits.mplot3d import Axes3D

pca3 = PCA(n_components=3)
X_pca3 = pca3.fit_transform(X_scaled)

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

ax.scatter(
    X_pca3[:,0],
    X_pca3[:,1],
    X_pca3[:,2],
    c=df['Cluster']
)

ax.set_xlabel("PC1")
ax.set_ylabel("PC2")
ax.set_zlabel("PC3")

plt.title("3D PCA Cluster Visualization")

plt.show()
