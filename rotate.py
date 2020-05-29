from PIL import Image

# image Rotate 180

image = Image.open("image_r400.png")
image_rot180 = image.rotate(180)
image_rot180.save("image_rot180.png")
image_rot180.show()

# image Rotate 90

image = Image.open("image_r400.png")
image_rot90 = image.rotate(90)
image_rot90.save("image_rot90.png")
image_rot90.show()