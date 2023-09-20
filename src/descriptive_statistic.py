'''Returns descriptive statistics and visualization for the Iris dataset.'''

import lib
import warnings

    
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