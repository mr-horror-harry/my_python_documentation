#file=open('/home/mitsuser/my_python_documentation/file_handling/file.txt')
file=open('/home/m/Documents/myGitHub/my_python_documentation/file_handling/file.java')

print(file.read())
file.seek(0)

data=file.read()
print(data)
file.seek(0)

print(file.readlines())

file.close()
