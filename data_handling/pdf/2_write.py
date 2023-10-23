import PyPDF2

#read file pointer
file = open('./sample.pdf', 'rb')
data = PyPDF2.PdfReader(file)

pg3 = data.pages[6]
pg3_txt = pg3.extract_text()
print(pg3_txt)

#write file pointer
pdf_writer = PyPDF2.PdfWriter()
pdf_writer.add_page(pg3) #unextracted data page adding

file2 = open('./sample_written.pdf', 'wb+')
pdf_writer.write(file2)

#read data with same pointer
file2.seek(0)
data2 = PyPDF2.PdfReader(file2)

pg1 = data2.pages[0]
pg1_txt = pg1.extract_text()
print(pg1_txt)