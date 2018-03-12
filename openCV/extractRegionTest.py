import numpy as np
import cv2

img = cv2.imread('C:/Users/benedikt.rauscher/Desktop/example.png', 1)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#filter after color
lower =np.array([0,0,0])
upper = np.array([75,255,255])
mask0 = cv2.inRange(hsv,lower,upper)
hsvR0 = cv2.bitwise_and(hsv,hsv,mask=mask0)
lower = np.array([130,130,130])
upper = np.array([180,255,255])
mask1 = cv2.inRange(hsv,lower,upper)
hsvR1 = cv2.bitwise_and(hsv,hsv,mask=mask1)
hsvRF = cv2.bitwise_or(hsvR0,hsvR1)
#totalMask = cv2.bitwise_or(mask0,mask1)
totalMask = cv2.bitwise_not(cv2.bitwise_or(mask0,mask1))


# find contours in the edged image, keep only the largest
# ones, and initialize our screen contour
im2, contours, hierarchy = cv2.findContours(totalMask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[-1]

#cv2.drawContours(hsv, [cnt], 0, (0,255,0), 3)
cv2.fillPoly(totalMask,[cnt],color=(255,255,255))
newImg = cv2.bitwise_and(img,img,mask=totalMask)

cv2.imshow('hsv',hsv)
cv2.imshow('hsvr0',hsvRF)
cv2.imshow('mask',totalMask)
cv2.imshow('newImg',newImg)


cv2.waitKey(0)
cv2.destroyAllWindows()