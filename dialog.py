import pygame as pg
from settings import *
from main import *

pg.init()

# WITDH = WITDH
# HEIGHT = HEIGHT
# screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pg.display.set_caption("Dialog Example")
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
current_dialog = dialog[current_character][current_dialog_index]
current_dialog_position = (WITDH//3.2, HEIGHT//1.3)
current_dialog_rect = pg.Rect(current_dialog_position, (50, 50))
is_text_animating = True
text_animation_timer = 0
text_index = 0

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
    
    screen.fill(WHITE)
    
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
