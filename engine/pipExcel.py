import sys, csv, shutil, os, json, openpyxl, re
from flask import Flask
from openpyxl import Workbook
from openpyxl import load_workbook

scores = json.loads(sys.argv[1])

wb = load_workbook(filename = './excelOutputs/output-test.xlsx')
ws = wb['Caracteristicas']
print(ws['B1'].value)

ws['A1'].value = scores['UX']

wb.save('./excelOutputs/output-test.xlsx') 

sys.stdout.flush()
