import pygame
import math
import random
from pygame import mixer

pygame.init()
screen = pygame.display.set_mode((1000, 600))

#initialaizing the caption 
pygame.display.set_caption("Dine-saurs")

# initializing the icon
icon = pygame.image.load('din.png')
pygame.display.set_icon(icon)

# initializing the sound
mixer.music.load("bgsound.wav")
mixer.music.play(-1)

# intializing the dinosaur
dinosaurImg = pygame.image.load('dinosaur.png')
dinosaurX = 450
dinosaurY = 900
dinosaurX_change = 0
dinosaurY_change = 0
pixel_change = 0.9
fire_change = 2

# initializing the egg
eggImg = pygame.image.load("egg.png").convert()
eggX = 50
eggY = 50

# initializing the fire
fireImg = pygame.image.load('fire.png')
fireX = 100
fireY = 470

# showing the score
score_count = 0
font = pygame.font.Font("freesansbold.ttf", 28)
testX = 10
testY = 10

# background
backgroundImg = pygame.image.load('bgg.jpg').convert()
x = 0

# collision
def isCollision(eggX, eggY, dinosaurX, dinosaurY):
    distance = math.sqrt((math.pow(eggX - dinosaurX,2))+ (math.pow(eggY - dinosaurY, 2)))
    if distance < 27:
        return True
    else:
        return False  

def fireCollision(fireX, fireY, dinosaurX, dinosaurY):
    distance = math.sqrt((math.pow(fireX - dinosaurX,2))+ (math.pow(fireY - dinosaurY, 2)))
    if distance < 27:
        return True
    else:
        return False            
# loop

running = True

while running:
   
    screen.blit(backgroundImg, (x, 0))
    screen.blit(eggImg, (eggX,eggY))
    screen.blit(dinosaurImg, (dinosaurX, dinosaurY)) 
    score = font.render("score: " + str(score_count), True, (255, 255,255))
    screen.blit(score,(testX,testY))
    screen.blit(fireImg, (fireX, fireY))

    pygame.display.update()  
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                dinosaurX_change =+ pixel_change
                scrollbackground(-pixel_change, 0)
            if event.key == pygame.K_LEFT:
                dinosaurX_change =- pixel_change

            # jumping
            if event.key == pygame.K_UP:
                dinosaurY_change =- pixel_change
            # going down    
            if event.key == pygame.K_DOWN:
                dinosaurY_change =+ pixel_change
                
            # going on place
            if event.key == pygame.K_SLASH:
                print("Fire")
               
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                dinosaurX_change = 0        

# boundry
    if dinosaurX <= 0:
        dinosaurX = 0
    elif dinosaurX >= 936:
        dinosaurX = 936
    if dinosaurY <= 0:
        dinosaurY = 0
    elif dinosaurY >= 470:
        dinosaurY = 470  

# the dinosaur
    dinosaurX += dinosaurX_change  
    dinosaurY += dinosaurY_change  
    
    # fire movement
    fireY += fire_change
    if fireX <= 0:
        fireX = 0
    if fireY >= 510:
        fireY = 0
      
        fireX = random.randint(0, 968)
      
        #collision
    collision = isCollision(eggX, eggY, dinosaurX, dinosaurY)
    if collision:
    # initializing the sound
        mixer.music.load("eggs.wav")
        mixer.music.play()
        score_count += 1
        
        
        eggX = random.randint(0, 968)
        eggY = random.randint(100, 500)  

    collision1 = fireCollision(fireX, fireY, dinosaurX, dinosaurY)
    
    if collision1: 
        # initializing the sound
        mixer.music.load("die.wav")
        mixer.music.play()  
        
        running = False
       
   
    pygame.display.update()