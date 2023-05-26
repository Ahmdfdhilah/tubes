import pygame as pg
import sys
import textwrap
from subprocess import Popen
from settings import *
from map import *
from player import *
from raycasting import *
from obj_render import *
from sprite_obj import *
from objects import *
from weapon import *
from sound import *
from npc import *
from path_finding import *
from hud import *
from dialog import *
from button import Button
dialog_data = []
dialog_data_prologue = [
    {"text": "Pada Tahun 20XX, Bumi mengalami kekacauan dengan datangnya monster-monster yang ingin mendominasi Bumi", "character_image": "textures\chara\watcher.png"},
    {"text": "Para monster sudah menyebar terlalu banyak sehingga populasi manusia saat ini hanya berkisar 20%", "character_image": "textures\chara\watcher.png"},
    {"text": "Masih menjadi misteri darimana monster tersebut tetapi diduga ada beberapa orang mencurigakan terlibat", "character_image": "textures\chara\watcher.png"},
    {"text": "Manusia yang tersisa bersembunyi di dalam bunker yang dihuni beberapa warga dan ilmuwan", "character_image": "textures\chara\watcher.png"},
    {"text": "Para ilmuwan sudah menyiapkan beberapa prajurit uji coba yang sudah dibekukan sebelum bencana terjadi", "character_image": "textures\chara\watcher.png"},
    {"text": "Para prajurit tersebut telah di cairkan untuk melawan monster yang sudah mulai menginvasi bumi", "character_image": "textures\chara\watcher.png"},
    {"text": "Uhh...dimana ini?", "character_image": "textures\chara\ghulwan.png"},
    {"text": "Sudah waktunya bangun ghulwan, dunia sekarang dilanda kekacauan", "character_image": "textures\chara\david.png"},
    {"text": "David!? Jadi begitu, jelaskan rinciannya!", "character_image": "textures\chara\ghulwan.png"},
    {"text": "David menjelaskan keadaan bumi dan bagaimana dia sudah dibangunkan", "character_image": "textures\chara\watcher.png"},
    {"text": "Bagaimana dengan prajurit lain?", "character_image": "textures\chara\ghulwan.png"},
    {"text": "Mereka sudah menjalani proses pencairan dan sedang menunggu di luar", "character_image": "textures\chara\david.png"},
    {"text": "Baiklah ayo kita temui mereka", "character_image": "textures\chara\ghulwan.png"},
    {"text": "Wah lihat siapa yang baru terbangun", "character_image": "textures\chara\ihsan.png"},
    {"text": "Sekarang akhirnya kita lengkap", "character_image": "textures\chara\jatmiko.png"},
    {"text": "Haha sepertinya kalian baik-baik saja ya", "character_image": "textures\chara\ghulwan.png"},
    {"text": "Waktunya bertugas kah?", "character_image": "textures\chara\david.png"},
    {"text": "Santai dulu ga sih?", "character_image": "textures\chara\jatmiko.png"},
    {"text": "Iya, selama kita di bunker pasti akan ama-", "character_image": "textures\chara\ihsan.png"},
    {"text": "Tiba-tiba terdengar suara ledakan dan sirine berbunyi diiringi para tentara dan beberapa monster menerobos bunker", "character_image": "textures\chara\watcher.png"},
    {"text": "Hahaha...Akhirnya kutemukan, para tentara serang mereka!", "character_image": "textures\chara\omandre.png"},
    {"text": "Dia kan Professor Andre, ilmuwan terbaik sebelum kita dibekukan", "character_image": "textures\chara\ihsan.png"},
    {"text": "Kudengar dia hilang secara misterius", "character_image": "textures\chara\jatmiko.png"},
    {"text": "Sepertinya kita tahu alasannya, dan harus menghentikannya", "character_image": "textures\chara\ghulwan.png"},
    {"text": "Waduh tapi kita belum makan sama sekali", "character_image": "textures\chara\ihsan.png"},
    {"text": "MAKAN TIDAK PERLU, TARUNG NOMOR SATU!!!", "character_image": "textures\chara\david.png"},
    {"text": "Ayo maju!", "character_image": "textures\chara\ghulwan.png"} 
    ]
    
dialog_data_epilog = [
    {"text": "Huft...Apakah sudah selesai?", "character_image": "textures\chara\ghulwan.png"},
    {"text": "Dimana Andre?", "character_image": "textures\chara\jatmiko.png"},
    {"text": "HAHAHA...Akhirnya kudapatkan hal yang dibutuhkan!", "character_image": "textures\chara\omandre.png"},
    {"text": "Dengan ini karya terbaikku akan tercipta...Adios para prajurit!", "character_image": "textures\chara\omandre.png"},
    {"text": "Waduhh...dia kabur", "character_image": "textures\chara\david.png"},
    {"text": "Setidaknya kita tahu kalau dialah yang menciptakan monster", "character_image": "textures\chara\jatmiko.png"},
    {"text": "Mau tidak mau kita harus keluar bunker kah...", "character_image": "textures\chara\ihsan.png"},
    {"text": "Perjalanan kita masih panjang", "character_image": "textures\chara\ghulwan.png"},
    {"text": "Para prajurit berhasil mengalahkan musuh-musuh yang menyerang bunker mereka", "character_image": "textures\chara\watcher.png"},
    {"text": "Tetapi, Prof.Andre berhasil kabur dengan membawa sesuatu untuk niat jahatnya", "character_image": "textures\chara\watcher.png"},
    {"text": "Para prajurit akan memulai petualangan mereka menghadapi musuh yang lebih berbahaya", "character_image": "textures\chara\watcher.png"},
    {"text": "TO BE CONTINUED", "character_image": "textures\chara\watcher.png"}
]
dialog_data.append(dialog_data_prologue)
dialog_data.append(dialog_data_epilog)
class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.global_trigger = False
        self.global_event = pg.USEREVENT + 0
        pg.time.set_timer(self.global_event, 40)
        self.new_game()
        self.dialog_data = dialog_data
    def dialog(self,index):
        get_dialog(self.dialog_data[index])
    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        self.object_handler = ObjectsHandler(self)
        self.weapon = weapon(self)
        self.sound = Sound(self)
        print(len(self.object_handler.npc_list))
        self.pathfinding = PathFinding(self)
        
    def update(self):
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        self.weapon.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        # self.screen.fill('black') 
        self.object_renderer.draw()
        self.weapon.draw()
        # self.map.draw()
        # self.player.draw()

    def check_events(self):
        self.global_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE) or len(self.object_handler.npc_list)<1:
                pg.QUIT()
                sys.exit()
            elif event.type == self.global_event:
                self.global_trigger = True
            self.player.single_fire_event(event)
            self.player.reloading(event)

    def run(self):
        self.dialog(0)
        while True:
            self.check_events()
            self.update()
            self.draw()

class Menu:
    def __init__(self):
        pg.init()
        self.SCREEN = pg.display.set_mode(RES)
        pg.display.set_caption("Menu")
        self.BG = pg.image.load("assets/bg8.jpg")
        self.font = pg.font.Font("assets/font.ttf", 45)
        # self.default_mode = pg.display.set_mode(RES)

    def play(self): 
        # self.default_mode = pg.display.set_mode(RES)
        # pg.display.set_mode(self.default_mode) 
        game = Game()
        game.run()  
    
    def options(self):
        while True:
            OPTIONS_MOUSE_POS = pg.mouse.get_pos()

            self.SCREEN.blit(self.BG, (0, 0)) 

            # Long string
            text = "Game ini berlatar di sebuah bunker dimana bumi mengalami kehancuran dikarenakan munculnya monster yang diciptakan untuk mendominasi bumi"

            # Calculate the maximum width and height based on the resolution
            max_width = 0.6 * self.SCREEN.get_width()  # 80% of the screen width
            max_height = 0.8 * self.SCREEN.get_height()  # 80% of the screen height

            # Split the long string into multiple lines to fit within the maximum width and height
            lines = textwrap.wrap(text, width=50)

            # Render each line of the text
            for i, line in enumerate(lines):
                line_text = self.font.render(line, True, "Black")

                # Adjust font size if the text exceeds the maximum width or height
                if line_text.get_width() > max_width:
                    line_text = pg.transform.scale(line_text, (int(max_width), line_text.get_height()))
                if line_text.get_height() > max_height:
                    line_text = pg.transform.scale(line_text, (line_text.get_width(), int(max_height)))

                line_rect = line_text.get_rect(center=(self.SCREEN.get_width() // 2, self.SCREEN.get_height() // 2 + i * 50))
                self.SCREEN.blit(line_text, line_rect)

            OPTIONS_BACK = Button(image=None, pos=(HALF_WITDH, 800),
                                text_input="BACK", font=self.font, base_color="Black", hovering_color="Green")

            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(self.SCREEN)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        self.main_menu()

            pg.display.update()

       
    def main_menu(self):
        while True:
            self.SCREEN.blit(self.BG, (0, 0))

            MENU_MOUSE_POS = pg.mouse.get_pos()

            MENU_TEXT = self.font.render("Apocalypse Dominator", True, "#000000")
            MENU_RECT = MENU_TEXT.get_rect(center=(HALF_WITDH,250))

            PLAY_BUTTON = Button(image=pg.image.load("assets/Play Rect.png"), pos=(HALF_WITDH, 510), 
                                text_input="PLAY", font=self.font, base_color="#000000", hovering_color="White")
            OPTIONS_BUTTON = Button(image=pg.image.load("assets/Options Rect.png"), pos=(HALF_WITDH, 660), 
                                text_input="ABOUT", font=self.font, base_color="#000000", hovering_color="White")
            QUIT_BUTTON = Button(image=pg.image.load("assets/Quit Rect.png"), pos=(HALF_WITDH, 810), 
                                text_input="QUIT", font=self.font, base_color="#000000", hovering_color="White")

            self.SCREEN.blit(MENU_TEXT, MENU_RECT)

            for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.SCREEN)
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        
                        self.play()
                    if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.options()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pg.quit()
                        sys.exit()

            pg.display.update()



if __name__ == '__main__':    
    menu = Menu()
    menu.main_menu()