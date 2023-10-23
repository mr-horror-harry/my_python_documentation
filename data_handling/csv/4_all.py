import csv

file = open('./wholesale-trade-survey-june-2023-quarter-csv.csv')
data = csv.reader(file)
li = list(data)

file2 = open('./written.csv', mode='w+', newline='')
writer = csv.writer(file2, delimiter=':')

for line in li[:50]:
    writer.writerow(line)

# f=open('./written.csv')
data_read = csv.reader(file2)
li=list(data_read)
print(li)
