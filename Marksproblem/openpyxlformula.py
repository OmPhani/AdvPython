import openpyxl
#from openpyxl.utils import FORMULAE
wb = openpyxl.load_workbook("C://Users/user790/Desktop/Product data.xlsx")
sheet = wb.active
sheet["A11"] = '=SUM(A1:A10)'
#sheet.append['A11'] = SUM
wb.save("C://Users/user790/Desktop/Sumformula.xlsx")