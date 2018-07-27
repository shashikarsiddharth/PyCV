# Reading image using OpenCV
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('apple.jpg')
cv2.imshow('apple image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
