#Version 1.0

## when we finish change the theme and make it a mouth thats eats food and avoids poison

import pygame, pygame.mixer
import sys

from utils import helpers
from utils import screens
from game.logic import gameLoop
from game.hungryMouth import hungryMouth




# pause = False

def main():
    pygame.init()
    pygame.mixer.init()

    displayWidth = 1000
    displayHeight = 690
    mouthWidth = 150  # adjust as fit

    gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
    pygame.display.set_caption("The Hungry Mouth")

    gameIcon = pygame.image.load(helpers.resource_path("assets/images/gameIcon.png"))
    pygame.display.set_icon(gameIcon)
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
    hungryMouthV = hungryMouth(gameDisplay)
    score = 0
    foodList = []
    GOSCount = [1]

    while True:
        events = pygame.event.get()
        keys = pygame.key.get_pressed()
        
        if state == "languageSelection":
            for event in events:
                if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                    sys.exit()
            selectedLang = ScreenObj.showLanguageSelection(events)
            if selectedLang:
                langData = helpers.loadLanguageData(selectedLang)
                state = "mainMenu"

        else:
            for event in events:
                if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                    state = "aggressiveQuit"
            if state == "mainMenu":
                result = ScreenObj.showMainMenu(langData, events)
                if result == 3:
                    ScreenObj.showAggressiveQuit(langData)
                elif result == 2:
                    state = "instructions"
                elif result == 1:
                    state = "play"
                elif result == 4:
                    state = "languageSelection"
                    selectedLang = None
                    langData = None


            elif state == "instructions":
                back = ScreenObj.showInstructionsScreen(langData, events)
                if back:
                    state = "mainMenu"

            elif state == "play":
                gameResult = gameLoop(gameDisplay, clock, langData, ScreenObj, hungryMouthV, score, foodList)
                if gameResult == "gameOver":
                    state = "gameOver"
                elif gameResult == "aggressiveQuit":
                    ScreenObj.showAggressiveQuit(langData)
                elif gameResult == "pause": ## still undeveloped code
                    return 420
            elif state == "gameOver":
                result = ScreenObj.showGameOverScreen(langData, events, GOSCount)
                if result == "playAgain":
                    score = 0
                    foodList = []
                    hungryMouthV.lives = 3
                    GOSCount[0] = 1
                    state = "play"
                elif result == "aggressiveQuit":
                    ScreenObj.showAggressiveQuit(langData)
            elif state == "aggressiveQuit":
                ScreenObj.showAggressiveQuit(langData)
        pygame.display.update()
        clock.tick(60)





if __name__ == "__main__":
    main() 





