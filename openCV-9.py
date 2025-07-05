import cv2 


width = 640
height = 360


cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)

cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)

cam.set(cv2.CAP_PROP_FPS,30)

cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    ignore,frame = cam.read() 
    frameROI = frame[:,220:]
    frameROIGray = cv2.cvtColor(frameROI, cv2.COLOR_BGR2GRAY)
    frameROIGray2BGR =  cv2.cvtColor(frameROIGray, cv2.COLOR_GRAY2BGR)
    cv2.imshow('my ROI', frameROIGray)
    cv2.moveWindow('my ROI',0,0)

    frame[:,220:] = frameROIGray2BGR
    """ Show a frame """
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',600,0)

    """ to exit press q """
    if cv2.waitKey(1) & 0xff == ord('q') : 
        break 

cam.release()