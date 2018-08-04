# Image thresholding

import cv2
import numpy as np

img = cv2.imread('input/bookpage.jpg')
img2gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow('original_image',img)
# cv2.imshow('gray_image',img2gray)

# Threshold Color Image 
ret_color,thres_color = cv2.threshold(img,10,255,cv2.THRESH_BINARY)
cv2.imshow('threshold_image',thres_color)

# Threshold Gray Image
ret_gray,thres_gray = cv2.threshold(img2gray,10,255,cv2.THRESH_BINARY)
cv2.imshow('threshold_image 2',thres_gray)

# Adaptive Thresholding
# Parameters are in the following orders 
# adaptiveThreshold(src_img, dst_img, maxValue, adaptiveMethod, thresholdType, blockSize, C)
# blocksize -> integer variable, depicting pixel neighbourhood for calculating the threshold values.
thres_ada = cv2.adaptiveThreshold(img2gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
cv2.imshow('adaptiveThreshold',thres_ada)


cv2.waitKey(0)
cv2.destroyAllWindows()