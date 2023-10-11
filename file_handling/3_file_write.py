#This python script is to write content to a file
#Method 1:
with open('./tmp_file.txt', mode='w') as file:
    file.write("Hello this mssg is written through file handling write operation!\n")
    file.close()

#This is to append the message to the existing file
#Method 2:
file = open('./tmp_file.txt', 'a')
file.write("Hello this mssg is appended through file handling write operation!\n")
file.close()
