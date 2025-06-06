import sys
import os
import pygame
from utils import colors as color
import arabic_reshaper
from bidi.algorithm import get_display

#snippet taken to compile all images used in one exe file and have no errors. usage: instead of "E:/myfile.png" use resource_path("E:/myfile.png")
import os
import sys

def resource_path(relative_path):
    """    Get absolute path to resource.     Works in development and after PyInstaller bundling."""
    try:
        # If running from a PyInstaller bundle
        base_path = sys._MEIPASS
    except AttributeError:
        # Use the directory of main.py
        base_path = os.path.dirname(os.path.abspath(sys.argv[0]))

    return os.path.join(base_path, relative_path)

def makeArabic(text: str) -> str:
    reshapeText = arabic_reshaper.reshape(text) 
    return get_display(reshapeText)

def rectangle(gameDisplay, thingX, thingY, thingW, thingH, color):
    pygame.draw.rect(gameDisplay, color, [thingX, thingY, thingW, thingH])

def textToSurface(text, font, color=color.black):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

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



