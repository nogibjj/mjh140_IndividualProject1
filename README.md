# Descriptive Statistics with Pandas and Seaborn   
[![Install](https://github.com/nogibjj/mjh140_IndividualProject1/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/mjh140_IndividualProject1/actions/workflows/install.yml)   [![Format](https://github.com/nogibjj/mjh140_IndividualProject1/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/mjh140_IndividualProject1/actions/workflows/format.yml)   [![Linting](https://github.com/nogibjj/mjh140_IndividualProject1/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/mjh140_IndividualProject1/actions/workflows/lint.yml)   [![Unit Tests](https://github.com/nogibjj/mjh140_IndividualProject1/actions/workflows/unitTests.yml/badge.svg)](https://github.com/nogibjj/mjh140_IndividualProject1/actions/workflows/unitTests.yml)



## Summary:

This project uses the Pandas package for generating descriptive statistics on the Iris Species dataset. The Seaborn package was used to create a boxplot visualization of Sepal Length broken down by Species. A Jupyter Notebook is included in this repository to walk through the functions used to generate the descriptive statistics and visualzation. For more info on the Iris Species dataset, visit the following link:

https://www.kaggle.com/datasets/uciml/iris?resource=download

## Structure

```text
├── .devcontainer
│   ├── Dockerfile
│   └── devcontainer.json
├── data
│   └── iris_data.csv
├── .github/workflows
│   ├── format.yml
│   ├── install.yml
│   ├── lint.yml
│   └── unitTests.yml
├── .gitignore
├── Makefile
├── plots
│   ├── .test_cases_plot.png
│   └── SepalLengthbySpecies_boxplot.png
├── README.md
├── requirements.txt
├── src
│   ├── __init__.py
│   ├── lib.py
│   ├── script.py
│   └── statistics_notebook.ipynb
└── tests
    ├── __init__.py
    ├── test_lib.py
    └── test_script.py

```

## Results:

The following table of descriptive statistics was outputed from the `describe_iris` function within `src/descriptive_statistic.py`:

|          | PetalLengthCm | PetalWidthCm | SepalWidthCm | SepalLengthCm |
| -------- | ------------- | ------------ | ------------ | ------------- |
|count     |    150.00     |   150.00    |   150.00     |    150.00 |
|mean      |      3.76     |     1.20    |     3.05     |      5.84 |
|std       |      1.76     |     0.76    |     0.43     |      0.83 |
|min       |      1.00     |     0.10    |     2.00     |      4.30 |
|25%       |      1.60     |     0.30    |     2.80     |      5.10 |
|median    |      4.06     |     1.25    |     3.03     |      5.82 |
|75%       |      5.10     |     1.80    |     3.30     |      6.40 |
|max       |      6.90     |     2.50    |     4.40     |      7.90 |


The following boxplot visualization for Sepal Length distribution by Species was created from the `visualize_iris` function within `src/descriptive_statistic.py`:

<p align = "center"><img src = "https://github.com/nogibjj/mjh140---MiniProject2/blob/main/SepalLength_by_Species.png" width = 500px></p>
