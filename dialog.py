import pygame 
from settings import *

pygame.init()

screen = pygame.display.set_mode(RES)

# Lebar dan tinggi kotak dialog
DIALOG_WIDTH = 800
DIALOG_HEIGHT = 200

# Warna yang digunakan
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# Menggambar kotak dialog dengan border radius
def draw_dialog_box(x, y, width, height, border_radius=0):
    rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, WHITE, rect, border_radius=border_radius)
    pygame.draw.rect(screen, BLACK, rect, width=2, border_radius=border_radius)

# Menggambar teks pada kotak dialog
def draw_text(text, x, y, font_size):
    text_font = pygame.font.SysFont("Arial", font_size)
    words = text.split()
    lines = []
    current_line = ""
    
    for word in words:
        line_test = current_line + " " + word if current_line else word
        if text_font.size(line_test)[0] <= DIALOG_WIDTH - 40:
            current_line = line_test
        else:
            lines.append(current_line)
            current_line = word
    lines.append(current_line)
    
    line_height = text_font.size("Tg")[1]  # Menentukan tinggi setiap baris
    for i, line in enumerate(lines):
        text_surface = text_font.render(line, True, BLACK)
        screen.blit(text_surface, (x, y + i * line_height))


# Menggambar gambar karakter
def draw_character(image, x, y):
    DEFAULT_IMAGE_SIZE = (250, 250)
    character = pygame.image.load(image)
    character = pygame.transform.scale(character, DEFAULT_IMAGE_SIZE)
    screen.blit(character, (x, y))

def show_dialog(text, character_image, character_name):
    bg_img = pygame.image.load('textures/sky/sky.png')
    screen.blit(pygame.transform.scale(bg_img, (WITDH, HEIGHT)), (0, 0))
    text_font = pygame.font.SysFont("Arial", 20)
    # Menggambar kotak dialog di tengah layar
    dialog_x = (WITDH - DIALOG_WIDTH) // 2
    dialog_y = (HEIGHT - DIALOG_HEIGHT) // 2
    draw_dialog_box(dialog_x, dialog_y, DIALOG_WIDTH, DIALOG_HEIGHT, border_radius=10)

    # Menggambar teks pada kotak dialog
    text_x = dialog_x + 20
    text_y = dialog_y + 20
    draw_text(text, text_x, text_y, 40)

    # Menggambar nama karakter dalam kotak karakter yang sedang berbicara
    character_name_x = text_x
    character_name_y = text_y - 30  # Meletakkan kotak nama di atas teks dialog
    character_name_width = text_font.size(character_name)[0] + 20  # Menyesuaikan lebar kotak dengan panjang teks nama karakter
    character_name_height = 30
    draw_dialog_box(character_name_x, character_name_y, character_name_width, character_name_height, border_radius=5)
    draw_text(character_name, character_name_x + 10, character_name_y + 8, 16)

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
            show_dialog(dialog[current_line]["text"], dialog[current_line]["character_image"], dialog[current_line]["chara"])
