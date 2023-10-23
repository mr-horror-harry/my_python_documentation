from PIL import Image as img

blue = img.open('./blue.png')
blue.show()

#saving images
blue.crop((50, 50, 100, 100)).save('./cropped_blue.png')
blue_cropped = img.open('./cropped_blue.png') 
blue_cropped.show()

#paste and save
house = img.open('./house_copy.png')
blue.show()
house.paste(im=blue, box=(50, 50))
house.save('./blue_house.png')
img.open('./blue_house.png')

#opacity of images
dull = img.open('./RJB.jpeg')
dull = dull.convert('RGB')
dull.putalpha(10)
dull.save('./dull_img.png') # or dull.save('./dull_img.png', format='PNG')
img.open('./dull_img.png').show()