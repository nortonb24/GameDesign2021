#Brenna Norton
#6/16/2021
#K_UP                  up arrow
#K_DOWN                down arrow
#K_RIGHT               right arrow
#K_LEFT                left arrow
import pygame, time, sys
from pygame import color
from pygame.constants import K_SPACE
from pygame.display import flip, update
from pygame.draw import rect
pygame.init()
pygame.time.delay(100)
WIDTH=500
HEIGHT=600
#create object to open window

bg=pygame.image.load("NewImages\\Bee.png")
some=pygame.image.load("NewImages\\characters.png")
white=[255,255,255]
yellow=[200,190,0]
green=[50,25,255]
red=[255, 0, 0]
purple=[255, 0, 255]
blue= [0, 0, 255]
#create an object to open window

screen=pygame.display.set_mode((WIDTH,HEIGHT))

screen.fill(green)
screen.blit(bg, (0,0))

pygame.display.set_caption("My Game") #change title on the screen and can also change icon 
pygame.display.update() #command to actually do something

#you must alweays have this loop
check = True
x=10
y=10
xr= 40
yr= 50
rad=30
hbox, wbox=20,20
rect=pygame.Rect(x,y,hbox,wbox)
rect2=pygame.Rect(xr, yr, hbox, wbox)
JumpCheck=False
jump=10
while check:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            check= False
    speed=5
    keyBoardKey=pygame.key.get_pressed() #checking what key is pressed 
    if keyBoardKey[pygame.K_LEFT]: #Moving left on x (-)
        rect.x -=speed
        rad -=speed
    if keyBoardKey[pygame.K_RIGHT]: #Moving right on x (+)
        rect.x +=speed
        rad +=speed
    #to check if we are going to mump
    

    if not JumpCheck: 
        if keyBoardKey[pygame.K_UP]:        #Moving up on y (-)
            rect.y -= speed 
            #yR -= speed
        if keyBoardKey[pygame.K_DOWN]:        #Moving down on y (+)
            rect.y += speed
           # yR += speed
        if keyBoardKey[pygame.K_SPACE]:
            JumpCheck=True
    else:
        if jump >=-10:
            rect.y -=(jump*abs(jump))/2
            #yR -=(jump*abs(jump))/2
            jump-=1
        else:
            jump = 10
            JumpCheck=False

    if keyBoardKey[pygame.K_s]:
        rad -=speed
    if keyBoardKey[pygame.K_f]:
        rad +=speed

    if rect.x < 0: rect.x=0
    if rect.x > WIDTH-wbox: rect.x=WIDTH-wbox
    if rect.y < 0: rect.y=0
    if rect.y > HEIGHT-hbox: rect.y=HEIGHT-hbox
    if rad < 0: rad=1

    if rad > WIDTH-x: rad =WIDTH-x
    if rect.colliderect(rect):
        rect.x -=3
        rect.x +=3
    

    if keyBoardKey[pygame.K_j]: #Moving left on x (-)
        rect2.x -=speed
        rad -=speed
    if keyBoardKey[pygame.K_k]: #Moving right on x (+)
        rect2.x +=speed
        rad +=speed
    if keyBoardKey[pygame.K_i]: #Moving up on y (-)
        rect2.y -=speed
    if keyBoardKey[pygame.K_m]: #Moving down on y (+)
        rect2.y +=speed


    screen.fill(green)
    screen.blit(bg, (0,0))
    pygame.draw.rect(screen, (yellow), rect) #where, what color, what shape
    pygame.draw.rect(screen, (blue), rect2)
    pygame.draw.circle(screen, (red), (x+300, y+200), rad,2)

    pygame.display.flip()
    pygame.time.delay(30)
pygame.QUIT
