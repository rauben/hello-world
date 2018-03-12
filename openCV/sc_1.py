# !/usr/bin/python
import numpy as np
import cv2
import os
import re
import logging

def filterImage(path):
        img = cv2.imread(path, 1)
        #hsv
        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

        #create mask for lower spectrum
        lower = np.array([0,0,0])
        upper = np.array([75,255,255])
        mask0 = cv2.inRange(hsv,lower,upper)
        #create mask for upper spectrum
        lower = np.array([130,130,130])
        upper = np.array([180,255,255])
        mask1 = cv2.inRange(hsv,lower,upper)
        #reduce noise
        mask0bl = cv2.GaussianBlur(mask0,(3,3),0)
        mask1bl = cv2.GaussianBlur(mask1,(7,7),0)
        #create mask
        totalMaskBL = cv2.bitwise_or(mask0bl,mask1bl)

        return totalMaskBL



if name == '__main__':
    logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s - %(message)s')
    topdir = '.'

    reg0 = re.compile(r"(.*.JPG)|(.*.TIF)")
    reg1 = re.compile(r".*\(c.*")
    reg2 = re.compile(r".*copyResult.*")

    logging.debug('start of program')
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
                    logging.info(name + "finished2)
                except:
                    logging.error(dirpath + "/" + name)
                    print(dirpath +"/" + name)
                    pass
