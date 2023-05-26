       while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

            self.SCREEN.fill("white")

            # Long string
            text = "Game ini berlatar di sebuah bunker dimana bumi mengalami kehancuran dikarenakan munculnya monster yang diciptakan untuk mendominasi bumi"

            # Split the long string into multiple lines to fit on the screen
            lines = textwrap.wrap(text, width=50)

            # Render each line of the text
            for i, line in enumerate(lines):
                line_text = self.font.render(line, True, "Black")
                line_rect = line_text.get_rect(center=(640, 200 + i*50))
                self.SCREEN.blit(line_text, line_rect)

            OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                                text_input="BACK", font=self.font, base_color="Black", hovering_color="Green")

            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(self.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        self.main_menu()

            pygame.display.update()