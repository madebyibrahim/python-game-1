from utils import helpers
import pygame
import random

class food:
    def __init__(self, gameDisplay,isPoison, langData):
        displayWidth, _ = gameDisplay.get_size()
        self.x = random.randrange(0,displayWidth-110,1)
        self.y = -100
        self.isPoison = isPoison
        self.fallSpeed = random.randrange(5,10,1)
        self.width = 110
        self.height = 110
        if isPoison:
            poisonData = random.choice(langData["poisonFood"])
            imagePath = poisonData.get("image")
            self.sfxPath = poisonData.get("sfx", "")
        else:
            imagePath = random.choice(langData['healthyFood'])
            self.sfxPath = ''
        originalImage = pygame.image.load(helpers.resource_path(imagePath))
        self.image = pygame.transform.scale(originalImage, (110,110))        
        
    def updatePos(self):
        self.y += self.fallSpeed

    def drawFood(self, gameDisplay):
        gameDisplay.blit(self.image , (self.x,self.y))

    def getRect(self):
        return pygame.Rect(self.x,self.y,self.width,self.height)
    
    def isOffScreen(self, gameDisplay):
        _, displayHeight = gameDisplay.get_size()
        return self.y > displayHeight + 30

    def getSfxPath(self):
        return self.sfxPath