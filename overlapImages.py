# Overlapping images on one another
import cv2
import numpy as np

img1 = cv2.imread('input/3D-Matplotlib.png')
img2 = cv2.imread('input/mainlogo.png')

rows,cols,channels = img2.shape
roi = img2[0:rows,0:cols]

# Converting color to gray scale
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

# Thresholding images
# Parameters are in the following order grayImage, min_value, max_value, threshold_functions
res, mask = cv2.threshold(img2gray,220,255,cv2.THRESH_BINARY)
res_inv, mask_inv = cv2.threshold(img2gray,220,255,cv2.THRESH_BINARY_INV)

cv2.imshow('mask',mask)
cv2.imshow('mask_inv',mask_inv)

# bitwsie_and operator
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

# adding two images
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows,0:cols] = dst

cv2.imshow('final_img',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()