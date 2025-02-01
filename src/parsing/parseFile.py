# Function that parses the file and returns the data in variables

import openpyxl

def parseFile(file):
    dataframe = openpyxl.load_workbook(file)
    sheet = dataframe.active
    data = []
    for row in range(2, sheet.max_row + 1):
        row_data = {
            'id': sheet.cell(row=row, column=1).value,
            'name': sheet.cell(row=row, column=2).value,
            'price': sheet.cell(row=row, column=3).value,
            'ref': sheet.cell(row=row, column=4).value,
            'packageId': sheet.cell(row=row, column=5).value,
            'warranty': sheet.cell(row=row, column=6).value,
            'duration': sheet.cell(row=row, column=7).value
        }
        data.append(row_data)

    return data

