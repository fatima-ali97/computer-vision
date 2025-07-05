import cv2 

width = 640
height = 360

cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)

cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)

cam.set(cv2.CAP_PROP_FPS,30)

cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))



# set up vars 
current_x_point = 0  # originally 200
current_y_point = 0  # originally 130
space_interval = 1 
SnipWidth = 160
SnipHeight = 160
SnipCR = []


while True:
    ignore,frame = cam.read() 

    # first slice dimension (130:290) is in respect to the columns!!

    ## specify ROI range
    frameROI = frame[current_y_point:int(current_y_point+SnipWidth), current_x_point:current_x_point+SnipHeight]   # 160 w && 160 h 
    
    
    ## convert the ROI to gray
    frameROIGray = cv2.cvtColor(frameROI, cv2.COLOR_BGR2GRAY)
    frameROIGray2BGR =  cv2.cvtColor(frameROIGray, cv2.COLOR_GRAY2BGR)

    ## place the ROI in the original frame's position
    frame[current_y_point:int(current_y_point+SnipWidth), current_x_point:current_x_point+SnipHeight] = frameROIGray2BGR  # 160 w && 160 h 

    """ Show a frame """
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',600,0)


    #cv2.imshow('my ROI', frameROIGray)
    #cv2.moveWindow('my ROI',0,0)

    #frame[current_y_point:int(current_y_point+160), current_x_point:current_x_point+160]

    
    if  current_x_point >= 160 :
        #frame[current_y_point:int(current_y_point+160), current_x_point:current_x_point+160] = frameROIGray2BGR
        current_y_point += space_interval 
        current_x_point -= space_interval 
       # print(current_y_point)
        print(current_x_point)
    else :
        #frame[current_y_point:int(current_y_point+160), current_x_point:current_x_point+160] = frameROIGray2BGR
        current_y_point += space_interval
        current_x_point += space_interval

    # current_y_point += space_interval
    #current_x_point += space_interval 
    
    #frame[int(current_y_point):(current_y_point+ 160),current_x_point:(current_x_point+ 160)] = frameROIGray2BGR
    #""" Show a frame """
    #cv2.imshow('my WEBcam', frame)
    #cv2.moveWindow('my WEBcam',600,0)

    """ to exit press q """
    if cv2.waitKey(1) & 0xff == ord('q') : 
        break 

cam.release()