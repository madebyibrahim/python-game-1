from utils import colors as color
from utils import helpers
import pygame



class langSelectionScreen:
    def __init__(self, gameDisplayy):
        self.gameDisplay = gameDisplayy
        self.displayWidth, self.displayHeight = gameDisplayy.get_size()
        # Load fonts once
        self.enFont = "assets/fonts/Arial.ttf"
        self.arFont = "assets/fonts/Traditional_Arabic.ttf"
        # Preprocess text once
        self.arTitle = helpers.makeArabic("العربية ﴿A﴾")
        self.enTitle = "English (E)"
        self.arChooseText = helpers.makeArabic('إختر اللغة')
        self.enChooseText = "Choose Language"
        # Load images once
        self.enFlag = helpers.resource_path("assets/images/usa_flag.png")
        self.arFlag = helpers.resource_path("assets/images/lebanon_flag.png")
        self.selectedLang = None    
    def chooseLang(self, lang):
        self.selectedLang = lang
        return self.selectedLang
    def showMenu(self, events):
        gameDisplay = self.gameDisplay
        gameDisplay.fill(color.white)
        
        helpers.messageDisplay(gameDisplay,self.enChooseText,95, self.enFont, color.black, -1, self.displayHeight/10)
        helpers.messageDisplay(gameDisplay,self.arChooseText,115, self.arFont, color.black, -1, self.displayHeight/4 + 40)

        helpers.button(gameDisplay, "", self.displayWidth/2 - 125, self.displayHeight/2  , 250, 70, color.gray, color.lightGray, events, lambda: self.chooseLang("en"))
        helpers.button(gameDisplay, "", self.displayWidth/2 - 125, self.displayHeight/2 + 95 , 250, 70, color.gray, color.lightGray, events, lambda: self.chooseLang("ar"))
        
        helpers.messageDisplay(gameDisplay,self.arTitle,55, self.arFont, color.red, -1, self.displayHeight/2 + 130)
        helpers.messageDisplay(gameDisplay,self.enTitle,40, self.enFont, color.red, -1, self.displayHeight/2 + 30)
        
        helpers.showImage(gameDisplay, self.arFlag, (self.displayWidth/2 + 160), (self.displayHeight/2 + 80), (135,90))
        helpers.showImage(gameDisplay, self.enFlag, (self.displayWidth/2 - 300), (self.displayHeight/2), (140,70))
        
        # helpers.button(gameDisplay, "", displayWidth/2 - 300, displayHeight/2 + 120, 140, 60, color.gray, color.lightGray, lambda: chooseLang("en"))
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:  # E key for English
                    self.selectedLang = "en"
                elif event.key == pygame.K_a:  # A key for Arabic
                    self.selectedLang = "ar"
        return self.selectedLang

