import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv("PoliceKillingsUS.csv")

# Select numeric features
data = df[['age']].dropna()

# Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(data)

# KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(X_scaled)

data['Cluster'] = clusters

# Train classifier to determine feature importance
rf = RandomForestClassifier()
rf.fit(X_scaled, clusters)

importance = rf.feature_importances_

# Plot feature importance
plt.bar(['Age'], importance)
plt.title("Feature Importance for Clusters")
plt.ylabel("Importance Score")
plt.show()

print("Feature Importance:", importance)
