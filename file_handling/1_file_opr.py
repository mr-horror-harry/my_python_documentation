file=open('/Users/MariaAntonyHarishJ/Documents/Programming/my_python_documentation/file_handling/file.txt')

print(file.read())
file.seek(0)

data=file.read()
print(data)
file.seek(0)

print(file.readlines())

file.close()