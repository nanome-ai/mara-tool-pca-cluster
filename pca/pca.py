import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from datetime import datetime, date

def run(file, pca_columns, variance_threshold, n_components):

    def perform_pca(data, variance_threshold, n_components):
        ## Standardize the data
        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(data)
        
        if n_components < 1:
            ## Create a PCA object
            pca = PCA()

            ## Fit the PCA model and transform the data
            transformed_data = pca.fit_transform(scaled_data)

            ## Get the explained variance ratio
            explained_variance_ratio = pca.explained_variance_ratio_

            ## Calculate the cumulative explained variance ratio
            cumulative_variance_ratio = np.cumsum(explained_variance_ratio)

            ## Find the number of components needed to cover the specified variance threshold
            n_components = np.argmax(cumulative_variance_ratio >= variance_threshold) + 1

            transformed_data = transformed_data[:, :n_components]
            explained_variance_ratio = explained_variance_ratio[:n_components]

        else:
            ## Create a PCA object
            pca = PCA(n_components=n_components)

            ## Fit the PCA model and transform the data
            transformed_data = pca.fit_transform(scaled_data)

            ## Get the explained variance ratio
            explained_variance_ratio = pca.explained_variance_ratio_

            
            
        ## Generate feature names for the principal components
        feature_names = [f'PC{i+1}' for i in range(n_components)]
        summed_variance_ratio = round(sum(explained_variance_ratio), 4)

        return transformed_data, explained_variance_ratio, summed_variance_ratio, feature_names


    ## Read data from a CSV file
    data_df = pd.read_csv(file)
    if len(pca_columns) == 0:
        clean_data = data_df.select_dtypes(include=['float'])
    else:
        missing_columns = [column for column in pca_columns if column not in data_df.columns]
        assert len(missing_columns) == 0, "These columns are not present in the data: " + str(missing_columns)
        clean_data = data_df[pca_columns]
    clean_data = clean_data.dropna(axis=1)
    data_sets = clean_data.columns
    data_array = clean_data.values

    ## Perform PCA with default number of components
    transformed_data, explained_variance_ratio, summed_variance_ratio, feature_names = perform_pca(data_array, variance_threshold, n_components)

    variances = pd.DataFrame(explained_variance_ratio).transpose()
    variances.columns = feature_names

    ## Append PC1-n to OG CSV
    PCA_df = pd.DataFrame(transformed_data, columns=feature_names)
    PCA_data_df = pd.concat([data_df, PCA_df], axis=1)

    ## Create the File Name
    today = date.today()
    day = today.strftime("%d%m%Y")
    now = datetime.now()
    day_time = day + f"_{now.hour}{now.minute}{now.second}"

    filename = f'{(file.split(".csv")[0])}_PCA_{variance_threshold}_{day_time}_.csv'

    ## Create the File
    PCA_data_df.to_csv(filename, index=False)

    print(f"The PCA is complete and generated {len(feature_names)} components to reach the {summed_variance_ratio} cumulative variance ratio."+
        f"\nThey had the following variances by component:\n{variances}"+
        f"\n\nThe following columns were able to be used: {', '.join(list(data_sets))}"+
        f"\n\nThe PC values have been added to your data table in {filename}.")
    
    return    
    