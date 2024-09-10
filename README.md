The current repository contains the following MARA tools:

* Perform PCA on your numerical dataset
* Cluster numerical data with or without predefined number of classes
* Generate a 2D or 3D scatter plot using provided CSV file

## Suggested data analysis workflow
1. upload `test_data/EGFR_unique.csv`
2. what are the numerical columns in this csv file?
3. create PCA on this dataset, excluding MolRegNo, Value,Assay Category, Target ID, Pubmed ID
4. draw a scatter plot for the first 3 principal components
5. cluster the data into 3 categories using k-means
6. add cluster labels to the previous scatter plot