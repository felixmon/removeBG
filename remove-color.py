# designed to remove the watermark (red marks) of the pa email

import cv2
import numpy as np

# load the image
img = cv2.imread('input.png')
if img is None:
    print('Could not open or find the image')
    exit(0)

# define the color range to remove
# PAB watermark is 230, 230, 230 to 255, 255, 255 when the background is white
# PAB watermark is 210, 210, 210 to 255, 255, 255 when the background is white and gray 
# PAB watermark is 200, 200, 200 to 255, 255, 255 when the background for the new os
# 0,100,232 to 255, 255, 255 for the kycr (new os)
lower_range = np.array([0,100,232], dtype=np.uint8)
upper_range = np.array([255, 255, 255], dtype=np.uint8)

# create a mask that identifies the pixels within the color range
mask = cv2.inRange(img, lower_range, upper_range)

# remove the color by setting the masked pixels to white
img[mask != 0] = [255, 255, 255]

# save the new image
cv2.imwrite('new_image.png', img)
