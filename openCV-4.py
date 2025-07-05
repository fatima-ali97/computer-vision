import cv2 


rows = int(input("what is the # of rows? "))
columns = int(input("what is the # of columns? "))

width =   1280     
height =  720


cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)

cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)

cam.set(cv2.CAP_PROP_FPS,30)

cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    ignore,frame = cam.read() 

    """Scale the frame"""
    frame= cv2.resize(frame, (int(width/columns),int(height/columns)))

    for i in range(0,rows) :
        for j in range(0,columns):
            windowName = f'{i} X {j} window'

            cv2.imshow(windowName,frame)
            cv2.moveWindow(windowName, int(width/columns) * j, int(height/columns +30)*i)

    """ to exit press q """
    if cv2.waitKey(1) & 0xff == ord('q') : 
        break 

cam.release()