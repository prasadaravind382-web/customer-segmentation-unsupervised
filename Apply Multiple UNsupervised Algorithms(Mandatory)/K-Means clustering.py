kmeans = KMeans(n_clusters=3, random_state=42)

df['KMeans_Cluster'] = kmeans.fit_predict(X_scaled)

print(df[['age','gender','race','KMeans_Cluster']].head())
