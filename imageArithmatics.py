# Adding images 

import cv2
import numpy as np

img1 = cv2.imread('input/3D-Matplotlib.png')
img2 = cv2.imread('input/mainsvmimage.png')

add = img1+img2
cv2.imshow('add',add)
cv2.waitKey(0)
cv2.destroyAllWindows()

