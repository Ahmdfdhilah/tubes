from sprite_obj import *
from npc import *

class ObjectsHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_sprite_path = 'sprite/NPC/'
        self.static_sprite_path = 'sprite/Static/'
        self.anim_sprite_path = 'sprite/Animated/'
        add_sprite = self.add_sprite
        add_npc = self.add_npc
        self.npc_pos = {}

        # Sprite Map
        # add_sprite(SpriteObj(game))
        add_sprite(AnimatedSprite(game))
        add_sprite(AnimatedSprite(game, pos=(7, 2)))
        add_sprite(AnimatedSprite(game, pos=(2, 4)))
        add_sprite(AnimatedSprite(game, pos=(10.5, 7.5)))

        # NPC map
        add_npc(NPC(game))
        add_npc(NPC(game, pos=(4.5, 25.5)))
        add_npc(NPC(game, pos=(23, 28)))
        add_npc(NPC(game, pos=(21, 2)))
        add_npc(NPC(game, pos=(3, 2)))
        add_npc(NPC(game, pos=(18, 12)))
        
        # add_npc(NPC(game))
        # add_npc(NPC(game))
        # add_npc(NPC(game))
        # add_npc(NPC(game))
        # add_npc(NPC(game))

        


    def update(self):
        self.npc_pos = {npc.map_pos for npc in self.npc_list if npc.alive}
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]

    def add_npc(self, npc):
        self.npc_list.append(npc)

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)