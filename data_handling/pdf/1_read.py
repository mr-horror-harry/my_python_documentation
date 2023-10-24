import PyPDF2

#a binary read file pointer
file = open('./sample.pdf', mode='rb')

#read the data
data = PyPDF2.PdfReader(file)
print(len(data.pages)) 

#page indexing
pg5 = data.pages[4] 
pg5_txt = pg5.extract_text() #to extract the data of the page
print(pg5_txt)
