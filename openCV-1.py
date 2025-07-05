import cv2 
""" launch the camera """
cam=cv2.VideoCapture(0)

while True :
    """ Read a frame """
    ignore, frame =cam.read()

    """ to make the video BLACK & WHITE"""
    grayFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    """ Show a frame """
    cv2.imshow('my WEBcam', grayFrame)

    cv2.moveWindow('my WEBcam',0,0)

    """ to exit press q """
    if cv2.waitKey(1) & 0xff == ord('q') : 
        break 

cam.release()
cv2.destroyAllWindows()
