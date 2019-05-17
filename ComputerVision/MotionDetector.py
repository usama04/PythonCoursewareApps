#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 15:40:36 2019

@author: usama
"""

import cv2
from datetime import datetime as dt
import pandas as pd
video = cv2.VideoCapture(0)

first_frame = None

status_list = [None, None]
status_change_times = []
df = pd.DataFrame(columns=["Start","End"])

while True:
    check, frame = video.read()
    status = 0
    resized_frame = cv2.resize(frame,(int(frame.shape[1]*1.4),int(frame.shape[0]*1.4)))
    gray_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.GaussianBlur(gray_frame,(21,21),0)
    if first_frame is None:
        first_frame = gray_frame
        continue
    deltaFrame = cv2.absdiff(first_frame, gray_frame)
    thresh_delta = cv2.threshold(deltaFrame, 30, 255, cv2.THRESH_BINARY)[1]
    
    thresh_delta = cv2.dilate(thresh_delta,None,iterations=2)
    
    cnts, heirarchy = cv2.findContours(thresh_delta.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in cnts:
       if cv2.contourArea(contour)<10000:
           continue
       status=1
       (x,y,w,h) = cv2.boundingRect(contour)
       cv2.rectangle(resized_frame, (x,y), (x+w,y+h), (0,255,0),3)
    
    #print(gray_frame)
    #cv2.imshow('Thresh Delta', thresh_delta)
    #cv2.imshow('Delta Frame', deltaFrame)
    cv2.imshow('Capturing video', resized_frame)
    key = cv2.waitKey(1)
    if key==ord('q'):
        if status==1:
            status_change_times.append(dt.now())
        break

    status_list.append(status)
    
    if status_list[-1] == 1  and status_list[-2] == 0:
        status_change_times.append(dt.now())
    if status_list[-1] == 0  and status_list[-2] == 1:
        status_change_times.append(dt.now())
    
for i in range(0,len(status_change_times),2):
    df=df.append({"Start":status_change_times[i], "End":status_change_times[i+1]}, ignore_index=True)
    
df.to_csv("TimesMotionDetected.csv")
video.release()
cv2.destroyAllWindows()