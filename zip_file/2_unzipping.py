import zipfile

#extract the files
extractor = zipfile.ZipFile('./docs_material.zip','r')
extractor.extractall('docs_material')