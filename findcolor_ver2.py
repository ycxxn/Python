import numpy as np
import cv2

cap = cv2.VideoCapture(0)

def nothing(x):
    pass

cv2.namedWindow('image')
cv2.resizeWindow("image",640,480)
cv2.createTrackbar('lh','image',0,255,nothing)
cv2.createTrackbar('ls','image',60,255,nothing)
cv2.createTrackbar('lv','image',32,255,nothing)
cv2.createTrackbar('hh','image',180,255,nothing)
cv2.createTrackbar('hs','image',255,255,nothing)
cv2.createTrackbar('hv','image',255,255,nothing)

kernel = np.ones((5,5),np.uint8)

while(True):
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    hsv=cv2.erode(hsv,kernel,iterations = 1)
    hsv=cv2.dilate(hsv,kernel,iterations = 1)
    #blur = cv2.blur(hsv,(5,5))
    ret,frame=cv2.threshold(imgray,127,255,0)

    lh = cv2.getTrackbarPos('lh','image')
    ls = cv2.getTrackbarPos('ls','image')
    lv = cv2.getTrackbarPos('lv','image')
    hh = cv2.getTrackbarPos('hh','image')
    hs = cv2.getTrackbarPos('hs','image')
    hv = cv2.getTrackbarPos('hv','image')

    lower = np.array([lh,ls,lv])
    upper = np.array([hh,hs,hv])
    mask = cv2.inRange(cnt1, lower, upper)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()