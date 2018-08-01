# Image is a 2D array, few basic operation that can be perfomed on images
import cv2
import numpy as np


img = cv2.imread('input/watch.jpg')

# Print Image Diamensions
# width,height,channels = img.shape
# print(width)
# print(height)
# print(channels)

watchFace = img[37:111,107:194]
img[0:74, 0:87] = watchFace
cv2.imshow('watch',img)
cv2.imwrite('output/watchFace.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()