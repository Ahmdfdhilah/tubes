import pygame 
from settings import *

pygame.init()

screen = pygame.display.set_mode(RES)

# Lebar dan tinggi kotak dialog
DIALOG_WIDTH = 400
DIALOG_HEIGHT = 200

# Warna yang digunakan
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# Menggambar kotak dialog
def draw_dialog_box(x, y, width, height):
    pygame.draw.rect(screen, WHITE, (x, y, width, height), 0)
    pygame.draw.rect(screen, BLACK, (x, y, width, height), 2)

# Menggambar teks pada kotak dialog
def draw_text(text, x, y, font_size):
    text_font = pygame.font.SysFont("Arial", font_size)
    text_surface = text_font.render(text, True, BLACK)
    screen.blit(text_surface, (x, y))

# Menggambar gambar karakter
def draw_character(image, x, y):
    DEFAULT_IMAGE_SIZE = (100, 100)
    character = pygame.image.load(image)
    character = pygame.transform.scale(character, DEFAULT_IMAGE_SIZE)
    screen.blit(character, (x, y))

def show_dialog(text, character_image):
    bg_img = pygame.image.load('textures\sky\sky.png')
    screen.blit(pygame.transform.scale(bg_img, (WITDH, HEIGHT)), (0,0))
    
    # Menggambar kotak dialog di tengah layar
    dialog_x = (WITDH - DIALOG_WIDTH) // 2
    dialog_y = (HEIGHT - DIALOG_HEIGHT) // 2
    draw_dialog_box(dialog_x, dialog_y, DIALOG_WIDTH, DIALOG_HEIGHT)

    # Menggambar teks pada kotak dialog
    text_x = dialog_x + 20
    text_y = dialog_y + 20
    draw_text(text, text_x, text_y, 20)

    # Menggambar gambar karakter di sebelah kanan kotak dialog
    character_x = dialog_x + DIALOG_WIDTH - 120
    character_y = dialog_y + DIALOG_HEIGHT - 120
    draw_character(character_image, character_x, character_y)

    pygame.display.flip()


bg_img = pygame.image.load('textures\sky\sky.png')

def get_dialog(dialog):
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
            show_dialog(dialog[current_line]["text"], dialog[current_line]["character_image"]) 
