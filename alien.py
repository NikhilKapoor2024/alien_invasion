import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class managing a computer-controlled alien sprite"""

    def __init__(self, ai_game):
        """Initalizes alien object"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load image of alien and store rectangular representation
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # Start each new alien at the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Get exact horizontal position
        self.x = float(self.rect.x)
    

    def check_edges(self):
        """Checks if the alien reaches the edge"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
    

    def update(self):
        """Update alien sprite"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

