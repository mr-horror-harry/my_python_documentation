#This is to read and write with the same file opener

file = open('./tmp_file.txt', 'r+')

print(file.read())

#After reading the pointer is at the end. write : act as append for now
file.write("This is through read and append!\n")

#now pointer at the end. Moving to the start
file.seek(0)
print("Modified content:\n", file.read())

file.close()
