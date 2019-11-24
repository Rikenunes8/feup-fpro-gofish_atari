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
layersunr = 5
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



def handle_events():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


while True:
    handle_events()

    pygame.gfxdraw.box(screen, [0, HEIGHT-HLAYpoints, WEIGHT, HLAYpoints], col['yellow']) 
    for i in range(1,5):
        pygame.gfxdraw.box(screen, [0, HEIGHT-HLAYpoints-HLAYsea*i, WEIGHT, HLAYsea], col['blue'+str(i)])  
    pygame.gfxdraw.box(screen, [0, HLAYsky, WEIGHT, HLAYwaves], col['blue5'])
    pygame.gfxdraw.box(screen, [0, 0, WEIGHT, HLAYsky], col['blue6'])
    pygame.gfxdraw.filled_circle(screen, int(COORsun[0]), int(COORsun[1]), int(RLAYsun), col['sun'])
    for i in range(4):    
        pygame.gfxdraw.filled_ellipse(screen, 0+(WEIGHT//4)*i, HLAYsky, int(RLAYelipse[0]), int(RLAYelipse[1]), col['blue5'])
        
        

    pygame.display.update()



    