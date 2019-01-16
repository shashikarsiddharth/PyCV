# Bitwise operations in image processing, AND, OR, NOT, XOR are few of the bitwise operations.

import cv2

img1 = cv2.imread('input/apple.jpeg')
img2 = cv2.imread('input/moon.jpg')

r,c,ch = img1.shape
roi = img1[0:r,0:c]

img2gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray_scale',img2gray)

ret, mask = cv2.threshold(img2gray,205,255,cv2.THRESH_BINARY)
cv2.imshow('thresholded,mask)

mask_inv = cv2.bitwise_not(mask)
cv2.imshow('mask_inv',mask_inv)

img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
cv2.imshow('img1_bg',img1_bg)

img1_fg = cv2.bitwise_and(img1,img1,mask = mask)
cv2.imshow('img1_fg',img1_fg)

dst = cv2.add(img1_bg,img1_fg)
img2[0:r,0:c] = dst

cv2.imshow('overlap_img',img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
