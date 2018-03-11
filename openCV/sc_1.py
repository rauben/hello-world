# !/usr/bin/python
import numpy as np
import cv2
import os
import re

def filterImage(path):
    try:
        img = cv2.imread(path, 1)
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
        hsvR1 = cv2.GaussianBlur(hsvR1,(9,9),0)


        hsvRF = cv2.bitwise_or(hsvR0,hsvR1)

        totalMask = cv2.bitwise_or(mask0,mask1)

        #blur
        blur = cv2.GaussianBlur(hsvRF,(5,5),0)


        blackblur = cv2.GaussianBlur(totalMask,(3,3),0)

        mask0bl = cv2.GaussianBlur(mask0,(3,3),0)
        mask1bl = cv2.GaussianBlur(mask1,(7,7),0)

        totalMaskBL = cv2.bitwise_or(mask0bl,mask1bl)

        return totalMaskBL

        cv2.imshow('img',img)
        #cv2.imshow('Filter1',hsvR0)
        #cv2.imshow('Filter2',hsvR1)
        cv2.imshow('Result',hsvRF)
        cv2.imshow('gBlur',blur)
        cv2.imshow('bblur',blackblur)
        cv2.imshow('blblure', totalMaskBL)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except:
        print(text)


topdir = '.'
resultPath = ''
reg0 = re.compile(r"(.*.JPG)|(.*.TIF)")
reg1 = re.compile(r".*\(c.*")
reg2 = re.compile(r".*copyResult.*")
for dirpath, dirnames, files in os.walk(topdir):
    for name in files:
        results = str()
        text = os.path.join(dirpath,name)
        if reg0.match(name) and not reg1.match(name) and not reg2.match(dirpath):
            try:
                image = filterImage(text)
                text = text.split('/')[1:]
                newPath = "./copyResult/"
                for i in text:
                    newPath = os.path.join(newPath,i)
                directory = os.path.dirname(newPath)
                if not os.path.exists(directory):
                    os.makedirs(directory)
                cv2.imwrite(newPath,image)
            except:
                pass
