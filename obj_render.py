import pygame as pg
from settings import *

class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()
    
        self.digit_size = 50
        self.digit_img = [self.get_texture(f'textures/digit/{i}.png', [self.digit_size] * 2)
                        for i in range(11)]
        self.digit = dict(zip(map(str, range(11)), self.digit_img))

        self.hud_face = self.get_texture('textures/hud/hud.png', (128, 128))
        self.hud_hit_face = self.get_texture('textures/hud/hud_hit.png', (128, 128))
        self.hud_face = self.get_texture('textures/hud/hud.png', (128, 128))
        self.game_over_image = self.get_texture('textures/game_over.png', (WITDH, HEIGHT))
    
    # Sky Render
        self.sky_image = self.get_texture('textures/sky/sky.png', (WITDH, HALF_HEIGHT))
        self.sky_offset = 0

    def draw(self):
        self.draw_background()
        self.render_game_object()
        self.draw_hud()

    def draw_hud(self):
        self.screen.blit(self.hud_face, (HALF_WITDH + 625, 125))

        bullet = str(self.game.weapon.bullet)
        for i, char in enumerate (bullet):
            self.screen.blit(self.digit[char], ((225 + i * self.digit_size), 175))
        health = str(self.game.player.hp)
        for i, char in enumerate (health):
            self.screen.blit(self.digit[char], ((225 + i * self.digit_size), 125))
        # self.screen.blit(self.digit['10'], ((225 + (i + 1) * self.digit_size), 125))

    # Draw Background (sky and floor) Method
    def draw_background(self):
    # sky
        self.sky_offset = (self.sky_offset + self.game.player.rel) % WITDH
        self.screen.blit(self.sky_image, (-self.sky_offset, 0))
        self.screen.blit(self.sky_image, (-self.sky_offset + WITDH, 0))
        # pg.draw.rect(self.screen, FLOOR_COLOR, (0, HALF_HEIGHT, WITDH, HEIGHT))
    # floor
        pg.draw.rect(self.screen, FLOOR_COLOR, (0, HALF_HEIGHT, WITDH, HEIGHT))

    def render_game_object(self):
        list_objects = sorted(self.game.raycasting.object_to_render, key=lambda t : t[0], reverse=True)
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos)

    def draw_game_over_image(self):
        self.game.screen.blit(self.game_over_image, (0, 0))
        
    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)
    
    def load_wall_textures(self):
        return{
            1: self.get_texture("textures/walls/1.jpg"),
            # 2: self.get_texture("textures/walls/2.png"),
            3: self.get_texture("textures/walls/3.jpg"),
            4: self.get_texture("textures/walls/4.jpg"),
            5: self.get_texture("textures/walls/5.jpg"),
            6: self.get_texture("textures/walls/6.jpg"),
            7: self.get_texture("textures/walls/7.jpg"),
            8: self.get_texture("textures/walls/8.jpg"),
            9: self.get_texture("textures/walls/9.jpg"),
            10: self.get_texture("textures/walls/10.jpg"),
            11: self.get_texture("textures/walls/11.jpg"),
            12: self.get_texture("textures/walls/12.jpg"),
            13: self.get_texture("textures/walls/13.jpg"),
            14: self.get_texture("textures/walls/14.jpg"),
            15: self.get_texture("textures/walls/15.jpg"),
            16: self.get_texture("textures/walls/16.png"),
            17: self.get_texture("textures/walls/17.png"),
            18: self.get_texture("textures/walls/18.png"),
            19: self.get_texture("textures/walls/19.png"),
            20: self.get_texture("textures/walls/20.png"),
            21: self.get_texture("textures/walls/21.png"),
            22: self.get_texture("textures/walls/22.png"),
            23: self.get_texture("textures/walls/23.png"),
            24: self.get_texture("textures/walls/24.png"),
            25: self.get_texture("textures/walls/25.png"),
            26: self.get_texture("textures/walls/26.png"),
            27: self.get_texture("textures/walls/27.png"),
        }

