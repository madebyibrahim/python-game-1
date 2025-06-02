import pygame
pygame.init()

blackC = (0,0,0)
whiteC = (255,255,255)
redC = (255,0,0)
greenC = (0,255,0)
blueC = (0,0,255)
tempC = (169,43,97)

gameDisplay = pygame.display.set_mode((600,800))
gameDisplay.fill(whiteC)

pixAr = pygame.PixelArray(gameDisplay)
# try each commented out one by one.
# pixAr[10][20] = greenC
# pygame.draw.line(gameDisplay,blueC, (100,200), (300,450), 5)
# pygame.draw.rect(gameDisplay, redC, (400,400,50,25))
# pygame.draw.circle(gameDisplay, greenC, (150,150),75)
# pygame.draw.polygon(gameDisplay, tempC, ((25,75),(76,125),(250,375),(400,25),(60,540)))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()