with open('/home/m/Documents/myGitHub/my_python_documentation/file_handling/file.java', mode='r') as file:

    print(file.read())

    file.seek(0)
    file.close()

