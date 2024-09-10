# Generate a 2D or 3D scatter plot using provided CSV file (Informatics)

Create either a 2d or 3d scatter plot from a CSV input file, which might optionally display the points colored by another column. 

## Input
* file - The CSV file containing data to plot
* x_column_name - The column name in the CSV file to be used as the x-axis
* y_column_name - The column name in the CSV file to be used as the y-axis
* z_column_name - If provided, this will be the column name in the CSV file to be used as the z-axis, and the scatter plot will be 3D
* color_column_name - If provided, this will be the column name in the CSV file to be used to color the points in the scatter plot. Depending whether this column data is categorical or continuous, a color legend or a color bar will be displayed respectively.
* additional_params - An optional dictionary that contains additional parameters for the scatter plot.

## Output
A scatter plot in the svg format

## Setup
### requirements
pandas
matplotlib
