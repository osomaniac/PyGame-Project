import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        ## load alien and rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        ## start each near alien near top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        ## store exact horizontal positoin
        self.x = float(self.rect.x)