# Cluster numerical data with or without predefined number of classes (Informatics)

## Description
Run either K-Means or DBSCAN clustering on a numerical dataset. The tool will generate a new column in the input CSV file that contains the cluster labels.

## Input
* file - The CSV file that contains numerical data to run clustering analysis
* cluster_columns - A list of columns for the numerical values in the CSV file to be used for clustering. If not provided, this will be an empty list and all numerical columns will be used.
* n_clusters - The number of clusters to be generated. If provided, the tool will run K-Means with this specified K value. Otherwise, it will run DBSCAN clustering that automatically defines the number of classes. 
* additional_params - An optional dictionary that contains additional parameters for the clustering algorithm. 

## Output
A CSV file and a description of the analysis that includes the clustering algorithm used, number of clustered labels, the list of features used from the original file, and the name of the generated file. 

## Setup
### requirements
pandas
numpy
scikit-learn