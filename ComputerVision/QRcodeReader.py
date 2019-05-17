#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 12 14:22:17 2019

@author: usama
"""

import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

cap = cv2.VideoCapture(0)

while True:
    check, frame = cap.read()
    cv2.imshow("Frame", frame)
    
    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        print("Data: {}", obj.data)
    
    key = cv2.waitKey(1)
    
    if key==ord('q'):
        break
