import PyPDF2

file = open('./sample.pdf', mode='rb')

data = PyPDF2.PdfReader(file)
print(len(data.pages)) 

pg5 = data.pages[4] 
pg5_txt = pg5.extract_text()
print(pg5_txt)