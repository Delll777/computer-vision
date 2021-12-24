# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 11:26:38 2021

@author: Аделина
"""

import cv2
import numpy as np
import time


cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cv2.namedWindow("Camera")

lower_green = (57, 130, 120)
upper_green = (73, 255, 255)

lower_yellow = (20, 110, 130)
upper_yellow = (35, 255, 255)

lower_blue = (90, 150, 120)
upper_blue = (100, 255, 255)

mask_lower = [lower_green, lower_yellow, lower_blue]
mask_upper = [upper_green, upper_yellow, upper_blue]

center = []

while cam.isOpened():
    _, image = cam.read()
    image = cv2.flip(image, 1)
    
    curr_time = time.time()
    blurred = cv2.GaussianBlur(image, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    
    #mask1 = cv2.inRange(hsv, lower_yellow, upper_yellow)
    #mask2 = cv2.inRange(hsv, lower_green, upper_green)
    #mask4 = cv2.bitwise_or(mask1, mask2)
    #mask = cv2.bitwise_or(mask4, mask3)
    
    for i in range(len(mask_upper)):
        mask = cv2.inRange(hsv, mask_lower[i], mask_upper[i])
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
    
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)[-2]
    
    
        if len(cnts) > 0:
            c = max(cnts, key=cv2.contourArea)
            (curr_x, curr_y), radius = cv2.minEnclosingCircle(c)
            center.append((curr_x, curr_y))
            
            if radius > 10:
                cv2.circle(image, (int(curr_x), int(curr_y)), int(radius),
                           (0, 255, 255), 2)
                cv2.circle(image, (int(curr_x), int(curr_y)), 5,
                           (0, 255, 255), 2)
                
 
        
   
    
    cv2.imshow("Camera", image)
    #cv2.imshow("Mask", mask)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
    

    
cam.release()
cv2.destroyAllWindows()