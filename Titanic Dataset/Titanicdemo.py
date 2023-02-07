import pandas as pd
df = pd.read_csv('train.csv')
print(df.head())
print(df.tail())
print(df.describe(include = "all"))
print(df.drop(['Ticket'],axis=1,inplace=True))
print(df.head())

print(df.iloc[10:20])

print(df[df.columns[3:5]] )
print(df.dtypes)
print(df.columns)
print(df['Sex'].describe())
print(df['Embarked'].describe())