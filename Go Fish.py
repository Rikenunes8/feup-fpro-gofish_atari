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
       'bluesky': (144, 164, 236),
       'white': (255, 255, 255),
       'black': (0,0,0),
       'mblue': (56, 64, 176)}

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
y = HEIGHT-HLAYpoints-40
MAXSPEEDX = 0.2#0.09
MAXSPEEDY = 0.1#0.055
velx = 0
vely = 0
ACCELX = 0.0004
ACCELY = 0.0004
FRICTIONX = 0.003
FRICTIONY = 0.002

# Player ()
DEAD = False
skull = pygame.image.load('Skull.png')
skullt = 0

# 186, 186, 62
p1 = pygame.image.load('Player1.png')
player1 = (p1, pygame.transform.flip(p1, True, False), (33.33, 11.25))

p2 = pygame.image.load('Player2.png')
player2 = (p2, pygame.transform.flip(p2, True, False),(37.5, 15))

p3 = pygame.image.load('Player3.png')
player3 = (p3, pygame.transform.flip(p3, True, False),(41.667, 18.75))

p4 = pygame.image.load('Player4.png')
player4 = (p4, pygame.transform.flip(p4, True, False),(45.833, 22.5))

p5 = pygame.image.load('Player5.png')
player5 = (p5, pygame.transform.flip(p5, True, False),(54.167, 22.5))

p6 = pygame.image.load('Player6.png')
player6 = (p6, pygame.transform.flip(p6, True, False),(79.167, 26.25))

p7 = pygame.image.load('Player7.png')
player7 = (p7, pygame.transform.flip(p7, True, False),(87.5, 26.25))

p8 = pygame.image.load('Player8.png')
player8 = (p8, pygame.transform.flip(p8, True, False),(100, 30))

p9 = pygame.image.load('Player9.png')
player9 = (p9, pygame.transform.flip(p9, True, False),(125, 30))


savedo = 0
savedp = player1
level = 0
energy = 0
best_score = 0
p_list = (player1, player2, player3, player4, player5, player6, player7, player8, player9)

# Enemies
e1 = pygame.image.load('Enemy1.png')  # 255, 255, 255
# E1_SIZE = (33.33, 11.25) = (8,3)
enemy1 = (e1, pygame.transform.flip(e1, True, False), (33.33, 11.25))

e2 = pygame.image.load('Enemy2.png')  # 80, 156, 128
# E2_SIZE = (37.5, 15) = (9, 4)
enemy2 = (e2, pygame.transform.flip(e2, True, False), (37.5, 15))

e3 = pygame.image.load('Enemy3.png')  # 229, 231, 95
# E3_SIZE = (41.667, 18.75) = (10,5)
enemy3 = (e3, pygame.transform.flip(e3, True, False), (41.667, 18.75))

e4 = pygame.image.load('Enemy4.png')  # 184, 45, 41
# E4_SIZE = (45.833, 22.5) = (11,6)
enemy4 = (e4, pygame.transform.flip(e4, True, False), (45.833, 22.5))

e5 = pygame.image.load('Enemy5.png')  # 156, 168, 100
# E5_SIZE = (54.167, 22.5) = (13,6)
enemy5 = (e5, pygame.transform.flip(e5, True, False), (54.167, 22.5))

e6 = pygame.image.load('Enemy6.png')  # 108, 108, 107     Cinzento
# E6_SIZE = (79.167, 26.25) = (19,7)
enemy6 = (e6, pygame.transform.flip(e6, True, False), (79.167, 26.25))

e7 = pygame.image.load('Enemy7.png')  # 145, 230, 192     Azul claro
# E7_SIZE = (87.5, 26.25) = (21,7)
enemy7 = (e7, pygame.transform.flip(e7, True, False), (87.5, 26.25))

e8 = pygame.image.load('Enemy8.png') # 132, 132, 36      Castanho
# E8_SIZE = (100, 30) = (24,8)
enemy8 = (e8, pygame.transform.flip(e8, True, False), (100, 30))

e9 = pygame.image.load('Enemy9.png') # 219, 158, 110     Laranja
# E9_SIZE = (125, 30) = (30,8)
enemy9 = (e9, pygame.transform.flip(e9, True, False), (125, 30))

e10 = pygame.image.load('Enemy10.png') # 104, 112, 52     Castanho escuro 1
# E10_SIZE = (154.167, 33.75) = (37,9)
enemy10 = (e10, pygame.transform.flip(e10, True, False), (154.167, 33.75))

e11 = pygame.image.load('Enemy11.png') # 104, 156, 192     Azul 2
# E11_SIZE = (179.167, 33.75) = (43,9)
enemy11 = (e11, pygame.transform.flip(e11, True, False), (179.167, 33.75))

e12 = pygame.image.load('Enemy12.png')  # 176, 60, 60     Vermelho 1
# E12_SIZE = (204.167, 37.5) = (49,10)
enemy12 = (e12, pygame.transform.flip(e12, True, False), (204.167, 37.5))

e13 = pygame.image.load('Enemy13.png') # 208, 128, 92     Laranja 3
# E13_SIZE = (204.167, 37.5) = (49,10)
enemy13 = (e13, pygame.transform.flip(e13, True, False), (204.167, 37.5))

e98 = pygame.image.load('Enemy98.png') # 3, 3, 7     Tubarao
# E98_SIZE = (104.167, 33.75) = (25,9)
enemy98 = (e98, pygame.transform.flip(e98, True, False), (104.167, 33.75))

e99 = pygame.image.load('Enemy99.png') # 56, 84, 167
e99col = pygame.image.load('Enemy99col.png') # 164, 200, 252
# E99_SIZE = (100, 7.5) = (24,2)
enemy99 = (e99, pygame.transform.flip(e99, True, False), (100, 7.5), e99col, pygame.transform.flip(e99col, True, False))

e100 = pygame.image.load('Enemy100.png')
# E100_SIZE = (54.167, 41.250) = (13,11)
enemy100 = (e100, pygame.transform.flip(e100, True, False), (54.167, 41.250))

e_list = ((enemy1, 0), (enemy2, 1), (enemy3, 2), (enemy4, 3), (enemy5, 4), (enemy6, 5), (enemy7, 6), (enemy8, 7), (enemy9, 8), (enemy10, 9), (enemy11, 10), (enemy12, 11), (enemy13, 12), (enemy98, 98), (enemy99,99), (enemy100, 100))

weight = [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
cenemies = 0
cenemiesvar = 50
enemiesposy = list(range(HLAYsea-20, HEIGHT-HLAYpoints-HLAYsea+20, 52))
dposy = {x:i for i, x in enumerate(enemiesposy)}
yweights = [1,1,1,1,1,1,1,1]
enemiesposx = [-204, WIDTH]
enemiesori = [1, -1]
enemiespresents = []
e99c = 0
energydict = {0:1,1:2,2:4,3:7,4:10,5:15,6:20,7:25,8:30}

# Fonts
largeFont = pygame.font.SysFont('arial', 50)
menuFont = pygame.font.SysFont('arial', 120)
startFont = pygame.font.SysFont('arial', 28)


# Recognize gamepalay events
def handle_events():
    global x, y, vely, velx, keys
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    if keys[pygame.K_UP]:
        vely -= ACCELY * dt
    if keys[pygame.K_DOWN]:
        vely += ACCELY * dt
    if keys[pygame.K_LEFT]:
        velx -= ACCELX * dt
    if keys[pygame.K_RIGHT]:
        velx += ACCELX * dt


# Recognize menu events
def menu_events():
    global menuf, enemiespresents, vely, yweights
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    if keys[pygame.K_SPACE]:
        enemiespresents = []
        vely = -0.5
        menuf = False
        yweights = [1,1,1,1,1,1,1,1]


# Menu
def menu():
    s = pygame.Surface((WIDTH, HEIGHT))
    s.set_alpha(128)
    s.fill(col['black'])
    screen.blit(s, (0,0))
    pygame.draw.rect(screen, col['mblue'],(WIDTH//6, 7*HEIGHT//16, 2*WIDTH//3, HEIGHT//5))
    title = menuFont.render('Go Fish', 1, col['white'])
    title2 = menuFont.render('Go Fish', 1, col['blue4'])
    start = startFont.render('Press SPACE to start',1, col['white'])
    screen.blit(pygame.transform.flip(title2, False, True), (WIDTH//4-10, HEIGHT//4+88))
    screen.blit(title, (WIDTH//4-10, HEIGHT//4))
    screen.blit(start, (11*WIDTH//32, 5*HEIGHT//6))
    menu_events()

# Draw background
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

# Draw score
def draw_score(e, w, h):
    text = largeFont.render(str(e).zfill(4), 1, col['white'])
    screen.blit(text, (w, h))

# Colisions
def overlaps(x1, y1, w1, h1, x2, y2, w2, h2):
    return not (x1+w1 < x2 or x1 > x2+w2 or y1+h1 < y2 or y1 > y2+h2)


clock = pygame.time.Clock()
menuf = True

keys = pygame.key.get_pressed()
spawn_time = 0

# Main
while True:
    dt = clock.tick(30)

    # Check events
    if not menuf:
        handle_events()

    # Draw background
    draw_background()

    # Limit velocity and create friction
    if velx > 0:
        if abs(velx) > MAXSPEEDX:
            velx = MAXSPEEDX
        velx = max(0, velx - FRICTIONX)
    if velx < 0:
        if abs(velx) > MAXSPEEDX:
            velx = -MAXSPEEDX
        velx = min(0, velx + FRICTIONX)
    if vely > 0:
        if abs(vely) > MAXSPEEDY:
            vely = MAXSPEEDY
        vely = max(0, vely - FRICTIONY)
    if vely < 0:
        if abs(vely) > MAXSPEEDY:
            vely = -MAXSPEEDY
        vely = min(0, vely + FRICTIONY)

    # Update coordinates
    if not menuf:
        if not DEAD:
            if 0 <= x+velx*dt <= WIDTH-p_list[level][2][0]:
                x += velx*dt
            elif x+velx*dt > WIDTH-p_list[level][2][0]:
                x = WIDTH-p_list[level][2][0]
            else:
                x = 0
            if HLAYsky <= y+vely*dt <= HEIGHT-HLAYpoints-p_list[level][2][1]:
                y += vely*dt
            if keys[pygame.K_LEFT]:
                screen.blit(p_list[level][0], (x, y))
                savedo = 0
            elif keys[pygame.K_RIGHT]:
                screen.blit(p_list[level][1], (x, y))
                savedo = 1
            else:
                savedp = p_list[level][savedo]
                screen.blit(savedp, (x, y))

    # Generate enemy
    if yweights != [0,0,0,0,0,0,0,0]:
       # if cenemies == cenemiesvar:
        if pygame.time.get_ticks() >= spawn_time:
            ee = random.choices(e_list, weight)
            ex = random.choice(enemiesposx)
            ey = random.choices(enemiesposy, yweights)
            yweights[dposy[ey[0]]] = 0
            eo = [-1 if ex == WIDTH else 1][0]
            if ee[0][1] == 98:
                ev = random.randint(6,15)/100  #2,4
            else:
                ev = random.randint(10, 25)/100  #3,7
            enemiespresents.append((ee[0], ex, ey[0], eo, ev))
            cenemiesvar = random.randint(300, 1500)  # daqui a qtos milisegundos aparecem inimigos
            # cenemies = 0
            spawn_time = pygame.time.get_ticks() + cenemiesvar
            
        # Count cycles
        # cenemies += 1

    # Move enemies
    for c, (enemy_l, enemy_x, enemy_y, enemy_o, enemy_v) in enumerate(enemiespresents):
        if enemy_l[1] <= level-3:
            if enemy_o == -1:
                screen.blit(enemy_l[0][0], (enemy_x, enemy_y))
                if enemy_x > x and not(y+p_list[level][2][1] < enemy_y or y > enemy_y+enemy_l[0][2][1]):
                    enemy_v = 45/100
                    enemy_o = 1
                    enemy_x += enemy_v*dt
                    enemiespresents[c] = (enemy_l, enemy_x, enemy_y, enemy_o, enemy_v)
                else:
                    enemy_x -= enemy_v*dt
                    enemiespresents[c] = (enemy_l, enemy_x, enemy_y, enemy_o, enemy_v)
            elif enemy_o == 1:
                screen.blit(enemy_l[0][1], (enemy_x, enemy_y))
                if enemy_x < x and not(y+p_list[level][2][1] < enemy_y or y > enemy_y+enemy_l[0][2][1]):
                    enemy_v = 45/100
                    enemy_o = -1
                    enemy_x -= enemy_v*dt
                    enemiespresents[c] = (enemy_l, enemy_x, enemy_y, enemy_o, enemy_v)
                else:
                    enemy_x += enemy_v*dt
                    enemiespresents[c] = (enemy_l, enemy_x, enemy_y, enemy_o, enemy_v)

        elif enemy_l[1] == 99:
            if enemy_o == -1:
                if e99c<40:
                    screen.blit(enemy_l[0][0], (enemy_x, enemy_y))
                else:
                    screen.blit(enemy_l[0][3], (enemy_x, enemy_y))
                if enemy_x < x and not(y+p_list[level][2][1] < enemy_y or y > enemy_y+enemy_l[0][2][1]):
                    enemy_o = 1
                    enemy_x += enemy_v*dt
                    enemiespresents[c] = (enemy_l, enemy_x, enemy_y, enemy_o, enemy_v)
                else:
                    enemy_x -= enemy_v*dt
                    enemiespresents[c] = (enemy_l, enemy_x, enemy_y, enemy_o, enemy_v)
            elif enemy_o == 1:
                if e99c<40:
                    screen.blit(enemy_l[0][1], (enemy_x, enemy_y))
                else:
                    screen.blit(enemy_l[0][4], (enemy_x, enemy_y))
                if enemy_x > x and not(y+p_list[level][2][1] < enemy_y or y > enemy_y+enemy_l[0][2][1]):
                    enemy_o = -1
                    enemy_x -= enemy_v*dt
                    enemiespresents[c] = (enemy_l, enemy_x, enemy_y, enemy_o, enemy_v)
                else:
                    enemy_x += enemy_v*dt
                    enemiespresents[c] = (enemy_l, enemy_x, enemy_y, enemy_o, enemy_v)
                
        elif enemy_o == -1:
            if enemy_l[1] == 98 and enemy_x > x and not(y+p_list[level][2][1] < enemy_y or y > enemy_y+enemy_l[0][2][1]):
                enemy_v += 1.5/100
            screen.blit(enemy_l[0][0], (enemy_x, enemy_y))
            enemy_x -= enemy_v*dt
            enemiespresents[c] = (enemy_l, enemy_x, enemy_y, enemy_o, enemy_v)
            
        elif enemy_o == 1:
            if enemy_l[1] == 98 and -enemy_l[0][2][0] < enemy_x < x and not(y+p_list[level][2][1] < enemy_y or y > enemy_y+enemy_l[0][2][1]):
                enemy_v += 1.5/100
            screen.blit(enemy_l[0][1], (enemy_x, enemy_y))
            enemy_x += enemy_v*dt
            enemiespresents[c] = (enemy_l, enemy_x, enemy_y, enemy_o, enemy_v)

        if enemy_x < -204 or enemy_x > WIDTH + enemy_l[0][2][0]: # -enemy_l[0][2][0]
            enemiespresents.remove((enemy_l, enemy_x, enemy_y, enemy_o, enemy_v))
            yweights[dposy[enemy_y]] = 1
            continue

        # Colision
        if overlaps(x,y,p_list[level][2][0],p_list[level][2][1], enemy_x, enemy_y, enemy_l[0][2][0], enemy_l[0][2][1]):
            if enemy_l[1] > level:
                DEAD = True
            else:
                enemiespresents.remove((enemy_l, enemy_x, enemy_y, enemy_o, enemy_v))
                yweights[dposy[enemy_y]] = 1
                energy += energydict[enemy_l[1]]

    # Light inguia
    e99c += 1
    if e99c == 50:
        e99c = 0

    # Grow player
    if energy >= 1:  # 1300
        level = 8
        weight = [1, 1, 2, 3, 3, 3, 4, 4, 5, 6, 7, 8, 8, 7, 6, 4]
    elif energy >= 400:  # 829
        level = 7
        weight = [1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 8, 0, 0, 0, 8, 4]
    elif energy >= 200:  # 488
        level = 6
        weight = [1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 0, 0, 0, 0, 7, 4]
    elif energy >= 100:  # 262
        level = 5
        weight = [1, 2, 2, 3, 3, 4, 5, 5, 6, 0, 0, 0, 0, 0, 6, 4]
    elif energy >= 50:  # 133
        level = 4
        weight = [1, 2, 2, 3, 3, 4, 5, 5, 0, 0, 0, 0, 0, 0, 5, 4]
    elif energy >= 25:  # 55
        level = 3
        weight = [1, 2, 2, 3, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4]
    elif energy >= 10:  # 19
        level = 2
        weight = [1, 2, 2, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4]
    elif energy >= 5:  # 5
        level = 1
        weight = [1, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3]

    if energy > best_score:
        best_score = energy

    draw_score(energy, WIDTH//10, HEIGHT-HLAYpoints)
    draw_score(best_score, 7.5*WIDTH//10, HEIGHT-HLAYpoints)

    # Check if is dead
    if DEAD:
        keys = pygame.key.get_pressed()
        if (x, y) != (0, 0):
            xd, yd = x, y
        x, y = 0, 0
        restart = startFont.render('Press SPACE to restart', 1, col['white'])
        screen.blit(restart, (11*WIDTH//32, 5*HEIGHT//6))
        if skullt < 100:
            screen.blit(skull, (xd, yd))
            skullt += 1
        if keys[pygame.K_SPACE]:
            DEAD = False
            energy = 0
            level = 0
            x = WIDTH // 2
            y = HEIGHT-HLAYpoints-40
            velx, vely = 0, -0.5
            savedp = player1[0]
            enemiespresents = []
            weight = [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            yweights = [1, 1, 1, 1, 1, 1, 1, 1]
            skullt = 0

    if menuf:
        menu()

    pygame.display.flip()
