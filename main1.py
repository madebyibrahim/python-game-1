#Version 1.0

## when we finish change the theme and make it a mouth thats eats food and avoids poison

import pygame
import time
import random

import utils.langSelection as langSelection
from utils import colors as color
from utils import helpers


pygame.init()

displayWidth = 1000
displayHeight = 690
mouthWidth = 150  # adjust as fit

clock = pygame.time.Clock()

ballImg = pygame.image.load(helpers.resource_path("250x250_img_1.png"))

gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("The Hungry Mouth")

gameIcon = pygame.image.load(helpers.resource_path("gameIcon.png"))
pygame.display.set_icon(gameIcon)

pause = False

# def pauseFunc():
#     largeText = pygame.font.SysFont("comicsansms",115)
#     textSurf, textRect = textObjects("Paused", largeText)
#     textRect.center = ((displayWidth/2), (displayHeight/4))
#     gameDisplay.blit(textSurf, textRect)
#     while pause:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()
#         gameDisplay.fill(whiteC)
#         button("PLAY", displayWidth / 2 - 180, 450, 120, 60, greenC, lightGreenC, unpause)
#         button("QUIT", displayWidth / 2 + 60, 450, 120, 60, redC, lightRedC, quitGame)

#         pygame.display.update()
#         clock.tick(15)

# def unpause():
#     global pause
#     pause = False

# def thingsDodged(count):
#     font = pygame.font.SysFont(None, 25)
#     text = font.render("Dodged: " + str(count), True, blackC)
#     gameDisplay.blit(text, (0, 0))


# def things(thingX, thingY, thingW, thingH, color):
#     pygame.draw.rect(gameDisplay, color, [thingX, thingY, thingW, thingH])


# def ballFunc(x, y):
#     gameDisplay.blit(ballImg, (x, y))


# def textObjects(text, font):
#     textSurface = font.render(text, True, blackC)
#     return textSurface, textSurface.get_rect()


# def messageDisplay(text):
#     largeText = pygame.font.Font("freesansbold.ttf", 115)
#     textSurf, textRect = textObjects(text, largeText)
#     textRect.center = (displayWidth / 2, displayHeight / 2)
#     gameDisplay.blit(textSurf, textRect)
#     pygame.display.update()
#     time.sleep(2)
#     gameLoop()


# def crash():
#     largeText = pygame.font.SysFont("comicsansms",115)
#     TextSurf, TextRect = textObjects("You Crashed", largeText)
#     TextRect.center = ((displayWidth/2),(displayHeight/4))
#     gameDisplay.blit(TextSurf, TextRect)
#     while True:
#         for event in pygame.event.get():
#             #print(event)
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()
#         gameDisplay.fill(whiteC)
        

#         button("Play Again",150,450,100,50,greenC,lightGreenC,gameLoop)
#         button("Quit",550,450,100,50,redC,lightRedC,quitGame)

#         pygame.display.update()
#         clock.tick(15) 
# def gameIntro():
#     intro = True
#     while intro:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()

#         gameDisplay.fill(whiteC)

#         largeText = pygame.font.Font("freesansbold.ttf", 80)
#         textSurf, textRect = textObjects("The Hungry Mouth", largeText)
#         textRect.center = (displayWidth / 2, displayHeight / 4)
#         gameDisplay.blit(textSurf, textRect)

#         button("PLAY", displayWidth / 2 - 180, 450, 120, 60, greenC, lightGreenC, gameLoop)
#         button("QUIT", displayWidth / 2 + 60, 450, 120, 60, redC, lightRedC, quitGame)

#         pygame.display.update()
#         clock.tick(30)


# def quitGame():
#     pygame.quit()
#     quit()


# def button(msg, x, y, w, h, ic, ac, action=None):
#     mousePos = pygame.mouse.get_pos()
#     mouseClicked = pygame.mouse.get_pressed()
#     # print(mouseClicked)  # can be commented out once you confirm clicks work

#     if x < mousePos[0] < x + w and y < mousePos[1] < y + h:
#         pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
#         if mouseClicked[0] == 1 and action is not None:
#             action()
#     else:
#         pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

#     smallText = pygame.font.Font("freesansbold.ttf", 30)
#     textSurf, textRect = textObjects(msg, smallText)
#     textRect.center = (x + (w / 2), y + (h / 2))
#     gameDisplay.blit(textSurf, textRect)


# def gameLoop():
#     x = 250
#     y = 354
#     xChange = 0

#     thingWidth = 100
#     thingHeight = 100
#     thingStartX = random.randrange(0, displayWidth - thingWidth)
#     thingStartY = -1500
#     thingSpeed = 7  # can increase or decrease to affect difficulty
#     dodged = 0

#     gameExit = False

#     while not gameExit:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     xChange = -15
#                 if event.key == pygame.K_RIGHT:
#                     xChange = 15
#                 if event.key == pygame.K_p:
#                     pause = True
#                     pauseFunc()
#             if event.type == pygame.KEYUP:
                
#                 xChange = 0  # stop moving when key is released

#         x += xChange

#         gameDisplay.fill(whiteC)
#         things(thingStartX, thingStartY, thingWidth, thingHeight, blockC)

#         thingStartY += thingSpeed
#         ballFunc(x, y)
#         thingsDodged(dodged)

#         # Boundary check: crash if mouth goes off-screen
#         if (x > (displayWidth - mouthWidth)) or (x < 0):
#             crash()

#         # When the “thing” moves past bottom, reset and speed up
#         if thingStartY > displayHeight:
#             thingStartY = 0 - thingHeight
#             thingStartX = random.randrange(0, displayWidth - thingWidth)
#             dodged += 1
#             thingSpeed += 1
#             thingWidth += (dodged)

#         # Collision: check vertical overlap first, then horizontal
#         if y < (thingStartY + thingHeight):
#             if (
#                 (x > thingStartX and x < (thingStartX + thingWidth))
#                 or ((x + mouthWidth) > thingStartX and (x + mouthWidth) < (thingStartX + thingWidth))
#             ):
#                 crash()

#         pygame.display.update()
#         clock.tick(60)


# gameIntro()


