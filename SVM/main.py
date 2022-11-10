import pandas as pd
from sklearn.datasets import load_iris

# Load Iris datasets
iris_dataset: pd.DataFrame = load_iris()
# Analyst data
print(iris_dataset)
# Distribution of target class colum
print(iris_dataset['target_class'].value_counts())
