# Perform PCA on your numerical dataset (Informatics)

## Details
 Using the sklearn package, analyze a data set via PCA to the designated variance threshold. You'll receive the resulting analysis concatenated to your original table and receive the explained variance ratios for your attached principal components. With this tool you can run a PCA on a CSV file or dataset.

## Input
* file - The CSV file to be analyzed
* pca_columns - A list of columns for the numerical values in the CSV file to be used for PCA. If not provided, this will be an empty list and all numerical columns will be used.
* variance_threshold -This is the desired variance threshold for the analysis. Defaults to 0.95.
* n_components - The number of designated components for the PCA. When provided, this will override the variance threshold. 


## Output
A CSV file and a description of the analysis that includes number of principal components, a table of explained variance ratios for the principal components, the list of features used from the original file, and the name of the generated file. 

## Setup
### requirements
pandas
numpy
scikit-learn