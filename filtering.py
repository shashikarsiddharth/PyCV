# Implementation of different blurring techniques using filters for ex: 
#   1) Average filter
#   2) Gaussian filter
#   3) Median Filter
#   4) Bilateral Filter

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('input/apple.jpeg')
cv2.imshow('i',img)

# Average Filter
avg_kernel = np.ones((5,5),np.float32)/25
avg_res = cv2.filter2D(img,-1,avg_kernel) 

# Gaussian Filter
# gau_kernel = np.array([[1,2,1],[2,4,2],[1,2,1]])/16
# gau_res = cv2.filter2D(img,-1,gau_kernel)
gau_res = cv2.GaussianBlur(img,(5,5),0)

# Median Filter
med_res = cv2.medianBlur(img,5)

titles = ['input_img','avg_filter_res','gaussian_filter_res','median_filter_res']
images = [img,avg_res,gau_res,med_res]

for i in range(0,4):
    plt.subplot(2,2,i+1),plt.imshow(images[i])
    plt.title(titles[i])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()