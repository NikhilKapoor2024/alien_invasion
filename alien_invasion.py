import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button

from time import sleep

class AlienInvasion:
    """A simple class to handle game assets and behaviors"""

    def __init__(self):
        """Creates objects for the video game (doesn't run it)"""
        pygame.init()
        self.settings = Settings()

        # window attributes
        self.screen = pygame.display.set_mode(
            size=(0, 0),
            flags=pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion!")

        # elements
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.stats = GameStats(self)

        # alien fleet
        self._create_fleet()

        # play button
        self.play_button = Button(self, "Play")


    def run_game(self):
        """Starts the game for reals"""
        while True:
            self._check_events()
            
            if self.stats.game_active == True:
                self.ship.update()
                self._update_bullets()
                self._update_alien()
            
            self._update_screen()


    def _check_events(self):
        """Checks user input (helper)"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    

    def _check_keydown_events(self, event):
        """When a key is pressed down"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()
    

    def _check_keyup_events(self, event):
        """When a key is released"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    

    def _fire_bullet(self):
        """Create a new bullet and add it to bullet group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    

    def _update_bullets(self):
        """Updates bullets group and gets rid of old bullets"""
        self.bullets.update()
        for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
        
        self._bullet_alien_collision()


    def _bullet_alien_collision(self):
        """Handles bullet/alien collision"""
        # if a bullet hits an alien, remove both from screen
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        # if fleet has been shot down, generate new fleet
        if not self.aliens:
            self.aliens.empty()
            self._create_fleet()
    

    def _create_fleet(self):
        """Create a fleet of aliens (create an alien and add it to aliens group)"""
        # Create an alien to get the alien's rectangle size
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        # Calculate available space and number of aliens for a row
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_of_aliens_x = available_space_x // (2 * alien_width)

        # Calculate available space for rows of aliens
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Create full fleet of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_of_aliens_x):
                self._create_alien(alien_number, row_number)
    

    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the row"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.y = alien_height + 2 * alien.rect.height * row_number
        alien.rect.x = alien.x
        alien.rect.y = alien.y
        self.aliens.add(alien)

    
    def _update_alien(self):
        self._check_fleet_edges()
        self.aliens.update()

        # if alien touches ship, print message and call _ship_hit()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            print("Ship hit!")
            self._ship_hit()
        
        # if alien touches bottom of screen, reset as well
        self._check_alien_bottom()

        
    def _check_fleet_edges(self):
        """Acts if the fleet hits an edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    
    def _change_fleet_direction(self):
        """Drops alien fleet and changes horiz direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    

    def _ship_hit(self):
        """Handle when a ship gets hit"""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()
            sleep(0.5)
        else:
            self.stats.game_active = False
    
    def _check_alien_bottom(self):
        """handles when alien fleet reaches bottom screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                print("Alien reached bottom!")
                self._ship_hit()
                break


    def _update_screen(self):
        """Updates images on screen (helper)"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()





if __name__ == "__main__":
    # Make a game instance, then run it
    ai = AlienInvasion()
    ai.run_game()