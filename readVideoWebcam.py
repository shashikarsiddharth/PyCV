# Read video from webcam

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

while True:
    ret, frame = cap.read()

    # converting gray scale
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # cv2.imshow('frame_gray',gray)
    out.write(frame)
    cv2.imshow('frame_color',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
out.release()
cv2.destroyAllWindows()