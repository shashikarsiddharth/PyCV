# Writing text on images

import cv2

img = cv2.imread('input/apple.jpeg')

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Python-3.x',(10,50),font,1,(0,0,203),2,cv2.LINE_AA)
cv2.imshow('input_img',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

