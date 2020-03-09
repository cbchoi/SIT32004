import numpy as np
import cv2

drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1

# mouse callback function
def draw_rect(event,x,y,flags,param):
    global ix,iy,drawing,mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(param[0],(ix,iy),(x,y),(0,255,0),-1)
                #param[1].write(param[0])
                cv2.imshow('frame2',frame)
            else:
                cv2.circle(param[0],(x,y),5,(0,0,255),-1)
                #param[1].write(param[0])

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(param[0],(ix,iy),(x,y),(0,255,0),-1)
            #param[1].write(param[0])
            cv2.imshow('frame2',frame)
        else:
            cv2.circle(param[0],(x,y),5,(0,0,255),-1)
            #param[1].write(param[0])

cv2.namedWindow('frame')
cv2.namedWindow('frame2')
cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)
        #cv2.circle(frame,(10,10),100,(255,0,0),-1)
        #cv2.imshow('frame',frame)
        cv2.setMouseCallback('frame', draw_rect, (frame, out))
        cv2.imshow('frame',frame)
        # write the flipped frame
        out.write(frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()