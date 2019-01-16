# Applying arithmetic operations on images, such as add, add_weight.

'''
Note: There is a difference b/w Numpy addition i.e; res = img1 + img2, and opencv add i.e; cv2.add()
as Numpy addition is modulo operation whereas cv2.add is a saturated operation.
'''

import cv2
import numpy as np

img_1 = cv2.imread('input/mainsvmimage.png')
img_2 = cv2.imread('input/3D-Matplotlib.png')

res_numpy_add = img_1 + img_2
cv2.imshow('numpy add', res_numpy_add)

res_cv_add = cv2.add(img_1,img_2)
cv2.imshow('cv2 add', res_cv_add)

cv2.waitKey(0)
cv2.destroyAllWindows()
