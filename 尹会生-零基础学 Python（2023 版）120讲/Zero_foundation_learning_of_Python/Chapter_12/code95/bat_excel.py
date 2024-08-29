# NOTE: 将目录下所有的excel表格数据集成到一个表中
from pathlib import PurePath, Path

import openpyxl

P = Path('.')
files = [x for x in P.iterdir() if PurePath(x).match("*.xlsx")]
print(files)

example_xlsx = openpyxl.Workbook()
example_sheet = example_xlsx.active

for file in files:
    wb = openpyxl.load_workbook(file)
    ws = wb.active
    for row in ws.iter_rows():
        data_row = []
        for cell in row:
            data_row.append(cell.value)
        example_sheet.append(data_row)

    # 获取全部工作簿
    print(wb.sheetnames)
    # 获取单个工作簿
    print(wb['Sheet'])

example_xlsx.save('example.xlsx')
