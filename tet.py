import pygame.font

# Mendapatkan daftar font yang tersedia
fonts = pygame.font.get_fonts()

# Menampilkan daftar font
for font in fonts:
    print(font)
