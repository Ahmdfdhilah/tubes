class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self._image = image
        self._x_pos = pos[0]
        self._y_pos = pos[1]
        self._font = font
        self._base_color = base_color
        self._hovering_color = hovering_color
        self._text_input = text_input
        self._text = self._font.render(self._text_input, True, self._base_color)
        if self._image is None:
            self._image = self._text
        self._rect = self._image.get_rect(center=(self._x_pos, self._y_pos))
        self._text_rect = self._text.get_rect(center=(self._x_pos, self._y_pos))

    def update(self, screen):
        if self._image is not None:
            screen.blit(self._image, self._rect)
        screen.blit(self._text, self._text_rect)

    def check_for_input(self, position):
        if position[0] in range(self._rect.left, self._rect.right) and position[1] in range(self._rect.top, self._rect.bottom):
            return True
        return False

    def change_color(self, position):
        if position[0] in range(self._rect.left, self._rect.right) and position[1] in range(self._rect.top, self._rect.bottom):
            self._text = self._font.render(self._text_input, True, self._hovering_color)
        else:
            self._text = self._font.render(self._text_input, True, self._base_color)

# class Button():
# 	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
# 		self.image = image
# 		self.x_pos = pos[0]
# 		self.y_pos = pos[1]
# 		self.font = font
# 		self.base_color, self.hovering_color = base_color, hovering_color
# 		self.text_input = text_input
# 		self.text = self.font.render(self.text_input, True, self.base_color)
# 		if self.image is None:
# 			self.image = self.text
# 		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
# 		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

# 	def update(self, screen):
# 		if self.image is not None:
# 			screen.blit(self.image, self.rect)
# 		screen.blit(self.text, self.text_rect)

# 	def checkForInput(self, position):
# 		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
# 			return True
# 		return False

# 	def changeColor(self, position):
# 		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
# 			self.text = self.font.render(self.text_input, True, self.hovering_color)
# 		else:
# 			self.text = self.font.render(self.text_input, True, self.base_color)