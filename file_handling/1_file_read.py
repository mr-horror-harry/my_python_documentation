#file=open('./file.txt')
file=open('./file.java')

print(file.read())
file.seek(0)

data=file.read()
print(data)
file.seek(0)

print(file.readlines())

file.close()
