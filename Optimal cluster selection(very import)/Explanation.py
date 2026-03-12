️#1- Elbow Method Explanation
  The Elbow Method evaluates the Within Cluster Sum of Squares (WCSS), which measures how compact the clusters are
  WCSS decreases rapidly until K = 3

  After K = 3, the reduction becomes small

  The graph forms an “elbow” at K = 3, meaning adding more clusters does not significantly improve compactness

  Therefore K = 3 is optimal according to the Elbow Method

️#2- Silhouette Score Explanation

    The Silhouette Score measures how well each data point fits inside its cluster compared to other clusters
   range:

Score                 	Meaning
-1              	Incorrect clustering
 0	              Overlapping clusters
 1	              Well-separated clusters
Highest score occurs at K = 3

This indicates best cluster separation

 Therefore K = 3 provides the most distinct clusters

️# 3- Davies–Bouldin Index Explanation

The Davies–Bouldin Index (DBI) evaluates cluster similarity
Rule:
      Lower DBI = Better clustering
Lowest DBI occurs at K = 3

This means clusters are well separated and compact
Method	            Optimal K
Elbow Method         	3
Silhouette Score     	3
Davies–Bouldin Index	3
K = 3 was chosen because it provides the best balance
