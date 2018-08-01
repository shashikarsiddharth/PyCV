# Marking objects in images

import cv2
import numpy as np

img = cv2.imread('input/watch.jpg',cv2.IMREAD_COLOR)

# Drawing a line
# parameters in following sequence -> image,start_point,end_point,color(BRG),line_width
cv2.line(img,(0,0),(150,150),(255,255,255),10)
cv2.imwrite('output/lineWatch.jpg',img)

# Drawing a rectangle
# parameters in following sequesnce -> image,top_left coordinate,bottom_right coordinate,color(BGR),line_width
cv2.rectangle(img,(15,25),(200,150),(0,0,255),5)
cv2.imwrite('output/rectangleWatch.jpg',img)


cv2.imshow('watch',img)
cv2.waitKey(0)
cv2.destroyAllWindows()