import PIL.Image as img

pto1 = img.open('./house.png')
print(type(pto1))
pto1.show()

pto2  = img.open('./RJB.jpeg')
print(type(pto2))
pto2.show()

# dimensions of the image
print(pto1.size)
#image's filename
print(pto1.filename)
#imgae's format
print(pto1.format_description)

print(pto2.size)
print(pto2.filename)
print(pto2.format_description)

#cropping the image --> tuple arguement
pto1.crop((250, 250, 800, 500)).show() 

#rotating the images
pto1.rotate(90).show()
pto2.rotate(-90).show()

#paste over images
pto1.paste(im=pto2.crop((100, 100, 200, 250)), box=(0, 200))
pto1.show()

pto1.resize((100, 500)).show()