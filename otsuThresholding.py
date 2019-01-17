# Implementing OTSU thresholding 
# OTSU thresholding algorithm is used for segmenting input image into 2 regions, 
# and is much useful if we have BI-MODAL images, i.e; they have two peaks in their histogram. 
# OTSU thresholding yields best result when used on noise-less image. 

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('input/gaussian-noise.png',0)
blur = cv2.GaussianBlur(img,(5,5),0)
ret, thres_img_0 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
ret, thres_img = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
ret, glb_img = cv2.threshold(img,0,255,cv2.THRESH_BINARY)

titles = ['input_img','blur_img','global thresholding', 'OTSU w/o blur', 'OTSU w/ blur']
images = [img,blur,glb_img,thres_img_0,thres_img]

for i in range(1,5):
    plt.subplot(2,2,i),plt.imshow(images[i],'gray')
    plt.title(titles[i])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()