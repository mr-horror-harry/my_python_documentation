file=open('/home/mitsuser/my_python_documentation/file_handling/1_file_opr.py')

print(file.read())
file.seek(0)

data=file.read()
print(data)
file.seek(0)

print(file.readlines())

file.close()
