import sys
import os
import pygame
from utils import colors as color
import arabic_reshaper
from bidi.algorithm import get_display



#snippet taken to compile all images used in one exe file and have no errors. usage: instead of "E:/myfile.png" use resource_path("E:/myfile.png")
def resource_path(relative_path):
    """    Get absolute path to resource.     Works in development and after PyInstaller bundling."""
    try:
        # If running from a PyInstaller bundle
        base_path = sys._MEIPASS
    except AttributeError:
        # Use the directory of main.py
        base_path = os.path.dirname(os.path.abspath(sys.argv[0]))

    return os.path.join(base_path, relative_path)

#Properly render arabic text
def makeArabic(text: str) -> str:
    reshapeText = arabic_reshaper.reshape(text) 
    return get_display(reshapeText)

#Draw a rectangle
def rectangle(gameDisplay, thingX, thingY, thingW, thingH, color):
    pygame.draw.rect(gameDisplay, color, [thingX, thingY, thingW, thingH])

#Converts a text to a surface
def textToSurface(text, font, color=color.black):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

#Function to display a text message
def messageDisplay(gameDisplay, text, fontSize = 115, fontTTF = "freesansbold.ttf",  color = color.black, xCen=-1, yCen=-1):
    (displayWidth, displayHeight) = gameDisplay.get_size()
    textSize = pygame.font.Font(fontTTF, fontSize)
    textSurf, textRect = textToSurface(text, textSize, color)
    if (xCen == -1):
        xCen = (displayWidth/2)
    if (yCen == -1):
        yCen = (displayHeight/2)   
    textRect.center = (xCen, yCen)
    gameDisplay.blit(textSurf, textRect)

def showImage(gameDisplay, imagePath, x=-1,y=-1, size = None):
    img = pygame.image.load(resource_path(imagePath))
    (displayWidth, displayHeight) = gameDisplay.get_size()
    if size:
        img = pygame.transform.scale(img, size)
    if x==-1:
        x=displayWidth/2
    if y == -1:
        y=displayHeight/2
    gameDisplay.blit(img,(x,y))

def button(gameDisplay, msg, x, y, w, h, inactiveColor, activeColor, events, action=None):
    mousePos = pygame.mouse.get_pos()
    if x < mousePos[0] < x + w and y < mousePos[1] < y + h:
        pygame.draw.rect(gameDisplay, activeColor, (x, y, w, h))
        for event in events:
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and action is not None):
                action()
    else:
        pygame.draw.rect(gameDisplay, inactiveColor, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf", 30)
    textSurf, textRect = textToSurface(msg, smallText)
    textRect.center = (x + (w / 2), y + (h / 2))
    gameDisplay.blit(textSurf, textRect)