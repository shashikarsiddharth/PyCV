# Reading image using OpenCV
import cv2
import numpy as np


img = cv2.imread('test.jpeg')
cv2.imshow('apple image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
