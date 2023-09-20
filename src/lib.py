import os
import pandas as pd
import seaborn as sns

def import_iris(file_name: str):
    '''Converts csv file to dataframe'''

    if not isinstance(file_name, str):
        raise TypeError("file_name must be a string")
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
    new_path = parent_dir + "/data"
    file_path = os.path.join(new_path, file_name)

    try:
        iris_df = pd.read_csv(file_path)
        cols = set(iris_df.columns) - {'Id'}
        reduced_iris = iris_df[list(cols)]
        return reduced_iris
    
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"The file ({file_name}) was not found.") from exc
    
def describe_iris(iris_df):
    '''Returns pandas descriptive statistics on dataframe.'''

    if not isinstance(iris_df, pd.DataFrame):
        raise TypeError("Iris data must be in pandas dataframe form")
    iris_stats = iris_df.describe().round(2)
    print(type(iris_stats))
    return iris_stats

def visualize_iris(iris_df):
    '''Visualize sepal length distribution for each species.'''

    if not isinstance(iris_df, pd.DataFrame):
        raise TypeError("Data must be in pandas dataframe form")

    g = sns.catplot(
        x="Species", 
        y="SepalLengthCm", 
        data=iris_df,
        kind="box",
        height=6, 
        aspect=1.3
    )
    
    g.set(
        title="Boxplot of Sepal Length by Species", 
        xlabel="Species", 
        ylabel = "Sepal Length (Cm)"
    )
    
    return g
