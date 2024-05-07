#file=open('./file.txt')
file=open('./file.java')

print(file.read())
file.seek(0)

data=file.read()
print(data)
file.seek(0)

lines = file.readlines()
print(type(lines))

file.close()
