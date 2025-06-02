import pygame
import time
import random

pygame.init()

displayWidth = 800
displayHeight = 600
ballWidth = 250 #adjust as fit

blackC = (0,0,0)
whiteC = (255,255,255)
redC = (255,0,0)




clock = pygame.time.Clock()

ballImg = pygame.image.load("250x250 img 1.png")

gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("The Bouncing Ball")

def things(thingX, thingY, thingW, thingH, color):
    pygame.draw.rect(gameDisplay, color, [thingX, thingY, thingW, thingH])

def ballFunc(x,y):
    gameDisplay.blit(ballImg, (x,y))

def textObjects(text, font):
    textSurface = font.render(text, True, blackC)
    return textSurface, textSurface.get_rect()

def messageDisplay(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    textSurf, textRect = textObjects(text, largeText)
    textRect.center =  ((displayWidth/2), (displayHeight/2))
    gameDisplay.blit(textSurf, textRect)
    pygame.display.update()
    time.sleep(2)
    gameLoop()

def crash():
    messageDisplay('You crashed!')

def gameLoop():
    x = 250
    y = 354
    # x = (displayWidth * 0.45) # random x coordinate 
    # y = (displayHeight * 0.8) # x is positive from left to right and y is postive from up to down.
    xChange = 0
    thingWidth = 100
    thingHeight = 100
    thingStartX = random.randrange(0,displayWidth-thingWidth)
    # thingStartX = random.randrange(0,displayWidth) # this is wrong
    thingStartY = -3600
    thingSpeed = 7 # can increase or decrease to affect difficulty

    gameExit = False

    while not gameExit: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xChange = -15
                if event.key == pygame.K_RIGHT:
                    xChange = 15
            if event.type == pygame.KEYUP:
                # if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:   # not really needed
                    xChange = 0
        x += xChange   
        gameDisplay.fill(whiteC)
        things(thingStartX, thingStartY, thingWidth, thingHeight, redC)
        thingStartY += thingSpeed
        ballFunc(x,y)        
        if (x > (displayWidth - ballWidth)) or (x < 0):
            crash()
        if thingStartY>displayHeight:
            thingStartY = 0 - thingHeight
            thingStartX = random.randrange(0,displayWidth-thingWidth)
            # thingStartX = random.randrange(0,displayWidth)
        if y < thingStartY + thingHeight:
            print('y crossover')
            if x > thingStartX and x < thingStartX + thingWidth or x + ballWidth > thingStartX and x + ballWidth < thingStartX + thingWidth:
                print('x crossover')
                crash()

        pygame.display.update()
        clock.tick(60)
    pygame.quit()
    quit()
gameLoop()
pygame.quit()
quit()

