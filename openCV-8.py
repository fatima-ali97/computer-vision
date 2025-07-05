import cv2 
import numpy as np 
import time

width = 640
height = 360


cam=cv2.VideoCapture(1,cv2.CAP_DSHOW)

cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)

cam.set(cv2.CAP_PROP_FPS,30)

cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))


start_time = time.time()
fpsFilter =30
time.sleep(0.3)

while True:
    secondsPassed =  time.time() - start_time 
    fps = 1/secondsPassed

    # number in the places of 0.9 and 0.1 need to be equal to 1.
    fpsFilter = fpsFilter *0.9+fps*0.1
    start_time =time.time()


    
    ignore,frame = cam.read() 

    fpsCount = f"fps is {int(fpsFilter)}"

    
    cv2.putText(frame, fpsCount, (100,60), cv2.FONT_HERSHEY_DUPLEX,1,(0,0,0),1)
    
    """ Show a frame """
    cv2.imshow('my WEBcam', frame)
    

    if cv2.waitKey(1) & 0xff == ord('q'):
        break


cam.release()