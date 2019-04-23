import cv2
import numpy as np

img=cv2.imread("images.jpg")
img=cv2.resize(img,(480,400))
cv2.imshow("image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()

def FindM(mask):
    contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(res_combine,contours_1,-1,(0,0,255),3)
    
    areas = [cv2.contourArea(c) for c in contours]
    a = len(areas)
    if a > 0 :
        max_index = np.argmax(areas)
        cnt = contours[max_index]
        M = cv2.moments(cnt)
        cx=int(M['m10']/M['m00'])
        cy=int(M['m01']/M['m00'])
        cv2.circle(res_combine, (cx, cy), 10, (1, 227, 254), -1)

