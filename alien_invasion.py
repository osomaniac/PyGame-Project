import sys 
from time import sleep
import pygame 
from random import randint as r
from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from star import Star


class AlienInvasion:
    def __init__(self):
        ## initialize game
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.stars = pygame.sprite.Group()
        self._create_sky()
        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        

        self._create_fleet()

    def run_game(self):
        ## main loop for game
        while True:
            self._check_events()
            
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                
            self._update_screen()

    def _check_events(self):
        ## responds to keypresses and mouse events
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        ## respond to key presses
        if event.key == pygame.K_RIGHT:
            ## move ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _ship_hit(self):
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()
            sleep(0.5)
        else:
            self.stats.game_active = False

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        ## create a new bullet and add it to group
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        ## update bullet positions
        self.bullets.update()
        ## get rid of bullets off screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()
        
    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
    
    def _check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _create_sky(self):
        for s in range(self.settings.NUMBER_STARS):
            self._create_star()

    def _create_star(self):
        star = Star(self)
        x_loc = r(0,self.settings.screen_width)
        y_loc = r(0, self.settings.screen_height)
        star.rect.x = x_loc
        star.rect.y = y_loc
        self.stars.add(star)

    def _create_fleet(self):
        ## make an alien
        alien = Alien(self)

        ## determine how many aliens can fit on a row
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2*alien_width)
        number_alien_x = available_space_x // (2*alien_width)

        ## determine number of rows that fit on a screen
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                                (3*alien_height) - ship_height)
        number_rows = available_space_y // (2*alien_height)

        ## create full fleet of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_alien_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2*alien.rect.height*row_number
        self.aliens.add(alien)
    
    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

        ## look for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        
        ## look for aliens hitting bottom of screen
        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        ## update images on the screen
        ## redraw screen during each pass through loop
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        ## make recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    ## make a game instance and run game
    ai = AlienInvasion()
    ai.run_game()