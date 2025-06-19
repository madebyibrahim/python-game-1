import pygame
from game.food import food
from utils import colors as color
from utils import helpers
import random




def gameLoop(gameDisplay, clock, langData, ScreenObj, hungryMouthV, score, foodList):
    running = True
    while running:
        # Move and draw
        events = pygame.event.get()
        keys = pygame.key.get_pressed()
        for event in events:
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                return "quit"
        gameDisplay.fill(color.white)
        # hungryMouthV.drawMouth(gameDisplay)
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            hungryMouthV.moveLeft()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            hungryMouthV.moveRight()
        hungryMouthV.updatePoisonTimer()
        hungryMouthV.drawMouth(gameDisplay)
        if len(foodList) == 0:
            foodList = spawnFoodWave(gameDisplay, langData, foodList)

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

        if hungryMouthV.lives <= 0:
            return "gameOver"

        # # UI text
        # font = pygame.font.Font(langData.get("fontPath"), 28)
        # helpers.messageDisplay(gameDisplay, f"{langData.get('scoreText')}: {score}", 28, langData.get("fontPath"), color.black, 20, 20)
        # helpers.messageDisplay(gameDisplay, f"{langData.get('livesText')}: {hungryMouthV.lives}", 28, langData.get("fontPath"), color.red, 20, 60)

        pygame.display.update()
        clock.tick(60)


def spawnFoodWave(gameDisplay, langData, foodList):    
    waveSize = random.choice([1,2,3])
    if waveSize ==1:
        poison =  random.choice([True, False])
        foodList.append(food(gameDisplay, poison, langData))
    elif waveSize ==2:
        poisonCount = random.choice([1,2])
        for i in range(2):
            isPoison = i < poisonCount
            foodList.append(food(gameDisplay,isPoison, langData))
    elif waveSize == 3:
        poisonCount = random.choice([2,3])
        for i in range(3):
            isPoison = i < poisonCount
            foodList.append(food(gameDisplay, isPoison, langData))
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

