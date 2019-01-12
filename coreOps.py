# Implementing core operations on images
import cv2
import numpy as np

# Getting pixels values and assigning it.
img = cv2.imread('input/apple.jpeg')
cv2.imshow('img',img)
img[123,123] = [0,0,0]
cv2.imshow('altered_img',img)

# Accessing image properties
print('Image properties')
print("image shape -> (r,c,channels): ",img.shape)
print("total # of pixels: ",img.size)
print("pixel value types: ",img.dtype)

# Getting ROI (Region of Interest)
region = img[200:250,200:250]
img[150:200, 150:200] = region
cv2.imshow('ROI_img',img)

# Splitting image into different channels
b,g,r = cv2.split(img)
cv2.imshow('b',b)
cv2.imshow('g',g)
cv2.imshow('r',r)

# Merging splits into single image
merged = cv2.merge((b,g,r))
cv2.imshow('merged',merged)

cv2.waitKey(0)
cv2.destroyAllWindows()