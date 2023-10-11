with open('./file.java', mode='r') as file:

    print(file.read())

    file.seek(0)
    file.close()

