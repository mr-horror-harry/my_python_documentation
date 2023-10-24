import csv

#read mode pointer
file = open('./wholesale-trade-survey-june-2023-quarter-csv.csv')
data = csv.reader(file)
li = list(data)
file.close()

#pointer to write and read
file2 = open('./written.csv', mode='w+', newline='')
writer = csv.writer(file2, delimiter=':')

for line in li[:50]:
    writer.writerow(line)

file2.seek(0) #to move the file pointer to the beginning

# f=open('./written.csv', mode='r') 
# or close and open to move pointer to initial

data_read = csv.reader(file2)
print(list(data_read))

file2.close()