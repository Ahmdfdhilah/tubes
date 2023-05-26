import pygame
from settings import *

class DialogBox:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(RES)
        self.dialog_width = 800
        self.dialog_height = 200
        self.text_font = pygame.font.SysFont("georgia", 35)
        self.character_image_size = (250, 250)
        self.bg_img = pygame.image.load('textures/sky/sky.png')

    def draw_dialog_box(self, x, y, width, height, border_radius=0):
        rect = pygame.Rect(x, y, width, height)
        pygame.draw.rect(self.screen, WHITE, rect, border_radius=border_radius)
        pygame.draw.rect(self.screen, BLACK, rect, width=2, border_radius=border_radius)

    def draw_text(self, text, x, y, font_size):
        words = text.split()
        lines = []
        current_line = ""
        self.text_font = pygame.font.SysFont("georgia", font_size)
        for word in words:
            line_test = current_line + " " + word if current_line else word
            if self.text_font.size(line_test)[0] <= self.dialog_width - 40:
                current_line = line_test
            else:
                lines.append(current_line)
                current_line = word
        lines.append(current_line)
        
        line_height = self.text_font.size("Tg")[1]
        for i, line in enumerate(lines):
            text_surface = self.text_font.render(line, True, BLACK)
            self.screen.blit(text_surface, (x, y + i * line_height))

    def draw_character(self, image, x, y):
        character = pygame.image.load(image)
        character = pygame.transform.scale(character, self.character_image_size)
        self.screen.blit(character, (x, y))

    def show_dialog(self, text, character_image, character_name):
        self.screen.blit(pygame.transform.scale(self.bg_img, (WITDH, HEIGHT)), (0, 0))
        dialog_x = (WITDH - self.dialog_width) // 2
        dialog_y = (HEIGHT - self.dialog_height) // 2
        self.draw_dialog_box(dialog_x, dialog_y, self.dialog_width, self.dialog_height, border_radius=50)

        text_x = dialog_x + 20
        text_y = dialog_y + 20
        self.draw_text(text, text_x, text_y, 35)

        character_name_x = text_x
        character_name_y = text_y - 30
        character_name_width = self.text_font.size(character_name)[0] + 20
        character_name_height = 30
        self.draw_dialog_box(character_name_x, character_name_y, character_name_width, character_name_height, border_radius=10)
        self.draw_text(character_name, character_name_x + 10, character_name_y + 8, 16)

        character_x = dialog_x + self.dialog_width - 120
        character_y = dialog_y + self.dialog_height - 120
        self.draw_character(character_image, character_x, character_y)

        pygame.display.flip()

    def get_dialog(self, dialog):
        current_line = 0
        running = True

        while running:
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if current_line < len(dialog)-1:
                            current_line += 1
                        else:
                            running = False
            self.show_dialog(dialog[current_line]["text"], dialog[current_line]["character_image"], dialog[current_line]["chara"])