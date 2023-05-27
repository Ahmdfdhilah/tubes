from sprite_obj import *

class weapon(AnimatedSprite):
    def __init__(self, game, path='sprite/weapon/wennie/1.png', scale=.3, animation_time=80):
        super().__init__(game=game, path=path, scale=scale, animation_time=animation_time)
        # self.shoot_images = self.get_images(self.path + '/shoot')
        # self.reload_images = self.get_images(self.path + '/reload')

        self.images = deque(
            [pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
             for img in self.images])
        
        self.weapon_pos = (HALF_WITDH - self.images[0].get_width() // 2, HEIGHT - self.images[0].get_height())
        self.reloading = False
        self.num_images = len(self.images)
        self.frame_counter = 0
        self.damage = 80
        self.max_bullet = 10
        self.bullet_empty = False
        self.bullet = self.max_bullet

    def check_bullet (self):
        if self.bullet < 1:
            self.bullet_empty = True
        else : 
            self.bullet_empty = False

    def weapon_logic(self):
        if self.bullet_empty:
            self.reloading = True
            self.bullet = self.max_bullet
            self.bullet_empty = False

    def reload(self):
        self.bullet = self.max_bullet 
        self.reloading = False
        self.check_bullet()

    def shot(self):
        self.game.player.shot = True
        self.bullet -= 1
        self.check_bullet()
        print( self.bullet)


    def animate_shot(self):
        if self.reloading:
            self.game.player.shot = False
            if self.animation_trigger:
                self.images.rotate(-1)
                self.image = self.images[0]
                self.frame_counter += 1
                if self.frame_counter == self.num_images:
                    self.reloading = False
                    self.frame_counter = 0

    def draw(self):
        self.game.screen.blit(self.images[0], self.weapon_pos)

    def update(self):
        self.check_animation_time()
        self.animate_shot()