import csv

csv_file = open("./get.csv", "r", encoding="UTF-8", errors="", newline="" )
#リスト形式

f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
header = next(f)
print(header)
for row in f:
    #rowはList
    #row[0]で必要な項目を取得することができる
    print(row)