#Version 1.0

## when we finish change the theme and make it a mouth thats eats food and avoids poison

import pygame, pygame.mixer
import time
import random
import sys

import utils.langSelection as langSelection
from utils import colors as color
from utils import helpers
import utils.langManager as langManager
from game.hungryMouth import hungryMouth
from game.food import food
from utils.screens import showGameOverScreen, showPauseScreen, showMainMenu, showInstructionsScreen


pygame.init()
pygame.mixer.init()

displayWidth = 1000
displayHeight = 690
mouthWidth = 150  # adjust as fit

# clock = pygame.time.Clock()

# ballImg = pygame.image.load(helpers.resource_path("250x250_img_1.png"))

gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("The Hungry Mouth")

gameIcon = pygame.image.load(helpers.resource_path("assets/images/gameIcon.png"))
pygame.display.set_icon(gameIcon)


# pause = False


def spawnFoodWave(gameDisplay, langText):
    foodList = []
    waveSize = random.choice([1,2,3])
    if waveSize ==1:
        poison =  random.choice([True, False])
        foodList.append(food(gameDisplay, poison, langText))
    elif waveSize ==2:
        poisonCount = random.choice([1,2])
        for i in range(2):
            isPoison = i < poisonCount
            foodList.append(food(gameDisplay,isPoison, langText))
    elif waveSize == 3:
        poisonCount = random.choice([2,3])
        for i in range(3):
            isPoison = i < poisonCount
            foodList.append(food(gameDisplay, isPoison, langText))
    usedRects = []
    for item in foodList:
        tries = 0
        while True:
            item.x = random.randint(50, gameDisplay.get_width() - item.width - 50)
            itemRect = pygame.Rect(item.x, item.y, item.width, item.height)
            # Check no overlap and at least 30px gap
            if all(abs(itemRect.x - r.x) > (item.width + 30) for r in usedRects):
                usedRects.append(itemRect)
                break
            tries += 1
            if tries > 30:
                # Couldn’t find a good spot after many tries, place anyway
                break
    return foodList


bgMusicPath = helpers.resource_path("assets/sounds/bg_music.mp3")
try:
    pygame.mixer.music.load(bgMusicPath)
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)
except Exception as e:
    print(f"[Warning] Failed to load background music: {e}")
langSelectionScreen = langSelection.langSelectionScreen(gameDisplay)
running = True
clock = pygame.time.Clock()
selectedLang = None
hungryMouthV = hungryMouth(gameDisplay)
score = 0
foodList = []
helpers.myfunc()
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            running = False
    keys = pygame.key.get_pressed()
    if selectedLang is None:
        selected = langSelectionScreen.showMenu(events)
        if selected is not None:
            selectedLang = selected
        pygame.display.update()
        clock.tick(60)
    else:
        langText = langManager.getLangContent(selectedLang)
        menuChoice = showMainMenu(gameDisplay, langText, events)
        try:
            gameOverSound = pygame.mixer.Sound(helpers.resource_path(langText.get("sfxGameOver", "assets/sounds/sfx_en_game_over.wav")))
        except Exception as e:
            print(f"[Warning] 22 Failed to load gameOverSound: {e}")
            gameOverSound = None
        if menuChoice == "instructions":
            showInstructionsScreen(gameDisplay, langText)
        elif menuChoice == "quit":
            pygame.quit()
            sys.exit()
        if keys[pygame.K_p]:
            pauseResult = showPauseScreen(gameDisplay, langText)
            if pauseResult == "quit":
                running = False
                break
        gameDisplay.fill(color.white)
        hungryMouthV.drawMouth(gameDisplay)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            hungryMouthV.moveLeft()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            hungryMouthV.moveRight()
        hungryMouthV.updatePoisonTimer()
        hungryMouthV.drawMouth(gameDisplay)
        if len(foodList) == 0:
            foodList = spawnFoodWave(gameDisplay, langText)
        if hungryMouthV.lives <= 0:
            result = showGameOverScreen(gameDisplay, langText)
            if result == "restart":
                selectedLang = None
                hungryMouthV = hungryMouth(gameDisplay)
                score = 0
                foodList.clear()
                continue

        for foodItem in foodList[:]:  # Copy to safely remove while iterating
            foodItem.updatePos()
            
            if foodItem.getRect().colliderect(hungryMouthV.getRect()):
                if foodItem.isPoison:
                    sfxPath = foodItem.getSfxPath()
                    if sfxPath:
                        try:
                            pygame.mixer.Sound(helpers.resource_path(sfxPath)).play()
                        except Exception as e:
                            print(f"[Warning] Failed to play poison sound: {e}")
                    hungryMouthV.activatePoisonEffect()
                    hungryMouthV.lives -= 1
                else:
                    score += 1
                foodList.remove(foodItem)
                continue  # Skip drawing if removed due to collision
 
            if foodItem.isOffScreen(gameDisplay):
                foodList.remove(foodItem)
                continue  # Skip drawing if removed for being off-screen

            foodItem.drawFood(gameDisplay)


    pygame.display.update()
    clock.tick(60)



# gameOverSound.play()
# result = showGameOverScreen(gameDisplay, langText)


        # running = False
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




# def ballFunc(x, y):
#     gameDisplay.blit(ballImg, (x, y))







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


