import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class managing bullets from the ship"""

    def __init__(self, ai_game):
        """Initializes bullet at the ship's current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = ai_game.settings.bullet_color

        # Create bullet rect at (0, 0) and set position to ship's rect.midtop
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store bullet's position as decimal value
        self.y = float(self.rect.y)
    

    def update(self):
        """Move bullet up the screen"""
        # Update decimal position, THEN the rect position of the bullet
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y
    
    
    def draw_bullet(self):
        """Draw bullet onscreen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
