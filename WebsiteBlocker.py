#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 15:47:50 2019

@author: usama
"""
import time
from datetime import datetime as dt

hosts_path = r"/etc/hosts"
hosts_path_inuse = "hosts"
redirect = "127.0.0.1"
websites = ["www.bing.com","www.qq.com", "bing.com", "www.bing.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 17) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17, 50):
        print("Test Woring Hours...")
        with open(hosts_path_inuse, 'r+') as file:
            content = file.read()
            for website in websites:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        print("Not working Hours")
        with open(hosts_path_inuse, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites):
                    file.write(line)
            file.truncate()
            
        
    time.sleep(5)