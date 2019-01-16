# We will change the color space of input image from BGR to HSV.

import cv2
import numpy as np

img = cv2.imread('input/apple.jpeg')
cv2.imshow('img',img)

cvt_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lower_red = np.array([10,50,50])
upper_red = np.array([230,255,255])
mask = cv2.inRange(cvt_img,lower_red,upper_red)

res = cv2.bitwise_and(img,img,mask=mask)

cv2.imshow('hsv_img',res)

cv2.waitKey(0)
cv2.destroyAllWindows()