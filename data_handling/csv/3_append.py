import csv

file = open('./sample_written.csv', mode='a', newline='') #newline: to seperate each lines whlie writing

appender = csv.writer(file, delimiter=',') #delimiter: to seperate each fields while writing

mat = [[2,5,8],[4,1,8],[4,6,8],[6,7,3]]

for row in mat:
    appender.writerow(row)
    #write rows for multiple rows as single arguement

file.close()
