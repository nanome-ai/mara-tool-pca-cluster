'''Create either a 2D or 3D scatter plot from a CSV input file, which might optionally display the points colored by another column. '''
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def create_timestamp() -> str:
  # helper function to create a unique timestamp
  dt = str(datetime.now())
  return dt.replace("-", "_").replace(":", "_").replace(" ", "_")

def run(file, x_column_name, y_column_name, z_column_name="none", color_column_name="none", additional_params={}):

    ## Read data from a CSV file
    data_df = pd.read_csv(file)
    mode = "2D"
    color_mode = "none"

    ## Check if the columns are present
    assert x_column_name in data_df.columns, f"Column {x_column_name} not found in the data"
    assert y_column_name in data_df.columns, f"Column {y_column_name} not found in the data"
    if z_column_name != "none":
        assert z_column_name in data_df.columns, f"Column {z_column_name} not found in the data. \
Please make sure column names match the data in the CSV file if you want to create a 3D scatterplot!"
        mode = "3D"
    if color_column_name != "none":
        assert color_column_name in data_df.columns, f"Column {color_column_name} not found in the data. \
Please make sure column names match the data in the CSV file if you want to color the points by a column!"
        # decide whether the color data is categorical or continuous. Only float type is considered continuous
        if pd.api.types.is_float_dtype(data_df[color_column_name]):
            color_mode = "continuous"
        else:
            color_mode = "categorical"

    ## Create the Plot based on different modes
    ## set font sizes
    plt.rcParams.update({'font.size': 14})
    if color_mode == "none":
        if mode == "2D":
            fig, ax = plt.subplots()
            ax.scatter(data_df[x_column_name], data_df[y_column_name], **additional_params)
        else:
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.scatter(data_df[x_column_name], data_df[y_column_name], data_df[z_column_name], **additional_params)

    elif color_mode == "continuous":
        if mode == "2D":
            fig, ax = plt.subplots()
            scatter = ax.scatter(data_df[x_column_name], data_df[y_column_name], c=data_df[color_column_name], **additional_params)
            colorbar = fig.colorbar(scatter, ax=ax)
        else:
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            scatter = ax.scatter(data_df[x_column_name], data_df[y_column_name], data_df[z_column_name], c=data_df[color_column_name], **additional_params)
            colorbar = fig.colorbar(scatter, ax=ax)  
        # show colorbar name
        colorbar.set_label(color_column_name)

    elif color_mode == "categorical":
        categories = sorted(data_df[color_column_name].unique())
        if mode == "2D":
            fig, ax = plt.subplots()
            for cat in categories:
                ax.scatter(data_df[x_column_name][data_df[color_column_name] == cat], data_df[y_column_name][data_df[color_column_name] == cat], 
                           label=f"{color_column_name}={cat}", **additional_params)
        else:
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            for cat in categories:
                ax.scatter(data_df[x_column_name][data_df[color_column_name] == cat], data_df[y_column_name][data_df[color_column_name] == cat],
                            data_df[z_column_name][data_df[color_column_name] == cat], label=f"{color_column_name}={cat}", **additional_params)
        # show legend
        ax.legend()


    
    ## Set the Labels
    ax.set_xlabel(x_column_name)
    ax.set_ylabel(y_column_name)
    if mode == "3D":
        ax.set_zlabel(z_column_name)

    ## Save figure
    filename = f"scatter.{create_timestamp()}.svg"
    plt.savefig(filename)
    print(f"{mode} scatter plot saved as {filename}")
    if color_mode != "none":
        print("Points are colored by", color_column_name)


if __name__ == "__main__":
    run("../test_data/after_PCA_K-Means_clustered_3_2024_09_09_17_22_35.486157.csv", "PC1", "PC2", color_column_name="pValue")