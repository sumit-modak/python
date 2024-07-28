from PIL import Image
 
im = Image.open(r"/home/sumit/grs/python/python.png")
 
left = 155
top = 65
right = 360
bottom = 270
 
im1 = im.crop((left, top, right, bottom))

im1.show()
