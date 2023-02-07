import pandas as pd
import numpy as np
d1 = pd.read_excel("C://Users/user790/Desktop/Product data.xlsx",sheet_name = "Data1")
d2 = pd.read_excel("C://Users/user790/Desktop/Product data.xlsx",sheet_name = "Data2")
print(d1.compare(d2))
d3 = np.where(d1['Price']>d2['Price'],True,False)
d4 = np.where(d1['Price']<d2['Price'],True,False)
d5 = np.where(d1['Price']==d2['Price'],True,False)
d6 = np.where(d1['Price']>d2['Price'],True,d2['Price']-d1['Price'])
print(d3)
print(d4)
print(d5)
print(d6)
print(d6.to_excel("demo.xlsx"))