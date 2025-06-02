# Basically at the level of the hardware, if you reduce frequency , you can see the image slowly being generated/ rendered from top left to right, top to bottom, line by line, pixel by pixel

import pygame
import time
import numpy as np

pygame.init()

displayWidth = 800
displayHeight = 600
ballWidth = 80

blackC = (0, 0, 0)
whiteC = (255, 255, 255)
redC = (255, 0, 0)

clock = pygame.time.Clock()

# Load the image
ballImg = pygame.image.load("250x250 img 1.png")

# Get image dimensions
imgWidth, imgHeight = ballImg.get_size()

# Create a new surface for pixel-by-pixel rendering
renderSurface = pygame.Surface((imgWidth, imgHeight))

# Convert the image to a 3D array (width x height x color channels)
pixelArray = pygame.surfarray.array3d(ballImg)

# Set up the game display
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("The Bouncing Ball")

# Simulate 1 MHz processing: render each pixel with a 1 microsecond delay
for y in range(imgHeight):
    for x in range(imgWidth):
        # Get RGB values of the pixel
        r, g, b = pixelArray[x][y]

        # Set the pixel on the render surface
        renderSurface.set_at((x, y), (r, g, b))

        # Optional: update the display to visualize rendering (commented out for performance)
        gameDisplay.blit(renderSurface, (0, 0))
        pygame.display.update(pygame.Rect(x, y, 1, 1))

        # Delay to simulate 1 MHz processing frequency (1 microsecond per pixel)
        time.sleep(1e-6)



def ballFunc(x, y):
    gameDisplay.blit(renderSurface, (x, y))

def textObjects(text, font):
    textSurface = font.render(text, True, blackC)
    return textSurface, textSurface.get_rect()

def messageDisplay(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    textSurf, textRect = textObjects(text, largeText)
    textRect.center = ((displayWidth / 2), (displayHeight / 2))
    gameDisplay.blit(textSurf, textRect)
    pygame.display.update()
    time.sleep(2)
    gameLoop()

def crash():
    messageDisplay('You crashed!')

def gameLoop():
    x = (displayWidth * 0.45)  # random x coordinate
    y = (displayHeight * 0.8)  # x is positive from left to right and y is positive from up to down.
    xChange = 0
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xChange = -20
                if event.key == pygame.K_RIGHT:
                    xChange = 20
            if event.type == pygame.KEYUP:
                # if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:   # not really needed
                xChange = 0
        x += xChange
        gameDisplay.fill(whiteC)
        ballFunc(x, y)
        if x > displayWidth - ballWidth or x < 0:
            crash()
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
    quit()

gameLoop()
pygame.quit()
quit()
