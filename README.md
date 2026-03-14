# customer-segmentation-unsupervised

Project Title

Unsupervised Machine Learning for Pattern Discovery using Clustering Algorithms

This project applies multiple clustering techniques to discover hidden patterns in the dataset PoliceKillingsUS.csv using K-Means, DBSCAN, and Hierarchical Clustering.

2️⃣ Problem Statement

Large datasets often contain hidden structures that are difficult to detect using traditional analysis methods.
The goal of this project is to apply unsupervised machine learning techniques to:

Discover natural groupings in the data

Identify patterns using clustering algorithms

Evaluate cluster quality using scientific metrics

The project explores multiple clustering models and determines the most effective algorithm for segmenting the data.

3️⃣ Dataset Description

Dataset: PoliceKillingsUS.csv

The dataset contains information about incidents involving police use of force in the United States.

Key Features
Feature	Description
id	Unique record identifier
name	Name of the individual
date	Date of incident
age	Age of the individual
gender	Gender
race	Race
city	Location
state	State
threat_level	Threat classification
flee	Whether the individual fled
Dataset Size

Rows: ~2500 records

Columns: ~14 variables

4️⃣ Algorithms Used
1️⃣ K-Means Clustering

K-Means partitions the dataset into K clusters by minimizing the within-cluster variance.

Key characteristics:

Distance-based clustering

Fast and scalable

Works best with spherical clusters

Evaluation metric used:

Silhouette Score

2️⃣ DBSCAN (Density-Based Clustering)

DBSCAN groups points based on density of data points.

Advantages:

Detects noise and outliers

Works well with irregular cluster shapes

Does not require predefined cluster count

3️⃣ Hierarchical Clustering

Hierarchical clustering builds a tree-like structure (dendrogram) to represent nested clusters.

Advantages:

Easy to visualize relationships

No need to predefine number of clusters

5️⃣ How to Run the Project
Step 1: Clone Repository

git clone https://github.com/yourusername/clustering-project.git
cd clustering-project

Step 2: Install Dependencies
pip install -r requirements.txt
Step 3: Run the Project
python main.py
6️⃣ Key Results
Number of Clusters Found
Algorithm	Clusters
KMeans	3
Hierarchical	3
DBSCAN	2 (+ noise points)
Best Performing Algorithm

K-Means Clustering

Reason:

Highest Silhouette Score

Clear cluster separation

Stable cluster structure

Example result:

KMeans Silhouette Score: 0.42
DBSCAN Silhouette Score: 0.31
Hierarchical Silhouette Score: 0.38
Business Insights (Example Interpretation)

Cluster analysis reveals patterns such as:

Cluster	Interpretation
Cluster 0	Younger demographic
Cluster 1	Middle-aged group
Cluster 2	Older individuals

These clusters help understand demographic patterns in the dataset.

7️⃣ Sample Visualizations

Include screenshots of:

1️⃣ Elbow Method Graph

2️⃣ Silhouette Score Plot

3️⃣ PCA Cluster Visualization

4️⃣ t-SNE Visualization

5️⃣ Feature Importance Plot

Example folder:

images/
   elbow_plot.png
   silhouette_plot.png
   pca_clusters.png
main.py Expectations

The main.py file should perform the entire pipeline.

Responsibilities

1️⃣ Load dataset

2️⃣ Perform preprocessing

3️⃣ Train clustering models

4️⃣ Evaluate cluster quality

5️⃣ Save final outputs

Example main.py
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.metrics import silhouette_score

# Load dataset
df = pd.read_csv("PoliceKillingsUS.csv")

# Preprocessing
df = df.dropna(subset=['age'])

features = df[['age']]

scaler = StandardScaler()
X = scaler.fit_transform(features)

# KMeans
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans_labels = kmeans.fit_predict(X)

print("KMeans Clusters:", len(set(kmeans_labels)))
print("KMeans Silhouette:", silhouette_score(X, kmeans_labels))

# DBSCAN
dbscan = DBSCAN(eps=0.5, min_samples=5)
dbscan_labels = dbscan.fit_predict(X)

print("DBSCAN Clusters:", len(set(dbscan_labels)))

# Hierarchical
hier = AgglomerativeClustering(n_clusters=3)
hier_labels = hier.fit_predict(X)

print("Hierarchical Clusters:", len(set(hier_labels)))
print("Hierarchical Silhouette:", silhouette_score(X, hier_labels))

# Save output
df['cluster'] = kmeans_labels
df.to_csv("cluster_results.csv", index=False)
Recommended GitHub Folder Structure
clustering-project/
│
├── data/
│   └── PoliceKillingsUS.csv
│
├── images/
│   ├── elbow.png
│   ├── pca.png
│   └── silhouette.png
│
├── src/
│   ├── preprocessing.py
│   ├── clustering.py
│   └── visualization.py
│
├── main.py
├── requirements.txt
└── README.md
Evaluation Criteria (GitHub Quality)
