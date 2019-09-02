import csv
import datetime
from Column import Column

inputFileName = input('input')
firstTime = datetime.datetime.now()
with open(inputFileName, encoding="utf-8", newline='') as csvFile:
    rows = csv.reader(csvFile)
    dataArray = []
    for row in rows:
        if len(row) != 6:
            continue

        memo = row[5]
        if not Column.check(memo):
            continue

        data = row[1] + ","
        data += Column.createMemo(memo)
        dataArray.append(data)

outputFileName = inputFileName.replace('.csv', '') + '_output.csv'

with open(outputFileName, 'w', newline='') as csvFile2:
    writer = csv.writer(csvFile2)
    writer.writerow(['日期和時間', '帳戶名稱', '工作站名稱', '來源網路位址', '登入程序', '驗證封裝'])
    for data in dataArray:
        writer.writerow(data.split(','))

nowTime = datetime.datetime.now()
sec = nowTime - firstTime
print(sec)
