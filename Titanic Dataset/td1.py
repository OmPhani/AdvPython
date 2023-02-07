import pandas as pd
import numpy as np
df = pd.read_csv('train.csv')
grouped_data = df.groupby('Sex')
print(grouped_data.describe())
print(pd.crosstab(index = df['Sex'],columns = df['Survived']))
print(pd.pivot_table(df,index = ['Sex','Age'],aggfunc = np.sum))
print("HELLO")
print(df.sort_values(by = ['Pclass','Age'],ascending = False))
df['Survived']= df["Survived"]