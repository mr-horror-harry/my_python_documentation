import csv

#opening a file
file = open('./wholesale-trade-survey-june-2023-quarter-csv.csv', encoding='utf-8')

#read the data 
data = csv.reader(file)

#list of data
li = list(data)

print(li[0],"\n", li[1])
print(len(li))

for line in li[:10]:
    print(line)

#close the file : indiectly file pointer to begin
file.close()
