import csv

#write file pointer
file = open('./sample_written.csv', mode='w', newline='')

#csv writer --> pen
writer = csv.writer(file, delimiter=',')

mat=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
#wrie to file
for row in mat:
    writer.writerow(row)

#closing the file
file.close()