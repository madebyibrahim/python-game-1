import pygame
import time
import random

pygame.init()

displayWidth = 1000
displayHeight = 680
ballWidth = 250 #adjust as fit

blackC = (0,0,0)
whiteC = (255,255,255)
redC = (255,0,0)
greenC = (0,255,0)
blueC = (0,0,255)
blockC = (169,43,97)
lightGreenC = (116,245,24)
lightRedC = (224,52,72)

clock = pygame.time.Clock()

ballImg = pygame.image.load("250x250 img 1.png")

gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("The Hungry Mouth")

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

def gameIntro():
    intro = True
    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type ==  pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(whiteC)
        largeText = pygame.font.Font("freesansbold.ttf", 80)
        textSurf,textRect = textObjects("The Hungry Mouth", largeText)
        textRect.center = ((displayWidth/2), (displayHeight/4))
        gameDisplay.blit(textSurf, textRect)
        # pygame.draw.line(gameDisplay, (0, 0, 255), (displayWidth/2, 0), (displayWidth/2, displayHeight)) # vertical center line

        mousePos = pygame.mouse.get_pos()
        if (displayWidth/2-180)+120>mousePos[0]>(displayWidth/2-180) and 450+60>mousePos[1]>450:
            pygame.draw.rect(gameDisplay, lightGreenC, ((displayWidth/2-180),450,120,60))
        else:
            pygame.draw.rect(gameDisplay, greenC,((displayWidth/2-180),450,120,60))
        if (displayWidth/2+60) + 120> mousePos[0] > (displayWidth/2+60) and 450+ 60 >mousePos[1] > 450:
            pygame.draw.rect(gameDisplay, lightRedC, ((displayWidth/2+60),450,120,60))
        else: 
            pygame.draw.rect(gameDisplay, redC, ((displayWidth/2+60),450,120,60))

        pygame.display.update()
        clock.tick(30)

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
                pygame.quit()
                quit()
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
        things(thingStartX, thingStartY, thingWidth, thingHeight, blockC)
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
            thingWidth+=(dodged*1.2)
            # thingWidth+=(dodged*1.2)
        if y < (thingStartY + thingHeight):
            # print('y crossover')   # it works, just commented out because its a bit spammy
            # <--- Added parentheses here to group the two “collision” checks clearly:
            if ((x > thingStartX and x < (thingStartX + thingWidth)) or ((x + ballWidth) > thingStartX and (x + ballWidth) < (thingStartX + thingWidth))):
                # print('x crossover')  # it works, just commented out because its a bit spammy
                crash()

        pygame.display.update()
        clock.tick(60)

gameIntro()
gameLoop()
pygame.quit()
quit()
