import pandas as pd
import numpy as np
import math
df = pd.read_csv("C://Users/user790/Downloads/Marks_problem.csv")
print(df)

def marks():
    df['Total'] = df.apply(np.sum,axis=1)
    print(df)
    for i in range of iloc[:]:
marks()

if __name__ == '__main__':
    main()

'''
class Readcsv():
    def create_df(self,path):
        self.path = path
        self.df = pd.DataFrame(self.path)
        self.df['Total'] = df.iloc[:].sum(axis=1)
        df['avg'] = df['Total']/6
        df.iloc[:20]
        print(df)
    create_df()
'''