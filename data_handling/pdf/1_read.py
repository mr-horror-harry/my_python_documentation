import PyPDF2

file = open('./sample.pdf')

data = PyPDF2.PdfReader(file)
print(data.numLines) 