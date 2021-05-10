from PIL import Image,ImageFilter

img=Image.open('./sample_image/vd1.jpg')
filtered_image=img.filter(ImageFilter.BLUR)

img2=img.convert('L')#filtered the image in black and white
img2.thumbnail((300,300))
c=img2.rotate(180)#rotation of image
#filtered_image.save("new.jpg")
c.save("red.png","png")
c.show()
#print(img.format)
#print(img.size)
#print(img.mode)
#print(dir(img))
#print(img.load)
#print(img.show)