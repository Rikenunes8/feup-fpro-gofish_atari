# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 19:07:53 2019

@author: Rikenunes8
"""


import pygame
import pygame.gfxdraw

pygame.init()
(atariw, atarih) = (192, 160)
(WEIGHT, HEIGHT) = (800, 600)
screen = pygame.display.set_mode((WEIGHT, HEIGHT))
fish1 = pygame.image.load('Fish1.png')

# Colors RGB
col = {'yellow': (132, 140, 76),
       'sun': (252, 252, 104),
       'blue1': (0, 0, 136),
       'blue2': (28, 32, 156),
       'blue3': (56, 64, 176),
       'blue4': (80, 92, 192),
       'blue5': (104, 116, 208),
       'blue6': (144, 164, 236)}

# pixels height in atari 2600
layerseah = 28
layerskyh = 15
layerwavesh = 20
layerpointsh = 13
layersunr = 4
layerelipser = (7, 4)
coorsun = (177, 5)


def resizeh(layerheigh):
    height = HEIGHT * layerheigh / atarih
    return round(height)


def resizew(layerweight):
    weight = WEIGHT * layerweight / atariw
    return round(weight, 0)


HLAYsea = resizeh(layerseah)
HLAYsky = resizeh(layerskyh)
HLAYwaves = resizeh(layerwavesh)
HLAYpoints = resizeh(layerpointsh)
RLAYsun = resizeh(layersunr)
COORsun = (resizew(coorsun[0]), resizeh(coorsun[1]))
RLAYelipse = (resizew(layerelipser[0]), resizeh(layerelipser[1]))

x = WEIGHT // 2
y = HEIGHT // 2
MAXSPEEDX = 0.15
MAXSPEEDY = 0.1
velx = 0
vely = 0
ACCELX = 0.0003
ACCELY = 0.0003
FRICTIONX = 0.004
FRICTIONY = 0.004


def handle_events():
    global x, y, vely, velx, keys
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        vely -= ACCELY * dt
    if keys[pygame.K_DOWN]:
        vely += ACCELY * dt
    if keys[pygame.K_LEFT]:
        velx -= ACCELX * dt
    if keys[pygame.K_RIGHT]:
        velx += ACCELX * dt


clock = pygame.time.Clock()

while True:
    dt = clock.tick(30)
    # Check events
    handle_events()
    
    # Draw background
    pygame.gfxdraw.box(screen, [0, HEIGHT-HLAYpoints, WEIGHT, HLAYpoints], col['yellow'])
    for i in range(1, 5):
        pygame.gfxdraw.box(screen, [0, HEIGHT-HLAYpoints-HLAYsea*i, WEIGHT, HLAYsea], col['blue'+str(i)])
    pygame.gfxdraw.box(screen, [0, HLAYsky, WEIGHT, HLAYwaves], col['blue5'])
    pygame.gfxdraw.box(screen, [0, 0, WEIGHT, HLAYsky], col['blue6'])
    pygame.gfxdraw.filled_circle(screen, int(COORsun[0]), int(COORsun[1]), int(RLAYsun), col['sun'])
    for i in range(4):
        pygame.gfxdraw.filled_ellipse(screen, 0+(WEIGHT//4)*i, HLAYsky, int(RLAYelipse[0]), int(RLAYelipse[1]), col['blue5'])
    
    # Limit velocity and create friction    
    if velx > 0:
        if abs(velx)>MAXSPEEDX:
            velx = MAXSPEEDX
        velx = max(0, velx - FRICTIONX)
    if velx < 0:
        if abs(velx)>MAXSPEEDX:
            velx = -MAXSPEEDX
        velx = min(0, velx + FRICTIONX)
    
    if vely > 0:
        if abs(vely)>MAXSPEEDY:
            vely = +MAXSPEEDY
        vely = max(0, vely - FRICTIONY)
    if vely < 0:
        if abs(vely)>MAXSPEEDY:
            vely = -MAXSPEEDY
        vely = min(0, vely + FRICTIONY)
        
    # Update coordinates
    x += velx*dt
    y += vely*dt 
        
    screen.blit(fish1, (x, y))
    pygame.display.flip()