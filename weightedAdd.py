# In this we will see how to add images giving weights to each of them, and deciding how much they contribute in the resultant image
# Addition works on the formula, res(x) = (1-a).f1(x) + a.f2(x), where 0 < a < 1 

import cv2
import numpy as np

img1 = cv2.imread('input/3D-Matplotlib.png')
img2 = cv2.imread('input/mainsvmimage.png')

res = cv2.addWeighted(img1,0.5,img2,0.5,0)

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('res',res)

cv2.waitKey(0)
cv2.destroyAllWindows()