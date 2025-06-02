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
greenC = (0,255,0)
blueC = (0,0,255)
tempC = (169,43,97)

clock = pygame.time.Clock()

ballImg = pygame.image.load("250x250 img 1.png")

gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("The Bouncing Ball")

def thingsDodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True , blackC)
    gameDisplay.blit(text, (0,0))

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
    thingCount = 1
    dodged = 0
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
        thingsDodged(dodged)
        if (x > (displayWidth - ballWidth)) or (x < 0):
            crash()
        if thingStartY > displayHeight:
            thingStartY = 0 - thingHeight
            thingStartX = random.randrange(0,displayWidth-thingWidth)
            # thingStartX = random.randrange(0,displayWidth)
            dodged+=1
            thingSpeed+=1
            thingWidth+=(dodged*1)
            # thingWidth+=(dodged*1.2)
        if y < (thingStartY + thingHeight):
            # print('y crossover')   # it works, just commented out because its a bit spammy
            # <--- Added parentheses here to group the two “collision” checks clearly:
            if ((x > thingStartX and x < (thingStartX + thingWidth)) or ((x + ballWidth) > thingStartX and (x + ballWidth) < (thingStartX + thingWidth))):
                # print('x crossover')  # it works, just commented out because its a bit spammy
                crash()

        pygame.display.update()
        clock.tick(60)
    pygame.quit()
    quit()

gameLoop()
pygame.quit()
quit()
