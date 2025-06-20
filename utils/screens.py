import pygame
import sys
from utils import colors as color
from utils import helpers

class Screen:
    #done
    def __init__(self, gameDisplayy):
        self.gameDisplay = gameDisplayy
        self.displayWidth, self.displayHeight = gameDisplayy.get_size()
        # Load fonts once
        self.enFont = helpers.loadLanguageData("en").get("fontPath")
        self.arFont = helpers.loadLanguageData("ar").get("fontPath")
        # Preprocess text once
        self.arTitle = helpers.makeArabic("العربية ﴿A﴾")
        self.enTitle = "English (E)"
        self.arChooseText = helpers.makeArabic('إختر اللغة')
        self.enChooseText = "Choose Language"
        # Load images once
        self.enFlag = helpers.resource_path("assets/images/usa_flag.png")
        self.arFlag = helpers.resource_path("assets/images/lebanon_flag.png")
        self.selectedLang = None
    
    # done
    def showLanguageSelection(self, events):
        self.selectedLang = None
        gameDisplay = self.gameDisplay
        gameDisplay.fill(color.white)
        helpers.messageDisplay(gameDisplay,self.enChooseText,95, self.enFont, color.black, -1, self.displayHeight/10)
        helpers.messageDisplay(gameDisplay,self.arChooseText,115, self.arFont, color.black, -1, self.displayHeight/4 + 40)
        if (helpers.button(gameDisplay, "", self.displayWidth/2 - 125, self.displayHeight/2  , 250, 70, color.gray, color.lightGray, events)):
            self.selectedLang = "en"
        if helpers.button(gameDisplay, "", self.displayWidth/2 - 125, self.displayHeight/2 + 95 , 250, 70, color.gray, color.lightGray, events):
            self.selectedLang = "ar"    
        helpers.messageDisplay(gameDisplay,self.arTitle,55, self.arFont, color.red, -1, self.displayHeight/2 + 130)
        helpers.messageDisplay(gameDisplay,self.enTitle,40, self.enFont, color.red, -1, self.displayHeight/2 + 30)
        helpers.showImage(gameDisplay, self.arFlag, (self.displayWidth/2 + 160), (self.displayHeight/2 + 85), (135,90))
        helpers.showImage(gameDisplay, self.enFlag, (self.displayWidth/2 - 300), (self.displayHeight/2), (140,70))        
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e or event.key == pygame.K_KP1:  # E key for English
                    self.selectedLang = "en"
                elif event.key == pygame.K_a or event.key == pygame.K_KP2:  # A key for Arabic
                    self.selectedLang = "ar"
        return self.selectedLang

    # done
    def showAggressiveQuit(self, langData):
        sfxGoodBye = pygame.mixer.Sound(helpers.resource_path(langData.get("sfxGoodBye")))
        while pygame.mixer.get_busy():  # Loop while any sound is playing
            pygame.time.delay(100)  # Short delay to reduce CPU usage
        sfxGoodBye.play()
        while pygame.mixer.get_busy():  # Loop while any sound is playing
            pygame.time.delay(100)
        sys.exit()

    def showGameOverScreen(self, langData, events, GOSCount):
        if GOSCount[0] >0:
            GOSCount[0] -= 1
            gameOverSound = pygame.mixer.Sound(helpers.resource_path(langData.get("sfxGameOver")))
            while pygame.mixer.get_busy():  # Loop while any sound is playing
                pygame.time.delay(200)  # Short delay to reduce CPU usage
            gameOverSound.play()
            
        self.gameDisplay.fill(color.white)
        if helpers.button(self.gameDisplay,"", self.displayWidth/2 - 150, self.displayHeight/2, 300, 80, color.gray, color.lightGray, events):
            return "playAgain"
        if helpers.button(self.gameDisplay, "", self.displayWidth/2 - 150, self.displayHeight/2 + 100, 300, 80, color.gray, color.lightGray, events):
            return "aggressiveQuit"

        helpers.messageDisplay(self.gameDisplay, langData.get("gameOverMessage"), 100, langData.get("fontPath"), color.black, -1,self.displayHeight/4,langData.get("language"))
        helpers.messageDisplay(self.gameDisplay, langData.get("playTitle"), 50, langData.get("fontPath"), color.red, self.displayWidth/2 ,self.displayHeight/2 + 40,langData.get("language"))
        helpers.messageDisplay(self.gameDisplay, langData.get("quitTitle"), 50, langData.get("fontPath"), color.red, self.displayWidth/2 ,self.displayHeight/2 + 140, langData.get("language"))
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_KP1:
                return "playAgain"
            if event.type == pygame.KEYDOWN and event.key == pygame.K_KP2:
                return "aggressiveQuit"


    # done
    def showPauseScreen(self, langData, events):
        self.gameDisplay.fill(color.white)
        # resume
        if helpers.button(self.gameDisplay, "", self.displayWidth/2 - 350, self.displayHeight/2 + 100 , 280, 80, color.gray, color.lightGray, events):
            return 2
        #  quit
        if helpers.button(self.gameDisplay, "", self.displayWidth/2 + 100, self.displayHeight/2 + 100 , 280, 80, color.gray, color.lightGray, events):
            return 1
        helpers.messageDisplay(self.gameDisplay,langData.get("gameTitle"),100, langData.get("fontPath"), color.black, -1, 100, langData.get("language"))
        helpers.messageDisplay(self.gameDisplay,langData.get("resumeButton"),60, langData.get("fontPath"), color.red, self.displayWidth/2 - 210, self.displayHeight/2 + 140, langData.get("language"))
        helpers.messageDisplay(self.gameDisplay,langData.get("quitTitle"),60, langData.get("fontPath"), color.red, self.displayWidth/2 + 240, self.displayHeight/2 + 140, langData.get("language"))



    # done
    def showMainMenu(self, langData, events):
        self.gameDisplay.fill(color.white)
        # events = pygame.event.get()
        #display text boxes
        if helpers.button(self.gameDisplay, "", self.displayWidth/2 - 175, self.displayHeight/2  , 350, 90, color.gray, color.lightGray, events):
            return 1 # play
        if helpers.button(self.gameDisplay, "", self.displayWidth/2 - 175, self.displayHeight/2 + 100 , 350, 90, color.gray, color.lightGray, events):
            return 2 # instructions
        if helpers.button(self.gameDisplay, "", self.displayWidth/2 - 175, self.displayHeight/2 + 200 , 350, 90, color.gray, color.lightGray, events):
            return 3 # quit
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                    return 4 # return back to language selection
            if event.type == pygame.KEYDOWN and event.key == pygame.K_KP1:
                return 1
            if event.type == pygame.KEYDOWN and event.key == pygame.K_KP2:
                return 2
            if event.type == pygame.KEYDOWN and event.key == pygame.K_KP3:
                return 3
        # Display the text boxes first and then the text
        helpers.messageDisplay(self.gameDisplay,langData.get("gameTitle"),100, langData.get("fontPath"), color.black, -1, 100, langData.get("language"))
        helpers.messageDisplay(self.gameDisplay,langData.get("playTitle"),60, langData.get("fontPath"), color.red, -1, self.displayHeight/2 + 45, langData.get("language"))
        helpers.messageDisplay(self.gameDisplay,langData.get("instructionsTitle"),60, langData.get("fontPath"), color.red, -1, self.displayHeight/2 + 145, langData.get("language"))
        helpers.messageDisplay(self.gameDisplay,langData.get("quitTitle"),60, langData.get("fontPath"), color.red, -1, self.displayHeight/2 + 245, langData.get("language"))
        return -1        

    # done
    def showInstructionsScreen(self, langData, events):
       
        self.gameDisplay.fill(color.white)

        helpers.messageDisplay(self.gameDisplay,langData.get("instructionsTitle"),100, langData.get("fontPath"), color.black, -1, 100, langData.get("language"))
        helpers.messageDisplay(self.gameDisplay,langData.get("instructionsD1"),30, langData.get("fontPath"), color.red, -1, self.displayHeight/2 - 100, langData.get("language"))
        helpers.messageDisplay(self.gameDisplay,langData.get("instructionsD2"),30, langData.get("fontPath"), color.red, -1, self.displayHeight/2 - 50, langData.get("language"))
        helpers.messageDisplay(self.gameDisplay,langData.get("instructionsD3"),30, langData.get("fontPath"), color.red, -1, self.displayHeight/2 , langData.get("language"))
        helpers.messageDisplay(self.gameDisplay,langData.get("instructionsD4"),30, langData.get("fontPath"), color.red, -1, self.displayHeight/2 + 50, langData.get("language"))
        helpers.messageDisplay(self.gameDisplay,langData.get("instructionsD5"),30, langData.get("fontPath"), color.red, -1, self.displayHeight/2 + 100, langData.get("language"))
    
        if helpers.button(self.gameDisplay, "", self.displayWidth/2 + 100, self.displayHeight/2 + 200 , 250, 70, color.gray, color.lightGray, events):
            return True
        helpers.messageDisplay(self.gameDisplay,langData.get("backButton"),50, langData.get("fontPath"), color.red, self.displayWidth/2 + 225, self.displayHeight/2 + 232, langData.get("language"))

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    return True


