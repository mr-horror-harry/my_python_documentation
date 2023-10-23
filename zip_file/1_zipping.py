import zipfile

#to create a zip
zip_var = zipfile.ZipFile('./docs_material.zip', 'w')

files_list = ['c_1', 'cpp_2', 'java_3.cpp'] #creates a folder
#to add the folders into zip
for file in files_list:
    zip_var.write('./', arcname=file, compress_type=zipfile.ZIP_DEFLATED)

zip_var.close()