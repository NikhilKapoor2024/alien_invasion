import pygame.font

class Button:
    """A class representing a button"""

    def __init__(self, ai_game, msg):
        """Initializes button attributes"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # dimensions and color of button (color: RGB) + pygame Font object
        self.width, self.height = 200, 50
        self.text_color = (255, 255, 255)
        self.button_color = (0, 255, 0)
        self.font = pygame.font.SysFont(None, 48)

        # rect and centering
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # call _prep_msg to render text as image (only need to do this once thx to _prep_msg function)
        self._prep_msg(msg)
    

    def _prep_msg(self, msg):
        """Renders msg param into image then centers on button"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    

    def draw_button(self):
        """Draws button then message"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

