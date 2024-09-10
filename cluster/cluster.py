import pandas as pd
from datetime import datetime

def create_timestamp() -> str:
  # helper function to create a unique timestamp
  dt = str(datetime.now())
  return dt.replace("-", "_").replace(":", "_").replace(" ", "_")

def perform_kmeans(data, n_clusters, additional_params={}):
    from sklearn.cluster import KMeans
    kmeans = KMeans(n_clusters=n_clusters, **additional_params)
    kmeans.fit(data)
    return kmeans.labels_

def perform_dbscan(data, additional_params={}):
    from sklearn.cluster import DBSCAN
    dbscan = DBSCAN(**additional_params)
    dbscan.fit(data)
    return dbscan.labels_

def run(file, cluster_columns, n_clusters=-1, additional_params={}):
    '''
    Run either K-Means or DBSCAN clustering on a numerical dataset. 
    The tool will generate a new column in the input CSV file that contains the cluster labels.
    '''
    

            
    ## Read data from a CSV file
    data_df = pd.read_csv(file)
    if len(cluster_columns) == 0:
        clean_data = data_df.select_dtypes(include=['float'])
    else:
        missing_columns = [column for column in cluster_columns if column not in data_df.columns]
        assert len(missing_columns) == 0, "These columns are not present in the data: " + str(missing_columns)
        clean_data = data_df[cluster_columns]
    clean_data = clean_data.dropna(axis=1)
    data_sets = clean_data.columns
    data_array = clean_data.values

    ## Run K-Means or DBSCAN based on n_clusters param
    if n_clusters > 0:
        method = "K-Means"
        cluster_labels = perform_kmeans(data_array, n_clusters, additional_params)
    else:
        method = "DBSCAN"
        cluster_labels = perform_dbscan(data_array, additional_params)
        n_clusters = len(set(cluster_labels))


    ## Append labels to OG CSV
    label_df = pd.DataFrame(cluster_labels, columns=["Label"])
    final_data_df = pd.concat([data_df, label_df], axis=1)

    ## Create the File Name
    filename = f'{(file.split(".csv")[0])}_{method}_clustered_{n_clusters}_{create_timestamp()}.csv'


    ## Create the File
    final_data_df.to_csv(filename, index=False)

    print(f"Successfully clustered data into {n_clusters} classes using {method}."+
        f"\n\nThe following columns were able to be used: {', '.join(list(data_sets))}"+
        f"\n\nThe clustered labels have been added to your data table in {filename}.")
    
if __name__ == "__main__":
    run("test_data/after_PCA.csv", 
        cluster_columns=["PC1", "PC2", "PC3"],
        n_clusters=3)