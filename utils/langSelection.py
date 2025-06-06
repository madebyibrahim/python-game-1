# plan: working = true variable then break , show 2 buttoms, click or keypress to select, 
from utils import colors as color
from utils import helpers
import pygame



def langSelection(gameDisplay):
    (displayWidth, displayHeight) = gameDisplay.get_size()
    print(displayWidth)
    print(displayHeight)
    enFont = "assets/fonts/Arial.ttf"
    arFont = "assets/fonts/Traditional_Arabic.ttf"
    arTitle = helpers.makeArabic("العربية ﴿A﴾")
    enTitle = "English (E)"
    arChooseText = helpers.makeArabic('إختر اللغة')
    enChooseText = "Choose Language"
    enFlag = pygame.image.load(helpers.resource_path("assets/images/usa_flag.png"))
    arFlag = pygame.image.load(helpers.resource_path("assets/images/lebanon_flag.png"))
 
    gameDisplay.fill(color.white)
    helpers.messageDisplay(gameDisplay,arTitle,115, arFont, color.red, -1, displayHeight/4)
    helpers.messageDisplay(gameDisplay,enTitle,95, enFont, color.red, -1, 3*displayHeight/4)