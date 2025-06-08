from utils import helpers
import pygame

class hungryMouth:
    def __init__(self, gameDisplay):
        self.width = 150
        self.height = 150
        (self.displayWidth, self.displayHeight) = gameDisplay.get_size()
        self.x = (self.displayWidth)//2 - self.width//2
        self.y = self.displayHeight - self.height
        self.xChange = 20
        self.imageOpen = pygame.image.load(helpers.resource_path('assets/images/small_open_tomato.png'))
        self.imagePoison = pygame.image.load(helpers.resource_path('assets/images/small_poison_tomato.png'))
        self.poisonTimer = 0

    def drawMouth(self, gameDisplay):
        if self.poisonTimer > 0:
            gameDisplay.blit(self.imagePoison, (self.x,self.y))
        else:
            gameDisplay.blit(self.imageOpen, (self.x,self.y))

    def updatePoisonTimer(self):
        # Call every frame to reduce poison timer
        if self.poisonTimer > 0:
            self.poisonTimer -= 1

    def activatePoisonEffect(self, duration = 45):
        # Activate poison effect for 'duration' frames (30fps = 1 second)
        self.poisonTimer = duration

    def moveLeft(self):
        # self.x = max(self.x - self.xChange, 0)
        new_x = self.x - self.xChange  # Calculate new position
        if new_x < 0:
            self.x = 0  # Prevent going off the left edge
        else:
            self.x = new_x # move left normally

    def moveRight(self):
        # self.x = min(self.x + self.xChange, self.displayWidth - self.width)
        new_x = self.x + self.xChange  # Calculate new position
        max_x = self.displayWidth - self.width  # Right boundary
        if new_x > max_x:
            self.x = max_x  # Prevent going off the right edge
        else:
            self.x = new_x  # Move right normally