import zipfile

extractor = zipfile.ZipFile('./docs_material.zip','r')
extractor.extractall('docs_material')