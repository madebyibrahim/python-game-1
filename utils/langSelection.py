# plan: working = true variable then break , show 2 buttoms, click or keypress to select, 
from utils import colors as color
from utils import helpers
import pygame

def langSelection(gameDisplay):
    (displayWidth, displayHeight) = gameDisplay.get_size()
    print(displayWidth)
    print(displayHeight)

   
    arTitle = "العربية (A)"
    enTitle = "English (E)"
    arChooseText = 'إختر اللغة'
    enChooseText = "Choose Language"
    enFlag = pygame.image.load(helpers.resource_path("assets/images/usa_flag.png"))
    arFlag = pygame.image.load(helpers.resouce_path("assets/images/lebanon_flag.png"))
 
    gameDisplay.fill(color.white)
