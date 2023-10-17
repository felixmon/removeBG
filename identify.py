from PIL import Image

# load the image
img = Image.open("image.png")

# get the RGB values of all pixels in the image
rgb_values = list(img.getdata())

# get the unique RGB values
unique_rgb_values = set(rgb_values)

# print the unique RGB values
for rgb in unique_rgb_values:
  print(rgb)
