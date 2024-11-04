import pygame

class Ship:
    """A class managing a user-controlled ship"""

    def __init__(self, ai_game):
        """Initalizes the Ship class object with AlienInvasion attributes"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Load ship and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # store ship's rect.x position as a float
        self.x = float(self.rect.x)

        # Movement flags (used in update())
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """Updates ship position based on keypress"""
        # Update ship's x-value, not rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        # Update rect object from self.x
        self.rect.x = self.x


    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)