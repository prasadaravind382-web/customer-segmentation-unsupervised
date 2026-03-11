gmm = GaussianMixture(n_components=3, random_state=42)

df['GMM_Cluster'] = gmm.fit_predict(X_scaled)

print(df[['age','gender','race','GMM_Cluster']].head())
