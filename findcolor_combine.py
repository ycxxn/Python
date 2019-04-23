import numpy as np
import cv2

cap = cv2.VideoCapture(0)

def nothing(x):
    pass

def Contour(mask):
    contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(res_combine,contours,-1,(0,0,255),3)

cv2.namedWindow('image_1')
cv2.namedWindow('image_2')
#cv2.resizeWindow("image",640,480)
cv2.createTrackbar('lh','image_1',50,255,nothing)
cv2.createTrackbar('ls','image_1',60,255,nothing)
cv2.createTrackbar('lv','image_1',32,255,nothing)
cv2.createTrackbar('hh','image_1',100,255,nothing)
cv2.createTrackbar('hs','image_1',255,255,nothing)
cv2.createTrackbar('hv','image_1',255,255,nothing)

cv2.createTrackbar('lh','image_2',105,255,nothing)
cv2.createTrackbar('ls','image_2',60,255,nothing)
cv2.createTrackbar('lv','image_2',32,255,nothing)
cv2.createTrackbar('hh','image_2',120,255,nothing)
cv2.createTrackbar('hs','image_2',255,255,nothing)
cv2.createTrackbar('hv','image_2',255,255,nothing)

kernel = np.ones((8,8),np.uint8)

while(True):
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    blur = cv2.blur(hsv,(5,5))

    lh_1 = cv2.getTrackbarPos('lh','image_1')
    ls_1 = cv2.getTrackbarPos('ls','image_1')
    lv_1 = cv2.getTrackbarPos('lv','image_1')
    hh_1 = cv2.getTrackbarPos('hh','image_1')
    hs_1 = cv2.getTrackbarPos('hs','image_1')
    hv_1 = cv2.getTrackbarPos('hv','image_1')

    lh_2 = cv2.getTrackbarPos('lh','image_2')
    ls_2 = cv2.getTrackbarPos('ls','image_2')
    lv_2 = cv2.getTrackbarPos('lv','image_2')
    hh_2 = cv2.getTrackbarPos('hh','image_2')
    hs_2 = cv2.getTrackbarPos('hs','image_2')
    hv_2 = cv2.getTrackbarPos('hv','image_2')


    lower_1 = np.array([lh_1,ls_1,lv_1])
    upper_1 = np.array([hh_1,hs_1,hv_1])
    mask_1 = cv2.inRange(hsv, lower_1, upper_1)
    mask_1 = cv2.erode(mask_1,kernel,iterations = 1)
    mask_1 = cv2.dilate(mask_1,kernel,iterations = 1)
    res_1 = cv2.bitwise_and(frame,frame, mask= mask_1)

    lower_2 = np.array([lh_2,ls_2,lv_2])
    upper_2 = np.array([hh_2,hs_2,hv_2])
    mask_2 = cv2.inRange(hsv, lower_2, upper_2)
    mask_2 = cv2.erode(mask_2,kernel,iterations = 1)
    mask_2 = cv2.dilate(mask_2,kernel,iterations = 1)
    res_2 = cv2.bitwise_and(frame,frame, mask= mask_2)

    res_combine = res_1 + res_2

    #contours_1, hierarchy = cv2.findContours(mask_1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(res_combine,contours_1,-1,(0,0,255),3)

    #contours_2, hierarchy = cv2.findContours(mask_2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(res_combine,contours_2,-1,(0,0,255),3)

    Contour(mask_1)
    Contour(mask_2)
    
    areas_1 = [cv2.contourArea(c) for c in contours_1]
    a = len(areas_1)
    if a > 0 :
        max_index_1 = np.argmax(areas_1)
        cnt_1=contours_1[max_index_1]
        M_1=cv2.moments(cnt_1)
        cx_1=int(M_1['m10']/M_1['m00'])
        cy_1=int(M_1['m01']/M_1['m00'])
        cv2.circle(res_combine, (cx_1, cy_1), 10, (1, 227, 254), -1)

    areas_2 = [cv2.contourArea(c) for c in contours_2]
    b = len(areas_2)
    if b > 0 :
        max_index_2 = np.argmax(areas_2)
        cnt_2=contours_2[max_index_2]
        M_2=cv2.moments(cnt_2)
        cx_2=int(M_2['m10']/M_2['m00'])
        cy_2=int(M_2['m01']/M_2['m00'])
        cv2.circle(res_combine, (cx_2, cy_2), 10, (1, 227, 254), -1)
    

    #cv2.imshow('frame',frame)
    cv2.imshow('image_1',res_1)
    cv2.imshow('image_2',res_2)
    cv2.imshow("res",res_combine)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()