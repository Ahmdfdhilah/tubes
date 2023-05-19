import pygame as pg
import math
from settings import *
from weapon import *

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
        self.shot = False
        self.hp = PLAYER_MAX_HP

    def get_damage(self, damage):
        self.hp -= damage
        # self.game.object_renderer.player_damage()
        self.game.sound.player_pain.play()

    def single_fire_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1 and not self.shot and not self.game.weapon.reloading and not self.game.weapon.bullet_empty:
                self.game.weapon.check_bullet()
                self.game.weapon.shot()
                self.game.sound.colt.play()
                self.game.weapon.reloading = True

    def reloading(self, event):
        if event.type == pg.K_r:
            if event.button == 1:
                self.game.weapon.reload()

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy =0, 0
        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_a]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:
            dx += -speed_sin
            dy += speed_cos

        if keys[pg.K_r]:
            self.game.weapon.reload()
            
        self.check_wall_collision(dx, dy)

        if keys[pg.K_LEFT]:
            self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        if keys[pg.K_RIGHT]:
            self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        self.angle %= math.tau

    def check_wall(self, x, y):
        return (x, y) not in self.game.map.world_map
    
    def check_wall_collision(self, dx, dy):
        scale = PLAYER_SIZE_SCALE / self.game.delta_time
        if self.check_wall(int(self.x + dx * scale), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy * scale)):
            self.y += dy

    def draw(self):
        pg.draw.line(self.game.screen, 'yellow', (self.x * 100, self.y * 100), 
                   (self.x * 100 + WITDH*math.cos(self.angle), 
                   self.y * 100 + WITDH*math.sin(self.angle)), 2)
        pg.draw.circle(self.game.screen, 'green',(self.x * 100, self.y * 100), 15)

    def mouse_control(self):
        mx, my = pg.mouse.get_pos()
        if mx < MOUSE_BORDER_LEFT or mx > MOUSE_BORDER_RIGHT:
            pg.mouse.set_pos([HALF_WITDH, HALF_HEIGHT])
        self.rel = pg.mouse.get_rel()[0]
        self.rel = max(-MOUSE_MAX_REL, min(MOUSE_MAX_REL, self.rel))
        self.angle += self.rel * MOUSE_SENS * self.game.delta_time

    def update(self):
        self.movement()
        self.mouse_control()

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x ), int(self.y)