import numpy as np
import cv2

img = cv2.imread('../40/8.JPG', 1)
#img = cv2.imread('383.TIF',1)
#img = cv2.imread('367.TIF',1)
#hsv
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

#filter after color
lower =np.array([0,0,0])
upper = np.array([75,255,255])
mask0 = cv2.inRange(hsv,lower,upper)
hsvR0 = cv2.bitwise_and(hsv,hsv,mask=mask0)
lower = np.array([130,130,130])
upper = np.array([180,255,255])
mask1 = cv2.inRange(hsv,lower,upper)
hsvR1 = cv2.bitwise_and(hsv,hsv,mask=mask1)

hsvR0 = cv2.GaussianBlur(hsvR0,(3,3),0)
hsvR1 = cv2.GaussianBlur(hsvR1,(7,7),0)


hsvRF = cv2.bitwise_or(hsvR0,hsvR1)

totalMask = cv2.bitwise_or(mask0,mask1)

#blur
blur = cv2.GaussianBlur(hsvRF,(5,5),0)


blackblur = cv2.GaussianBlur(totalMask,(3,3),0)

mask0bl = cv2.GaussianBlur(mask0,(3,3),0)
mask1bl = cv2.GaussianBlur(mask1,(7,7),0)

totalMaskBL = cv2.bitwise_or(mask0bl,mask1bl)

cv2.imshow('img',img)
#cv2.imshow('Filter1',hsvR0)
#cv2.imshow('Filter2',hsvR1)
cv2.imshow('Result',hsvRF)
cv2.imshow('gBlur',blur)
cv2.imshow('bblur',blackblur)
cv2.imshow('blblure', totalMaskBL)
cv2.waitKey(0)
cv2.destroyAllWindows()