import csv

with open('cc.csv', "rt", encoding='utf-8') as f:
    f_csv = csv.reader(f)
    # headers = next(f_csv) 有首行的时候需要用这个跳过首行
    for row in f_csv:
        print(row)
