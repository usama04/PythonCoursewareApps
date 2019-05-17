#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 10:04:00 2019

@author: usama
"""

import cv2

video = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
while True:
    check, frame = video.read()
    resized_frame = cv2.resize(frame,(int(frame.shape[1]*1.3),int(frame.shape[0]*1.3)))
    gray_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)
    faces=cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5)
    for x,y,w,h in faces:
        resized_frame = cv2.rectangle(resized_frame,(x,y),(x+w,y+h),(0,255,0),3)
    cv2.imshow('Capturing video', resized_frame)
    key = cv2.waitKey(1)
    if key==ord('q'):
        break

video.release()
cv2.destroyAllWindows()