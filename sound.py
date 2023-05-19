import pygame as pg

class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'sound/'
        self.colt = pg.mixer.Sound(self.path + 'colt.mp3')
        self.player_pain = pg.mixer.Sound(self.path + "zeta_pain.mp3")
        self.npc_pain = pg.mixer.Sound(self.path + 'Pain1.mp3')
        self.npc_shot = pg.mixer.Sound(self.path + 'colt.mp3')
        self.npc_death = pg.mixer.Sound(self.path + 'Pain_Sound.mp3')
        self.theme_song = pg.mixer.music.load(self.path + 'theme.mp3')