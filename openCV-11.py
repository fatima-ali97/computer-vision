import cv2 


width = 640
height = 360


cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)

cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)

cam.set(cv2.CAP_PROP_FPS,30)

cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))


evt = 0
cv2.namedWindow('my WEBcam')
def handleMouseClick(event, Xposition, Yposition,flags,params):
    
    global pnt
    global evt 
    if event == cv2.EVENT_LBUTTONDOWN:
        evt = event # 1 
        pnt=(Xposition,Yposition)
    if event == cv2.EVENT_LBUTTONUP:
        print("") # 4
    if event == cv2.EVENT_RBUTTONDOWN:
        evt = event # up is 5 ## down is 5 -- sometimes its 2 idk why ??
        print("cliked", evt,event)       

cv2.setMouseCallback('my WEBcam', handleMouseClick)

while True:
    ignore,frame = cam.read() 

    if evt == 1 or evt==4 :
       cv2.circle(frame,pnt,25,(255,0,0),2)
    if evt ==5 or evt == 2:
        break
    """ Show a frame """
    cv2.imshow('my WEBcam', frame)

    """ to exit press q """
    if cv2.waitKey(1) & 0xff == ord('q') : 
        break 

cam.release()