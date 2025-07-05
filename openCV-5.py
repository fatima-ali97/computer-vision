import cv2 
import numpy as np 

while True:
    frame = np.zeros(  [ 250,250],dtype=np.uint8)

    frame[:int(250/2),:] = 255
    cv2.imshow('my window',frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break 