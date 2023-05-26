import pygame
from settings import *

class DialogExample:
    def __init__(self, state):

        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)

        self.data_state = state

        self.text_animation_duration = 50
        self.text_font = pygame.font.SysFont("Arial", 24)
        self.text_color = self.BLACK

        self.current_character = "Character 1"
        self.current_dialog_index = 0
        self.current_dialog = self.data_state["dialog"][self.current_dialog_index]
        self.current_dialog_position = (50, 300)
        self.current_dialog_rect = pygame.Rect(self.current_dialog_position, (0, 0))
        self.is_text_animating = True
        self.text_animation_timer = 0
        self.text_index = 0

    def update(self):
        self.current_dialog_index += 1
        if self.current_dialog_index >= len(self.dialog[self.current_character]):
            if self.current_character == "Character 1":
                self.current_character = "Character 2"
            else:
                self.current_character = "Character 1"
            self.current_dialog_index = 0
        self.current_dialog = self.dialog[self.current_character][self.current_dialog_index]
        self.is_text_animating = True
        self.text_index = 0

        if self.is_text_animating:
                if self.text_index < len(self.current_dialog):
                    self.text_animation_timer += self.clock.get_time()
                    if self.text_animation_timer > self.text_animation_duration:
                        self.text_index += 1
                        self.text_animation_timer = 0
                else:
                    self.is_text_animating = False

        self.screen.fill(self.WHITE)

        if self.current_character == "Character 1":
            self.screen.blit(self.character1_image, (50, 50))
        else:
            self.screen.blit(self.character2_image, (self.WIDTH - 200, 50))
        self.current_dialog_rect.width = self.WIDTH - 100
        current_dialog_surface = self.text_font.render(self.current_dialog[:self.text_index], True, self.text_color)
        self.screen.blit(current_dialog_surface, self.current_dialog_position)
        pygame.draw.rect(self.screen, self.BLACK, self.current_dialog_rect, 2)

        pygame.display.flip()
        self.clock.tick(60)
obj = DialogExample
obj.update("start")







import pygame as pg
from settings import *
from main import *

pg.init()

screen = pg.display.set_mode(RES)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

character1_image = pg.image.load("textures/dialog/chara1.png")
character2_image = pg.image.load("textures/dialog/chara2.png")


dialog = {
        "Character 1": [
            "Hi there!",
            "How are you?",
            "What have you been up to?"
        ]
    ,
        "Character 2":
        [
            "Hey!",
            "I'm good, thanks. How about you?",
            "Not much, just hanging out."
        ]
    ,    "Character 1": [      
            "What have you been up to?"
        ]
    ,
        "Character 2":
        [
            "I'm good, thanks. How about you?",
            "Not much, just hanging out."
        ]
   
}

text_animation_duration = 50  
text_font = pg.font.SysFont("Arial", 24)
text_color = BLACK

current_character = "Character 1"
current_dialog_index = 0
current_character_index = 0

current_dialog = dialog[current_character][current_dialog_index]
current_dialog_position = (WITDH//3.2, HEIGHT//1.3)
current_dialog_rect = pg.Rect(current_dialog_position, (50, 50))
is_text_animating = True
text_animation_timer = 0
text_index = 0
bg_img = pg.image.load('textures\sky\sky.png')
clock = pg.time.Clock()
Dialog = True

while(Dialog == True):
    # print(pygame.event.get())
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            Dialog = False
        elif event.type == pg.MOUSEBUTTONUP:
            current_dialog_index += 1
            if current_dialog_index >= len(dialog[current_character]):
                
                if current_character == "Character 1":
                    current_character = "Character 2"
                else:
                    current_character = "Character 1"
                current_dialog_index = 0
            current_dialog = dialog[current_character][current_dialog_index]
            is_text_animating = True
            text_index = 0
    if is_text_animating:
        if text_index < len(current_dialog):
            text_animation_timer += clock.get_time()
            if text_animation_timer > text_animation_duration:
                text_index += 1
                text_animation_timer = 0
        else:
            is_text_animating = False
    
    screen.blit(pg.transform.scale(bg_img, (WITDH, HEIGHT)), (0,0))

    if current_character == "Character 1":
        screen.blit(character1_image, (50, 50))
    else:
        screen.blit(character2_image, (WITDH - 200, 50))

    current_dialog_rect.width = WITDH - 100
    current_dialog_surface = text_font.render(current_dialog[:text_index], True, text_color)
    screen.blit(current_dialog_surface, current_dialog_position)
    pg.draw.rect(screen, BLACK, current_dialog_rect, 2)
    
    pg.display.flip()
    
    clock.tick(60)
