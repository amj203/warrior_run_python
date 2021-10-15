# Abdulrazzak Jouhar 2020

import pygame
import math
import random
from pygame import mixer
import time

start_time = time.time()

#access to pygame
pygame.init()
#game screen
screen = pygame.display.set_mode((800,600))

#icon and captions and background
pygame.display.set_caption('warior run')
icon = pygame.image.load('static/shield.png')
pygame.display.set_icon(icon)
background = pygame.image.load('static/castle3.jpg')

#background music
def background_music():
    mixer.music.load('static/background.wav')
    mixer.music.play(-1)

#warior 
warior_body = pygame.image.load('static/helmet.png')
playerx = 750
playery = 536
playerx_change = 0
playery_change = 0

#shield 
shield_body = pygame.image.load('static/shield.png')
shieldx = 5
shieldy = 5

#kunai 
kunai_body = pygame.image.load('static/kunai.png')
kunaix = random.randint(410,800)
kunaiy = 0
kunaix_change = 5
kunaiy_change = 5

#axe 
axe_body = pygame.image.load('static/axe.png')
axex = random.randint(0,390)
axey = 0
axex_change = 5
axey_change = 5

# loses
loses = 0
font1 = pygame.font.Font('freesansbold.ttf',32)
font2 = pygame.font.Font('freesansbold.ttf',64)

def show_loses(x,y):
    num_loses = font1.render("loses: " + str(loses) ,True, (255,0,0))
    screen.blit( num_loses, (x , y))

textx = 660
texty = 10

def show_gameover(x,y):
    gameover = font2.render("Game Over" ,True, (255,0,0))
    screen.blit( gameover, (x , y))

text1x = 236
text1y = 236


def warior(x,y):
    screen.blit(warior_body, (x , y))

def shield(x,y):
    screen.blit(shield_body, (x , y))

def kunai(x,y):
    screen.blit(kunai_body, (x , y))

def axe(x,y):
    screen.blit(axe_body, (x , y))

def iscollision(playerx,playery,shieldx,shieldy):
    distanse = math.sqrt( (math.pow(shieldx-playerx ,2)) + (math.pow(shieldy-playery ,2)) )
    
    if distanse <= 20:
        return True
    else:
        return False

def iscollision1(playerx,playery,axex,axey):
    distanse1 = math.sqrt( (math.pow(axex-playerx ,2)) + (math.pow(axey-playery ,2)) )    

    if distanse1 <= 30:
        return True
    else:
        return False

def iscollision2(playerx,playery,kunaix,kunaiy):
    distanse2 = math.sqrt( (math.pow(kunaix-playerx ,2)) + (math.pow(kunaiy-playery ,2)) )    

    if distanse2 <= 30:
        return True
    else:
        return False

#exit virable
running = True
background_music()
#main loop
while running:
    screen.fill((255 , 255 , 255))
    screen.blit(background, (0 , 0))
    for event in pygame.event.get() :

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playery_change = 0
                    playerx_change = -1.5
                    #break
                if event.key == pygame.K_RIGHT:
                    playery_change = 0
                    playerx_change = 1.5
                    #break
                if event.key == pygame.K_UP:
                    playerx_change = 0
                    playery_change = -1.5
                    #break
                if event.key == pygame.K_DOWN:
                    playerx_change = 0
                    playery_change = 1.5
                    #break
                if event.key == pygame.K_SPACE:
                    playerx = playerx
                    playery = playery 
                    playerx_change = 0
                    playery_change = 0
                
                if event.key == pygame.K_s:
                    axex = axex
                    axey = axey
                    axex_change = 0
                    axey_change = 0

                if event.key == pygame.K_d:
                    kunaix = kunaix
                    kunaiy = kunaiy
                    kunaix_change = 0
                    kunaiy_change = 0


    playerx += playerx_change
    if playerx <= -13:
        playerx = -13
    elif playerx >= 750:
        playerx = 750
    playery += playery_change
    if playery <= 0:
        playery = 0
    elif playery >= 536:
        playery = 536

    kunaix += kunaix_change
    if kunaix <= 0:
        kunaix = 0
        kunaix_change = 5
    elif kunaix >= 736:
        kunaix = 736 
        kunaix_change = -5
    kunaiy += kunaiy_change
    if kunaiy <= 0:
        kunaiy = 0
        kunaiy_change = 5
    elif kunaiy >= 536:
        kunaiy = 536
        kunaiy_change = -5

    axex += axex_change
    if axex <= 0:
        axex = 0
        axex_change = 5
    elif axex >= 736:
        axex = 736
        axex_change = -5
    axey += axey_change
    if axey <= 0:
        axey = 0
        axey_change = 5
    elif axey >= 536:
        axey = 536
        axey_change = -5     

    # store true or false
    collision = iscollision(playerx,playery,shieldx,shieldy) 
    collision1 = iscollision1(playerx,playery,axex,axey)
    collision2 = iscollision2(playerx,playery,kunaix,kunaiy)

    if collision1:
        loses +=1
        playerx = 750
        playery = 536
        playerx_change = 0
        playerx_change = 0
        mixer.music.load('static/sword-hit1.wav')
        mixer.music.play()
        time.sleep(0.5)
        background_music()
         

    if collision2:
        loses +=1
        playerx = 750
        playery = 536
        playerx_change = 0
        playerx_change = 0
        mixer.music.load('static/sword-hit1.wav')
        mixer.music.play()
        time.sleep(0.5)
        background_music()
     

    if collision:
        playerx_change = 0
        playerx_change = 0
        axex = axex
        axey = axey
        axex_change = 0
        axey_change = 0
        kunaix = kunaix
        kunaiy = kunaiy
        kunaix_change = 0
        kunaiy_change = 0
        mixer.music.load('static/win-sound.wav')
        mixer.music.play()
        time.sleep(1.5)
        running = False

    if loses == 3:
        playerx = 750
        playery = 536
        playerx_change = 0
        playerx_change = 0
        axex = axex
        axey = axey
        axex_change = 0
        axey_change = 0
        kunaix = kunaix
        kunaiy = kunaiy
        kunaix_change = 0
        kunaiy_change = 0
        mixer.music.load('static/game-over.wav')
        mixer.music.play()
        show_gameover(text1x,text1y)
        time.sleep(1.5)
        running = False
        
        
    show_loses(textx , texty) 
    shield(shieldx , shieldy)
    warior(playerx , playery)
    kunai(kunaix , kunaiy)
    axe(axex , axey)
    #display what on screen
    pygame.display.update()         