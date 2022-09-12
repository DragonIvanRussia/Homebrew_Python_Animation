#Libraries

import pygame, sys
from pygame import *
from pygame import mixer
from pygame.locals import *
from time import sleep
from threading import Thread
from random import *

#Initialization

pygame.init()
mixer.init()
#display_surface = pygame.display.set_mode((980, 560))
display_surface = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
display_surface.fill((255,255,255))
pygame.display.flip()

mainLoop = True
Exec = 0
UP = 1
LFW = 1
LFWA = 1
LFBW = 1
LFFW = 1
Start = 1
StartW = 1
StartWA = 1
StartBW = 1
StartFW = 1

Fade = 0
Cycle = 0
BackWater = pygame.image.load('back.png').convert_alpha() 
FrontWater = pygame.image.load('front.png').convert_alpha() 
Bubble = pygame.image.load('bubble.png').convert_alpha() 
BubbleAlt = pygame.image.load('bubble2.png').convert_alpha() 
Wave = pygame.image.load('wave1.png').convert_alpha() 
WaveAlt = pygame.image.load('wave2.png').convert_alpha() 
Text = pygame.image.load('text.png').convert_alpha() 

BWX=0
FWX=0
BX=0
BAX=0
WX=0
WAX=0
TX=0

BY=0
FWY=0
Y=1000
BAY=0
TY=100

fadeout = Surface((1920, 1080))
fadeout = fadeout.convert()
fadeout.fill((0,0,0))
        
def QuitToWindows():
    global mainLoop
    mainLoop = False
def Update():
    global BackWater, FrontWater, Wave, WaveAlt, BWX, WX, WAX, FWX, TX, Y, TY, display_surface
    display_surface.fill((255,255,255))
    if Exec==1:
        display_surface.blit(FrontWater,(FWX,FWY))
    else:
        display_surface.blit(FrontWater,(FWX,Y))
    display_surface.blit(BackWater,(BWX,Y))
    display_surface.blit(Wave,(WX-250, Y))
    display_surface.blit(WaveAlt,(WAX-250, Y))
    if Exec==1:
        display_surface.blit(Text,(TX, TY-100))
    fadeout.set_alpha(Cycle)
    display_surface.blit(fadeout, (0, 0))
    pygame.display.flip()
    
def IntroMusic():
    mixer.music.load('entry.mp3')
    mixer.music.play()
def LoopMusic():
    mixer.music.load('music.mp3')
    mixer.music.play()

def Intro():
    print("hi")
    sleep(1.5)
    Update()


IntroMusic()
Intro()
while mainLoop:
    if pygame.time.get_ticks() >= 6000 and Exec==0:
        Update()
        display_surface.fill((255,255,255))
        pygame.display.flip()
        pygame.time.wait(120)
        Exec=1
        Update()
    #Intro
    if Y>100:
        Y -= 4
    elif Y>20:
        Y -= 3
    elif Y>0:
        Y -= 1
    else:
        Y = 0
        
    if Exec==1 and UP==1 and Start>=1:
        if TY>=80:
            TY-=1
        elif TY>=60:
            TY-=2
        elif TY>=20:
            TY-=2
        elif TY>0:
            TY-=1
        else:
            UP=0
            Start=0
    if Exec==1 and UP==0.0 and Start>=1:
        if TY<=0:
            TY+=1
        elif TY<=20:
            TY+=1
        elif TY<=80:
            TY+=2
        elif TY<=100:
            TY+=1
        else:
            UP=1
            Start=0
            
    if LFW==1 and StartW>=1:
        if WX>-300:
            WX-=3
        else:
            LFW=0
            StartW=0
    if LFW==0 and StartW>=1:
        if WX<=300:
            WX+=3
        else:
            LFW=1
            StartW=0

    if LFWA==1 and StartWA>=2:
        if WAX>-400:
            WAX-=2
        else:
            WAX=-400
            LFWA=0
            StartWA=0
    if LFW==0 and StartWA>=2:
        if WAX<=400:
            WAX+=3
        else:
            LFWA=1
            WAX=400
            StartWA=0

    if LFBW==1 and StartBW>=0.5:
        if BWX>-50:
            BWX-=0.5
        else:
            BWX=-50
            LFBW=0
            StartBW=0
    if LFBW==0 and StartBW>=1:
        if BWX<=50:
            BWX+=0.5
        else:
            LFBW=1
            BWX=50
            StartBW=0

    if LFFW==1 and StartFW>=3:
        if FWY>0:
            FWY-=0.2
        else:
            FWY=0
            LFFW=0
            StartFW=0
    if LFFW==0 and StartFW>=3:
        if FWY<=20:
            FWY+=0.2
        else:
            LFFW=1
            FWY=20
            StartFW=0
    if Fade==1:
        Cycle+=1
        mixer.music.set_volume(1-(Cycle/255))
    if Cycle==255:
        sleep(1)
        QuitToWindows()
    if StartW<=1:
        StartW+=0.1
    if StartWA<=2:
        StartWA+=0.1
    if StartBW<=1:
        StartBW+=0.1
    if StartFW<=3:
        StartFW+=0.1
    if Start<=1:
        Start+=0.1
    left, middle, right = pygame.mouse.get_pressed()
    if pygame.time.get_ticks() >= 12000 and left or middle or right:
        Fade=1
    pygame.event.get()
    Update()
pygame.quit()
