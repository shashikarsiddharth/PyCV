# Weighted Image Addition
import cv2
import numpy as np

img1 = cv2.imread('input/3D-Matplotlib.png')
img2 = cv2.imread('input/mainsvmimage.png')

# Parameters are in the following order image_1, contribution in final image, image_2, contribution in final image, gamma
# Gamma is the measurement of light
weighted = cv2.addWeighted(img1,0.6,img2,0.4,0)
cv2.imshow('weightedAdd',weighted)

cv2.waitKey(0)
cv2.destroyAllWindows()
