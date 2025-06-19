#Version 1.0

## when we finish change the theme and make it a mouth thats eats food and avoids poison

import pygame, pygame.mixer
import time
import random
import sys

from utils import helpers
from utils import screens
from game.logic import gameLoop

pygame.init()
pygame.mixer.init()

displayWidth = 1000
displayHeight = 690
mouthWidth = 150  # adjust as fit

gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("The Hungry Mouth")

gameIcon = pygame.image.load(helpers.resource_path("assets/images/gameIcon.png"))
pygame.display.set_icon(gameIcon)


# pause = False

def main():
    ScreenObj = screens.Screen(gameDisplay)
    clock = pygame.time.Clock()
    selectedLang = None
    state = "languageSelection"
    langData = None
    bgMusicPath = helpers.resource_path("assets/sounds/bg_music.mp3")
    try:
        pygame.mixer.music.load(bgMusicPath)
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)
    except Exception as e:
        print(f"[Warning] Failed to load background music: {e}")


    while True:
        events = pygame.event.get()
        keys = pygame.key.get_pressed()
        
        if state == "languageSelection":
            for event in events:
                if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    sys.exit()
            selectedLang = ScreenObj.showLanguageSelection(events)
            if selectedLang:
                langData = helpers.loadLanguageData(selectedLang)
                state = "mainMenu"

        else:
            for event in events:
                if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    state = "aggressiveQuit"
            if state == "mainMenu":
                result = ScreenObj.showMainMenu(langData, events)
                if result == 3:
                    ScreenObj.showAggressiveQuit(langData)
                elif result == 2:
                    state = "instructions"
                elif result == 1:
                    state = "play"

            elif state == "instructions":
                back = ScreenObj.showInstructionsScreen(langData, events)
                if back:
                    state = "mainMenu"

            elif state == "play":
                gameResult = gameLoop(gameDisplay, clock, langData, events, keys, ScreenObj)
                if gameResult == "gameOver":
                    state = "gameOver"

            elif state == "gameOver":
                result = ScreenObj.showGameOverScreen(langData, events)
                if result == "playAgain":
                    state = "play"
                elif result == "quit":
                    ScreenObj.showAggressiveQuit(langData)
            elif state == "aggressiveQuit":
                ScreenObj.showAggressiveQuit(langData)
        pygame.display.update()
        clock.tick(60)





if __name__ == "__main__":
    main() 





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



