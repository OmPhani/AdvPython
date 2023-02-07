import openpyxl
from openpyxl import load_workbook
from openpyxl.drawing.image import Image

workbook = load_workbook(filename = "C://Users/user790/Desktop/Product data.xlsx")
sheet = workbook.active

logo = Image("C://Users/user790/Desktop/HCLTech.jpg")

logo.height = 150
logo.width = 150

sheet.add_image(logo,"D10")
workbook.save(filename="C://Users/user790/Desktop/Logoadding.xlsx")