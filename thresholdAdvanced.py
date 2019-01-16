# Image thresholding

import cv2
import numpy as np
from matplotlib import pyplot as plt 

img = cv2.imread('input/bookpage.jpg',0)
ret,thres1 = cv2.threshold(img,107,255,cv2.THRESH_BINARY)
ret,thres2 = cv2.threshold(img,107,255,cv2.THRESH_BINARY_INV)
ret,thres3 = cv2.threshold(img,107,255,cv2.THRESH_TRUNC)
ret,thres4 = cv2.threshold(img,107,255,cv2.THRESH_TOZERO)
ret,thres5 = cv2.threshold(img,107,255,cv2.THRESH_TOZERO_INV)

# Adaptive Thresholding
thres6 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
thres7 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

titles = ['Input img','Binary','Binary_Inv','Trunc','To_zero','To_zero_inv']
images = [img,thres1,thres2,thres3,thres4,thres5]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
plt.show()

cv2.imshow('adaptive_img_mean',thres6)
cv2.imshow('adaptive_img_gaussian',thres7)

cv2.waitKey(0)
cv2.destroyAllWindows()