from PIL import Image as img

blue = img.open('./blue.png')
blue.show()

blue.crop((50, 50, 100, 100)).save('./cropped_blue.png')
blue_cropped = img.open('./cropped_blue.png')
blue_cropped.show()