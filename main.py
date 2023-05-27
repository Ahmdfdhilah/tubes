import pygame as pg
import time
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
from dialog import *
from button import Button

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
        self.background_music = pg.mixer.Sound(
            'sound/theme.mp3')
        self.new_game()
        self.dialog_data = dialog_data

    def dialog(self, index):
        obj__dialog = DialogBox()
        obj__dialog.get_dialog(self.dialog_data[index])

    def new_game(self):
        self.loss = False
        self.win = False
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        self.object_handler = ObjectsHandler(self)
        self.weapon = weapon(self)
        self.sound = Sound(self)
        print(len(self.object_handler.npc_list))
        self.pathfinding = PathFinding(self)
        self.background_music.play(-1, 0, 7000)

    def game_over(self):
        self.loss = True

    def game_win(self):
        self.win = True

    def update(self):
        if self.loss:
            self.object_renderer.draw_game_over_image()
            pg.mixer.Sound.stop(self.background_music)
            pg.mouse.set_visible(True)
            pg.display.flip()
            time.sleep(3)
            menu.main_menu()
        elif self.win:
            self.dialog(1)
            pg.mixer.Sound.stop(self.background_music)
            pg.mouse.set_visible(True)
            menu.main_menu()
        else:
            self.player.update()
            self.raycasting.update()
            self.object_handler.update()
            self.weapon.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f"{self.clock.get_fps() :.1f}")

    def draw(self):
        self.object_renderer.draw()
        self.weapon.draw()

    def check_events(self):
        self.global_trigger = False
        for event in pg.event.get():
            if (
                event.type == pg.QUIT
                or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE)
                or len(self.object_handler.npc_list) < 1
            ):
                pg.QUIT()
                sys.exit()
            elif event.type == self.global_event:
                self.global_trigger = True
            self.player.single_fire_event(event)
            self.player.reloading(event)

    def run(self):
        #self.dialog(0)
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
    def play(self):
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
                    line_text = pg.transform.scale(
                        line_text, (int(max_width), line_text.get_height())
                    )
                if line_text.get_height() > max_height:
                    line_text = pg.transform.scale(
                        line_text, (line_text.get_width(), int(max_height))
                    )

                line_rect = line_text.get_rect(
                    center=(
                        self.SCREEN.get_width() // 2,
                        self.SCREEN.get_height() // 2 + i * 50,
                    )
                )
                self.SCREEN.blit(line_text, line_rect)

            OPTIONS_BACK = Button(
                image=None,
                pos=(HALF_WITDH, 800),
                text_input="BACK",
                font=self.font,
                base_color="Black",
                hovering_color="Green",
            )

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
            MENU_RECT = MENU_TEXT.get_rect(center=(HALF_WITDH, 250))

            PLAY_BUTTON = Button(
                image=pg.image.load("assets/Play Rect.png"),
                pos=(HALF_WITDH, 510),
                text_input="PLAY",
                font=self.font,
                base_color="#000000",
                hovering_color="White",
            )
            OPTIONS_BUTTON = Button(
                image=pg.image.load("assets/Options Rect.png"),
                pos=(HALF_WITDH, 660),
                text_input="ABOUT",
                font=self.font,
                base_color="#000000",
                hovering_color="White",
            )
            QUIT_BUTTON = Button(
                image=pg.image.load("assets/Quit Rect.png"),
                pos=(HALF_WITDH, 810),
                text_input="QUIT",
                font=self.font,
                base_color="#000000",
                hovering_color="White",
            )

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


if __name__ == "__main__":
    menu = Menu()
    menu.main_menu()
