import pygame
import sys
from utils import colors as color
from utils import helpers

class Screen:
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
    
    def showLanguageSelection(self, events):
        gameDisplay = self.gameDisplay
        gameDisplay.fill(color.white)
        helpers.messageDisplay(gameDisplay,self.enChooseText,95, self.enFont, color.black, -1, self.displayHeight/10)
        helpers.messageDisplay(gameDisplay,self.arChooseText,115, self.arFont, color.black, -1, self.displayHeight/4 + 40)
        if helpers.button(gameDisplay, "", self.displayWidth/2 - 125, self.displayHeight/2  , 250, 70, color.gray, color.lightGray, events):
            self.selectedLang = "en"
        if helpers.button(gameDisplay, "", self.displayWidth/2 - 125, self.displayHeight/2 + 95 , 250, 70, color.gray, color.lightGray, events):
            self.selectedLang = "ar"    
        helpers.messageDisplay(gameDisplay,self.arTitle,55, self.arFont, color.red, -1, self.displayHeight/2 + 130)
        helpers.messageDisplay(gameDisplay,self.enTitle,40, self.enFont, color.red, -1, self.displayHeight/2 + 30)
        helpers.showImage(gameDisplay, self.arFlag, (self.displayWidth/2 + 160), (self.displayHeight/2 + 80), (135,90))
        helpers.showImage(gameDisplay, self.enFlag, (self.displayWidth/2 - 300), (self.displayHeight/2), (140,70))        
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:  # E key for English
                    self.selectedLang = "en"
                elif event.key == pygame.K_a:  # A key for Arabic
                    self.selectedLang = "ar"
        return self.selectedLang



def showGameOverScreen(gameDisplay, langText):
    titleFont = pygame.font.Font(None, 80)
    buttonFont = pygame.font.Font(None, 50)
    gameOverText = titleFont.render(langText["gameOverMessage"], True, color.red)
    playAgainText = buttonFont.render(langText["restartButton"], True, color.black)
    quitText = buttonFont.render(langText["quitButton"], True, color.black)
    playAgainRect = pygame.Rect(300, 400, 180, 60)
    quitRect = pygame.Rect(550, 400, 180, 60)

    while True:
        gameDisplay.fill(color.white)
        gameDisplay.blit(gameOverText, (300, 200))

        pygame.draw.rect(gameDisplay, color.gray, playAgainRect)
        pygame.draw.rect(gameDisplay, color.gray, quitRect)

        gameDisplay.blit(playAgainText, (playAgainRect.x + 20, playAgainRect.y + 10))
        gameDisplay.blit(quitText, (quitRect.x + 40, quitRect.y + 10))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                if playAgainRect.collidepoint(mousePos):
                    return "restart"
                elif quitRect.collidepoint(mousePos):
                    pygame.quit()
                    exit()


def showPauseScreen(gameDisplay, langText):
    fontBig = pygame.font.Font(None, 80)
    fontSmall = pygame.font.Font(None, 50)

    pauseText = fontBig.render(langText.get("pauseMessage", "PAUSED"), True, color.black)
    resumeText = fontSmall.render(langText.get("resumeButton", "Resume"), True, color.black)
    quitText = fontSmall.render(langText.get("quitButton", "Quit"), True, color.black)

    resumeRect = pygame.Rect(300, 400, 180, 60)
    quitRect = pygame.Rect(550, 400, 180, 60)

    while True:
        gameDisplay.fill(color.white)
        gameDisplay.blit(pauseText, (300, 200))

        pygame.draw.rect(gameDisplay, color.gray, resumeRect)
        pygame.draw.rect(gameDisplay, color.gray, quitRect)

        gameDisplay.blit(resumeText, (resumeRect.x + 20, resumeRect.y + 10))
        gameDisplay.blit(quitText, (quitRect.x + 40, quitRect.y + 10))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                if resumeRect.collidepoint(mousePos):
                    return "resume"
                elif quitRect.collidepoint(mousePos):
                    return "quit"

def showMainMenu(gameDisplay, langText, events):

    fontTitle = pygame.font.Font(None, 90)
    fontBtn = pygame.font.Font(None, 50)

    title = fontTitle.render(langText.get("mainTitle", "The Hungry Mouth"), True, color.black)
    playText = fontBtn.render(langText.get("playButton", "Play"), True, color.black)
    instText = fontBtn.render(langText.get("instructionsButton", "Instructions"), True, color.black)
    quitText = fontBtn.render(langText.get("quitButton", "Quit"), True, color.black)

    playRect = helpers.button(gameDisplay, "",320, 320,180,60,color.gray, color.lightGray, events)
    instRect = pygame.Rect(320, 380, 180, 60)
    quitRect = pygame.Rect(320, 460, 180, 60)

    while True:
        gameDisplay.fill(color.white)
        gameDisplay.blit(title, (200, 150))

        # pygame.draw.rect(gameDisplay, color.gray, playRect)
        pygame.draw.rect(gameDisplay, color.gray, instRect)
        pygame.draw.rect(gameDisplay, color.gray, quitRect)

        # gameDisplay.blit(playText, (playRect.x + 30, playRect.y + 10))
        gameDisplay.blit(instText, (instRect.x + 5, instRect.y + 10))
        gameDisplay.blit(quitText, (quitRect.x + 30, quitRect.y + 10))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     pos = pygame.mouse.get_pos()
            #     if playRect.collidepoint(pos):
            #         return "play"
            #     elif instRect.collidepoint(pos):
            #         return "instructions"
            #     elif quitRect.collidepoint(pos):
            #         return "quit"


def showInstructionsScreen(gameDisplay, langText):
    fontTitle = pygame.font.Font(None, 70)
    fontBody = pygame.font.Font(None, 40)

    instructions = [
        langText.get("instr1", "Eat only healthy food!"),
        langText.get("instr2", "Avoid poisons to survive."),
        langText.get("instr3", "Use ← → arrow keys to move."),
        langText.get("instr4", "Press P to pause."),
        langText.get("instr5", "You have 3 lives!")
    ]

    backText = fontBody.render(langText.get("backButton", "Back"), True, color.black)
    backRect = pygame.Rect(320, 500, 180, 60)

    while True:
        gameDisplay.fill(color.white)
        title = fontTitle.render(langText.get("instructionsTitle", "Instructions"), True, color.black)
        gameDisplay.blit(title, (250, 100))

        for i, line in enumerate(instructions):
            text = fontBody.render(line, True, color.black)
            gameDisplay.blit(text, (100, 180 + i * 50))

        pygame.draw.rect(gameDisplay, color.gray, backRect)
        gameDisplay.blit(backText, (backRect.x + 50, backRect.y + 10))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if backRect.collidepoint(pos):
                    return

