import numpy as np
import cv2

cap = cv2.VideoCapture(0)

def nothing(x):
    pass

cv2.namedWindow('image')
#cv2.resizeWindow("image",640,480)
cv2.createTrackbar('lh','image',0,255,nothing)
cv2.createTrackbar('ls','image',60,255,nothing)
cv2.createTrackbar('lv','image',32,255,nothing)
cv2.createTrackbar('hh','image',180,255,nothing)
cv2.createTrackbar('hs','image',255,255,nothing)
cv2.createTrackbar('hv','image',255,255,nothing)

kernel = np.ones((8,8),np.uint8)

while(True):
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    blur = cv2.blur(hsv,(5,5))

    lh = cv2.getTrackbarPos('lh','image')
    ls = cv2.getTrackbarPos('ls','image')
    lv = cv2.getTrackbarPos('lv','image')
    hh = cv2.getTrackbarPos('hh','image')
    hs = cv2.getTrackbarPos('hs','image')
    hv = cv2.getTrackbarPos('hv','image')

    lower = np.array([lh,ls,lv])
    upper = np.array([hh,hs,hv])
    mask = cv2.inRange(hsv, lower, upper)
    mask=cv2.erode(mask,kernel,iterations = 1)
    mask=cv2.dilate(mask,kernel,iterations = 1)

    contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame,contours,-1,(0,0,255),3)
    
    areas = [cv2.contourArea(c) for c in contours]
    max_index = np.argmax(areas)
    cnt=contours[max_index]
    
    M=cv2.moments(cnt)
    cx=int(M['m10']/M['m00'])
    cy=int(M['m01']/M['m00'])
    cv2.circle(frame, (cx, cy), 10, (1, 227, 254), -1)
    print(cx,cy)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()