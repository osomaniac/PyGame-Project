import sys 
import pygame 
from settings import Settings
from ship import Ship

class AlienInvasion:
    def __init__(self):
        ## initialize game
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        ## main loop for game
        while True:
            self._check_events()
            self.ship.update()
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

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        ## update images on the screen
        ## redraw screen during each pass through loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        ## make recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    ## make a game instance and run game
    ai = AlienInvasion()
    ai.run_game()