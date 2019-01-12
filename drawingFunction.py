# Drawing geometric functions in images using OpenCV

import numpy as np
import cv2

def drawLine(img):
    '''
    Draws a line across the diagonal. 
    '''
    res = cv2.line(img,(0,0),(img.shape[0],img.shape[1]),(204,244,21),3)
    return res

def drawRectangle(img):
    '''
    Draws a rectangle in the image, around the object.
    '''
    res = cv2.rectangle(img,(70,200),(102,140),(244,24,145),2)
    return res

def drawCircle(img):
    '''
    Draws a circle on image.
    '''
    res = cv2.circle(img,(120,130),50,(24,210,224),2)
    return res

def drawEllipse(img):
    '''
    Draws ellipse in the image.
    '''
    res  = cv2.ellipse(img,(256,256),(100,50),0,0,102,125,-1)
    # print(cv2.ellipse.__doc__)
    return res

img = cv2.imread('input/apple.jpeg')
cv2.imshow('input_img',img)

res = drawLine(img)
res = drawRectangle(res)
res = drawCircle(res)
res = drawEllipse(res)
cv2.imshow('result_img',res)



cv2.waitKey(0)
cv2.destroyAllWindows()
