#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 09:19:42 2019

@author: usama
"""

import pygame
pygame.init()
win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Space-Shooter")
bg = pygame.image.load('background.jpg')
score = 0
clock = pygame.time.Clock()

class Player(object):
    space_ship = pygame.image.load('Ligher1.png')
    font = pygame.font.SysFont('comicsans', 20, True, False)
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.hitbox = (self.x + 10, self.y - 5, 40, 70)
        self.health = 10
    
    def hit(self):
        self.health -= 1
        print("Player got hit")
    
    def draw(self, win):
        self.hitbox = (self.x + 10, self.y - 5, 40, 70)
        text = font.render('Health: ' + str(self.health), 1, (255,255,255))
        win.blit(text, (390,30))
        win.blit(self.space_ship, (self.x,self.y))
        #pygame.draw.rect(win, (255,0,0),self.hitbox, 2)
        

class Enemy(object):
    enemy_img = pygame.image.load('bluedestroyer.png')
    
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.vel = 3
        self.hitbox = (self.x, self.y - 5, 70, 95)
        self.visible = True
        self.health = 9
        
    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * (-1)
        if self.vel < 0:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * (-1)
    def draw(self, win):
        if self.visible==True:
            self.hitbox = (self.x, self.y - 5, 70, 95)
            self.move()
            win.blit(self.enemy_img, (self.x, self.y))
            #pygame.draw.rect(win,(255,0,0), self.hitbox, 2)
            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1]-20,60,10))
            pygame.draw.rect(win, (0,255,0), (self.hitbox[0], self.hitbox[1]-20,60-(6*(9-self.health)),10))
    def hit(self):
        global score
        score += 1
        if self.health>0:
            self.health -= 1
        else:
            self.visible = False
        print("Enemy got hit")

class Projectile(object):
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel = 15
        
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

ship = Player(300,410,64,64)
ship_ammo = []
enemy_ammo = []
enemy = Enemy(100, 70, 64, 88, 400)
shootloop=0
shootloop2=0
font = pygame.font.SysFont('comicsans', 20, True, False)
def redraw():
    global win
    win.blit(bg,(0,0))
    ship.draw(win)
    enemy.draw(win)
    text = font.render('Score: ' + str(score), 1, (255,255,255))
    win.blit(text, (390,10))
    for ammo in ship_ammo:
        ammo.draw(win)
    for ammo in enemy_ammo:
        ammo.draw(win)
    pygame.display.update()

run = True
while run:
    clock.tick(40)
    
    if shootloop>0:
        shootloop+=1
    if shootloop>15:
        shootloop=0
    
    if shootloop2>0:
        shootloop2+=1
    if shootloop2>40:
        shootloop2=0
    if enemy.visible == True:
        for ammo in enemy_ammo:
            if ammo.y - ammo.radius < ship.hitbox[1]+ship.hitbox[3] and ammo.y + ammo.radius>ship.hitbox[1]:
                if ammo.x+ammo.radius>ship.hitbox[0] and ammo.x-ammo.radius<ship.hitbox[0]+ship.hitbox[2]:
                    ship.hit()
                    enemy_ammo.pop(enemy_ammo.index(ammo))
            if ammo.y < 500 and ammo.y > 0:
                ammo.y += ammo.vel
            else:
                enemy_ammo.pop(enemy_ammo.index(ammo))
        if len(enemy_ammo)<1:
            enemy_ammo.append(Projectile(round(enemy.x + enemy.width//2),
                                         round(enemy.y + enemy.height//2),
                                         6,(255,0,0)))
            shootloop2=1
    else:
        enemy_ammo=[]
    for ammo in ship_ammo:
        if ammo.y - ammo.radius < enemy.hitbox[1]+enemy.hitbox[3] and ammo.y + ammo.radius>enemy.hitbox[1]:
            if ammo.x+ammo.radius>enemy.hitbox[0] and ammo.x-ammo.radius<enemy.hitbox[0]+enemy.hitbox[2]:
                enemy.hit()
                ship_ammo.pop(ship_ammo.index(ammo))
        if ammo.y < 500 and ammo.y > 0:
            ammo.y -= ammo.vel
        else:
            ship_ammo.pop(ship_ammo.index(ammo))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and ship.x > ship.vel:
        ship.x -= ship.vel
    if keys[pygame.K_RIGHT] and ship.x < 500-ship.width-ship.vel:
        ship.x += ship.vel
        
    if keys[pygame.K_SPACE] and shootloop==0:
        if len(ship_ammo) < 5:
            ship_ammo.append(Projectile(round(ship.x + ship.width//2),
                                        round(ship.y + ship.height//2),
                                        6,(255,255,0)))
            shootloop=1
    redraw()

pygame.quit()
