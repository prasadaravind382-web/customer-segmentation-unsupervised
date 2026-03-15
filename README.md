1.Project Title

Unsupervised Machine Learning for Pattern Discovery using Clustering Algorithms

This project applies multiple unsupervised learning algorithms to identify hidden patterns and natural groupings in the dataset using clustering techniques.

2️.Problem Statement

Large datasets often contain hidden structures that are difficult to identify using traditional analytical methods.
The objective of this project is to apply unsupervised machine learning algorithms to discover meaningful patterns in the dataset.

The project focuses on:

Identifying natural clusters in the data

Comparing different clustering algorithms

Evaluating clustering performance using scientific metrics

3️.Dataset Description

Dataset: PoliceKillingsUS.csv

The dataset contains information about incidents involving police use of force in the United States.

Key Features
| Feature      | Description                 |
| ------------ | --------------------------- |
| id           | Unique identifier           |
| name         | Name of individual          |
| date         | Date of incident            |
| age          | Age of individual           |
| gender       | Gender                      |
| race         | Race category               |
| city         | City location               |
| state        | State location              |
| threat_level | Level of threat reported    |
| flee         | Whether the individual fled |

Dataset Size

Records: ~2500 rows

Features: ~14 columns

4️.Algorithms Used
#1️.K-Means Clustering

K-Means partitions the dataset into K clusters by minimizing the distance between data points and cluster centroids.

Key characteristics:

Centroid-based clustering

Fast and efficient

Works best with spherical clusters

#2️.DBSCAN (Density-Based Spatial Clustering)

DBSCAN groups data points based on density of neighboring points.

Advantages:

Detects outliers automatically

Works well with irregular cluster shapes

Does not require predefined number of clusters

#3️.Hierarchical Clustering

Hierarchical clustering builds a tree-like structure (dendrogram) representing nested clusters.

Advantages:

No need to predefine cluster count

Provides intuitive visualization

5️.How to Run the Project

Step 1: Clone the Repository
git clone https://github.com/prasadaravind382-web/customer-segmentation-unsupervised.git
cd clustering-project

Step 2: Install Dependencies
pip install -r requirements.txt

Step 3: Run the Project
python main.py

6️.Key Results
Number of Clusters Found
| Algorithm    | Clusters           |
| ------------ | ------------------ |
| KMeans       | 3                  |
| Hierarchical | 3                  |
| DBSCAN       | 2 (+ noise points) |

Best Performing Algorithm

K-Means Clustering

Reason:

Highest Silhouette Score

Clear cluster separation

Stable clustering results

Example output:

KMeans Silhouette Score: 0.42
Hierarchical Silhouette Score: 0.38
DBSCAN Silhouette Score: 0.31
Business Insights

Cluster analysis reveals distinct demographic groupings in the dataset.

Example interpretation:

| Cluster   | Insight                 |
| --------- | ----------------------- |
| Cluster 0 | Younger individuals     |
| Cluster 1 | Middle-aged individuals |
| Cluster 2 | Older individuals       |

These patterns help identify demographic trends within the dataset.

7️.Sample Visualizations

Add screenshots of the following graphs:

Elbow Method Graph

K-Means Cluster Visualization

Hierarchical Clustering Plot

DBSCAN Clustering Plot

PCA Cluster Visualization

Correlation Heatmap

Example folder structure:

images/
   elbow_plot.png
   cluster_plot.png
   pca_visualization.png
main.py Expectations

The main.py script performs the entire clustering pipeline.

Responsibilities

The script should:

Load the dataset

Perform preprocessing

Apply clustering algorithms

Evaluate clustering performance

Save final outputs

Expected Outputs

The program prints:

Silhouette Score

Number of clusters detected

Example output:

Dataset Loaded Successfully
Preprocessing Completed

KMeans Clusters: 3
KMeans Silhouette Score: 0.42

Hierarchical Clusters: 3
Hierarchical Silhouette Score: 0.38

DBSCAN Clusters: 2
Output Files

The script saves results as:

cluster_results.csv
Recommended Project Folder Structure
clustering-project/
│

├── data/

│   └── PoliceKillingsUS.csv

│

├── images/

│   ├── elbow_plot.png

│   ├── clusters.png

│   └── pca_visualization.png

│

├── src/

│   ├── preprocessing.py

│   ├── clustering.py

│   └── visualization.py

│

├── main.py

├── requirements.txt

└── README.md

Evaluation Based on GitHub Quality

Your project will be evaluated based on the following criteria.

1️.Folder Structure Discipline

Maintain a well-organized directory structure separating:

data

source code

visualizations

documentation

2️.Clean Commits

Example commit messages:

Added preprocessing module
Implemented KMeans clustering
Added PCA visualization
Updated README documentation
3️.Code Modularity

Code should be separated into modules:

preprocessing

clustering

visualization

This improves maintainability and readability.

4️.Documentation Quality

The repository must include:

Detailed README

Explanation of algorithms

Instructions to run the project

5️.Code Readability

Follow best practices:

Use meaningful variable names

Add comments for important steps

Write clean and structured code
