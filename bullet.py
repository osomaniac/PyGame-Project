import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_game):
        ## bullet object at ship's position
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        ## bullet rect at (0,0) then set to correct position
        self.rect = pygame.Rect(0,0,self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        ## store bullet's position as decimal value
        self.y = float(self.rect.y)

    def update(self):
        ## update decimal positoin
        self.y -= self.settings.bullet_speed
        ## update rect position
        self.rect.y = self.y

    def draw_bullet(self):
        ## draw bullet on screen
        pygame.draw.rect(self.screen, self.color, self.rect)