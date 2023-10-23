import csv

file=open('./written.csv')

data = csv.reader(file)
print(list(data))