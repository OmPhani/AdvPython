from dataclasses import dataclass
from openpyxl import Workbook
wb = Workbook()
sheet = wb.active
@dataclass
class People():
    name:str
    no: int
    age: int
p = [People('steve',1,28), People('Raju',2,34),People('Rahul',3,25)]
data = [[p.name,p.no,p.age]for p in p]
for d in data:
    sheet.append(d)
    print(p)
wb.save("C://Users/user790/Desktop/dataclassdata.xlsx")