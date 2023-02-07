import pandas as pd
import numpy as np
import math

df = pd.read_csv("C://Users/user790/Downloads/Marks_problem.csv")
print(df)
df['Total'] = df.iloc[:].sum(axis = 1)

