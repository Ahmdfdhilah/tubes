import pygame as pg
from settings import *

class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()
    # Sky Render
        self.sky_image = self.get_texture('textures/sky/sky.png', (WITDH, HALF_HEIGHT))
        self.sky_offset = 0

    def draw(self):
        self.draw_background()
        self.render_game_object()

    # Draw Background (sky and floor) Method
    def draw_background(self):
    # sky
        self.sky_offset = (self.sky_offset + 4.0 * self.game.player.rel) % WITDH
        self.screen.blit(self.sky_image, (-self.sky_offset, 0))
        self.screen.blit(self.sky_image, (-self.sky_offset + WITDH, 0))
    # floor
        pg.draw.rect(self.screen, FLOOR_COLOR, (0, HALF_HEIGHT, WITDH, HEIGHT))

    def render_game_object(self):
        list_objects = sorted(self.game.raycasting.object_to_render, key=lambda t : t[0], reverse=True)
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos)

    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)
    
    def load_wall_textures(self):
        return{
            1: self.get_texture("textures/walls/test.jpg"),
            # 2: self.get_texture("textures/walls/2.png")
        }

