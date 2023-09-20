'''Returns descriptive statistics and visualization for the Iris dataset.'''

import lib
import warnings
import seaborn as sns
def save_plot(file_name, plot):

    if (file_name[-3:] != "png") | (file_name[-3:] != "jpg"):
        file_name += ".png"

    if not isinstance(plot, sns.FacetGrid):
        raise TypeError("Plot must be in Seaborn FacetGrid form")

    plot.savefig(
        "plots/" + f"{file_name}"
    )
    
def main():
    '''Main function for descriptive statistics and visualization'''

    warnings.filterwarnings('ignore', category=FutureWarning)

    # Import dataset
    iris_data = lib.import_iris("iris_data.csv")

    # Print descriptive statistics
    summary = lib.describe_iris(iris_data)
    print(summary)

    # Generate and save visualization
    plot = lib.visualize_iris(iris_data)
    lib.save_plot("SepalLengthbySpecies_boxplot.png", plot)

if __name__ == "__main__":
    main()