import pandas as pd

with pd.ExcelFile('export.xls') as xls:
    df = pd.read_excel(xls)
    df1 = pd.DataFrame(df, columns=['Muhammed MacIntyre'])
for x in df1.values.tolist():
    print(x[0])
