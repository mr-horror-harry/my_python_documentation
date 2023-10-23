import csv

file = open('./sample_written.csv', mode='w', newline='')

writer = csv.writer(file, delimiter=',')

mat=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for row in mat:
    writer.writerow(row)

file.close()