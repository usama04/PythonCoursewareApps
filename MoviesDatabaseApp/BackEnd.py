#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 09:36:16 2019

@production: usama
"""

import sqlite3

def connect():
    conn=sqlite3.connect('Movies.db')
    curr=conn.cursor()
    curr.execute("CREATE TABLE IF NOT EXISTS movies (id INTEGER PRIMARY KEY, title TEXT, production TEXT, year INTEGER, imdb INTEGER)")
    conn.commit()
    conn.close()
    
connect()

def addEntry(title, production, year, imdb):
    conn=sqlite3.connect('Movies.db')
    curr=conn.cursor()
    curr.execute("INSERT INTO movies VALUES (NULL, ?, ?, ?, ?)", (title, production, year, imdb))
    conn.commit()
    conn.close()
    
def view():
    conn=sqlite3.connect('Movies.db')
    curr=conn.cursor()
    curr.execute("SELECT * FROM movies")
    rows = curr.fetchall()
    conn.close()
    return rows

def searchEntry(title="", production="", year="", imdb=""):
    conn = sqlite3.connect('Movies.db')
    curr = conn.cursor()
    curr.execute("SELECT * FROM movies WHERE title=? OR production=? OR year=? OR imdb=?", (title, production, year, imdb))
    rows = curr.fetchall()
    conn.close()
    return rows

def deleteEntry(id):
    conn = sqlite3.connect('Movies.db')
    curr = conn.cursor()
    curr.execute("DELETE FROM movies WHERE id=?", (id,))
    conn.commit()
    conn.close()

def updateEntry(id, title, production, year,imdb):
    conn = sqlite3.connect('Movies.db')
    curr = conn.cursor()
    curr.execute("UPDATE movies SET title=?, production=?, year=?, imdb=? WHERE id=?", (title, production, year, imdb, id,))
    conn.commit()
    conn.close()
