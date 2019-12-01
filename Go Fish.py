# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 19:07:53 2019

@author: Rikenunes8
"""


import pygame
import pygame.gfxdraw
import random

pygame.init()
(atariw, atarih) = (192, 160)
(WIDTH, HEIGHT) = (800, 600)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Colors RGB
col = {'points': (132, 140, 76),
       'sun': (252, 252, 104),
       'blue1': (0, 0, 136),
       'blue2': (28, 32, 156),
       'blue3': (56, 64, 176),
       'blue4': (80, 92, 192),
       'bluewaves': (104, 116, 208),
       'bluesky': (144, 164, 236)}

# Pixels height in atari 2600
layerseah = 28
layerskyh = 15
layerwavesh = 20
layerpointsh = 13
layersunr = 4
layerelipser = (7, 4)
coorsun = (177, 5)
celip = 0 
seaweed = pygame.image.load('Seaweed.png') #58x58

# Sizes conversions
def resizeh(layerheigh):
    height = HEIGHT * layerheigh / atarih
    return round(height)
def resizew(layerwidth):
    width = WIDTH * layerwidth / atariw
    return round(width, 0)

HLAYsea = resizeh(layerseah)
HLAYsky = resizeh(layerskyh)
HLAYwaves = resizeh(layerwavesh)
HLAYpoints = resizeh(layerpointsh)
RLAYsun = resizeh(layersunr)
COORsun = (resizew(coorsun[0]), resizeh(coorsun[1]))
RLAYelipse = (resizew(layerelipser[0]), resizeh(layerelipser[1]))

# Constants and variables
x = WIDTH // 2
y = HEIGHT // 2
MAXSPEEDX = 0.09
MAXSPEEDY = 0.055
velx = 0
vely = 0
ACCELX = 0.0003
ACCELY = 0.0003
FRICTIONX = 0.001
FRICTIONY = 0.001

# Player
p1 = pygame.image.load('Player1.png')
P1_SIZE = (33.33, 11.25)
player1 = (p1, pygame.transform.flip(p1, True, False))
p2 = pygame.image.load('Player2.png')
P2_SIZE = (37.5, 15)
player2 = (p2, pygame.transform.flip(p2, True, False))
savedp = player1[0]
level = 0
energy = 0
p_list = (player1, player2)

# Enemies
e1 = pygame.image.load('Enemy1.png') # 255, 255, 255
E1_SIZE = (33.33, 11.25)
enemy1 = (e1, pygame.transform.flip(e1, True, False), (33.33, 11.25))

e2 = pygame.image.load('Enemy2.png') # 255, 255, 255
E2_SIZE = (37.5, 15)
enemy2 = (e2, pygame.transform.flip(e2, True, False), (37.5, 15))
e_list = ((enemy1, 0), (enemy2, 1))
cenemies = 0
cenemiesvar = 50
#enemiesposy = list(range(HLAYsea, HEIGHT-HLAYpoints-20, 25))*2
#enemiesposx = [0]*(len(enemiesposy)//2) + [WIDTH-30]*(len(enemiesposy)//2)
#enemiesori = [1]*(len(enemiesposy)//2) + [-1]*(len(enemiesposy)//2)
enemiesposy = list(range(HLAYsea-20, HEIGHT-HLAYpoints-HLAYsea+20, 52))
enemiesposx = [-30, WIDTH]
enemiesori = [1, -1]
enemiespresents = []


# Recognize events
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


def draw_background():
    # Draw background
    global celip
    pygame.gfxdraw.box(screen, [0, HEIGHT-HLAYpoints, WIDTH, HLAYpoints], col['points'])
    for i in range(1, 5):
        pygame.gfxdraw.box(screen, [0, HEIGHT-HLAYpoints-HLAYsea*i, WIDTH, HLAYsea], col['blue'+str(i)])
    pygame.gfxdraw.box(screen, [0, HLAYsky, WIDTH, HLAYwaves], col['bluewaves'])
    pygame.gfxdraw.box(screen, [0, 0, WIDTH, HLAYsky], col['bluesky'])
    pygame.gfxdraw.filled_circle(screen, int(COORsun[0]), int(COORsun[1]), int(RLAYsun), col['sun'])

    for i in range(4):
        pygame.gfxdraw.filled_ellipse(screen, 0+(WIDTH//4)*i+celip, HLAYsky, int(RLAYelipse[0]), int(RLAYelipse[1]), col['bluewaves'])
    celip += 1
    if celip >= WIDTH//4:
        celip = 0
    for i in range(3):
        screen.blit(seaweed, (WIDTH//6*(2*i+1)-29, HEIGHT-HLAYpoints-58))


clock = pygame.time.Clock()

# Main
while True:
    dt = clock.tick(30)
    # Check events
    handle_events()
    # Draw background
    draw_background()

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
            vely = MAXSPEEDY
        vely = max(0, vely - FRICTIONY)
    if vely < 0:
        if abs(vely)>MAXSPEEDY:
            vely = -MAXSPEEDY
        vely = min(0, vely + FRICTIONY)


    # Update coordinates
    if 0<= x+velx*dt <= WIDTH-25:
        x += velx*dt
    if HLAYsky<= y+vely*dt <= HEIGHT-HLAYpoints-8:
        y += vely*dt
    if keys[pygame.K_LEFT]:
        screen.blit(p_list[level][0], (x, y))
        savedp = p_list[level][0]
    elif keys[pygame.K_RIGHT]:
        screen.blit(p_list[level][1], (x, y))
        savedp = p_list[level][1]
    else:
        screen.blit(savedp, (x, y))
    # Generate enemy
    if cenemies == cenemiesvar:
        ee = random.choice(e_list)
        ex = random.choice(enemiesposx)
        ey = random.choice(enemiesposy)
        eo = [-1 if ex == WIDTH else 1][0]
        ev = random.randint(1, 3)
    #    enemiesposy.remove(ey)
        enemiespresents.append((ee,ex, ey, eo, ev))
        cenemiesvar = random.randint(20, 100)
        cenemies = 0
    # Count cycles
    cenemies += 1

    # Move enemies
    for c, (enemy_l, enemy_x, enemy_y, enemy_o, enemy_v) in enumerate(enemiespresents):
        if enemy_o == -1:
            screen.blit(enemy_l[0][0], (enemy_x, enemy_y))
            enemy_x -= enemy_v
            enemiespresents[c] = (enemy_l,enemy_x, enemy_y, enemy_o, enemy_v)
        else:
            screen.blit(enemy_l[0][1], (enemy_x, enemy_y))
            enemy_x += enemy_v
            enemiespresents[c] = (enemy_l, enemy_x, enemy_y, enemy_o, enemy_v)
        if (enemy_x <= x <= enemy_x + enemy_l[0][2][0] and enemy_y <= y <= enemy_y+enemy_l[0][2][1]) or (enemy_x <= x+P1_SIZE[0] <= enemy_x + enemy_l[0][2][0] and enemy_y <= y+P1_SIZE[1] <= enemy_y+enemy_l[0][2][1]) or (enemy_x <= x+P1_SIZE[0] <= enemy_x+enemy_l[0][2][0] and enemy_y <= y <= enemy_y+enemy_l[0][2][1]) or (enemy_x <= x <= enemy_x + enemy_l[0][2][0] and enemy_y <= y+P1_SIZE[1] <= enemy_y+enemy_l[0][2][1]):
            if enemy_l[1] > level:
                print('DEAD')
            else:
                enemiespresents.remove((enemy_l, enemy_x, enemy_y, enemy_o, enemy_v))
                energy += 1

    if energy == 5:
        level = 1


#    for enemy_x, enemy_y in zip(enemiesposx, enemiesposy):
#        screen.blit(enemy1, (enemy_x, enemy_y))
#        if (enemy_x <= x <= enemy_x + 25 and enemy_y <= y <= enemy_y+9) or (enemy_x <= x+25 <= enemy_x + 25 and enemy_y <= y+8 <= enemy_y+9) or (enemy_x <= x+25 <= enemy_x + 25 and enemy_y <= y <= enemy_y+9) or (enemy_x <= x <= enemy_x + 25 and enemy_y <= y+8 <= enemy_y+9):
#            print('colision')
#            print()


    pygame.display.flip()