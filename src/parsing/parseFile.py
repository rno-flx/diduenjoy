# Function that parses the file and returns the data in variables

import openpyxl

def parseFile(file):
    dataframe = openpyxl.load_workbook(file)
    sheet = dataframe.active
    for row in range(0, sheet.max_row):
        for col in sheet.iter_cols(1, sheet.max_column):
            print(col[0].value)
