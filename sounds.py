import pygame
from pygame.mixer import Sound

class Sounds:
    def __init__(self):
        pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
        self.bullet_sound = pygame.mixer.Sound("sounds/bullet_sound.wav")
        self.hit_sound = pygame.mixer.Sound("sounds/hit_sound.wav")
        self.game_over =  pygame.mixer.Sound("sounds/game_over.wav")
        self.start_sound = pygame.mixer.Sound("sounds/start_sound.wav")
        self.lost_ship = pygame.mixer.Sound("sounds/lost_ship.wav")


    def start_bg_music(self):
        pygame.mixer.music.load('sounds/bg_music.wav')
        pygame.mixer.music.play(-1)

    def play_lost_ship_sound(self):
        pygame.mixer.Sound.play(self.lost_ship)
        
    def play_bullet_sound(self):
        pygame.mixer.Sound.play(self.bullet_sound)

    def play_hit_sound(self):
        pygame.mixer.Sound.play(self.hit_sound)
    
    def play_game_over_sound(self):
        pygame.mixer.Sound.play(self.game_over)

    def play_start_sound(self):
        pygame.mixer.Sound.play(self.start_sound)

