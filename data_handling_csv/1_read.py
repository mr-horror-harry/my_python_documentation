import csv

file = open('./wholesale-trade-survey-june-2023-quarter-csv.csv', encoding='utf-8')

data = csv.reader(file)

li = list(data)

print(li[0],"\n", li[1])
print(len(li))

for line in li[:10]:
    print(line)

file.close()
