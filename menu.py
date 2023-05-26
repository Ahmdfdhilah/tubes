import pygame
import sys
import textwrap
from button import Button
from subprocess import Popen

# from main import *

class Menu:
    def __init__(self):
        pygame.init()
        self.SCREEN = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Menu")
        self.BG = pygame.image.load("assets/Background.png")
        self.font = pygame.font.Font("assets/font.ttf", 45)

    def play(self):  
        Popen(["python", "main.py"])    
    
    def options(self):
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

            self.SCREEN.fill("white")

            # Long string
            text = "Game ini berlatar di sebuah bunker dimana bumi mengalami kehancuran dikarenakan munculnya monster yang diciptakan untuk mendominasi bumi"

            # Calculate the maximum width and height based on the resolution
            max_width = 0.8 * self.SCREEN.get_width()  # 80% of the screen width
            max_height = 0.8 * self.SCREEN.get_height()  # 80% of the screen height

            # Split the long string into multiple lines to fit within the maximum width and height
            lines = textwrap.wrap(text, width=50)

            # Render each line of the text
            for i, line in enumerate(lines):
                line_text = self.font.render(line, True, "Black")

                # Adjust font size if the text exceeds the maximum width or height
                if line_text.get_width() > max_width:
                    line_text = pygame.transform.scale(line_text, (int(max_width), line_text.get_height()))
                if line_text.get_height() > max_height:
                    line_text = pygame.transform.scale(line_text, (line_text.get_width(), int(max_height)))

                line_rect = line_text.get_rect(center=(self.SCREEN.get_width() // 2, self.SCREEN.get_height() // 2 + i * 50))
                self.SCREEN.blit(line_text, line_rect)

            OPTIONS_BACK = Button(image=None, pos=(640, 600),
                                text_input="BACK", font=self.font, base_color="Black", hovering_color="Green")

            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(self.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        self.main_menu()

            pygame.display.update()

       
    def main_menu(self):
        while True:
            self.SCREEN.blit(self.BG, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = self.font.render("MAIN MENU", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

            PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                                text_input="PLAY", font=self.font, base_color="#d7fcd4", hovering_color="White")
            OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                                text_input="ABOUT", font=self.font, base_color="#d7fcd4", hovering_color="White")
            QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                                text_input="QUIT", font=self.font, base_color="#d7fcd4", hovering_color="White")

            self.SCREEN.blit(MENU_TEXT, MENU_RECT)

            for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.SCREEN)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.play()
                    if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.options()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()

menu = Menu()
menu.main_menu()