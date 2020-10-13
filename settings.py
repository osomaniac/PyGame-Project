## Class to store settings for Alien Invasion
class Settings:
    def __init__(self):
        ## initalize settings
        ''' Screen Settings '''
        self.screen_width = 975
        self.screen_height = 650
        self.bg_color = (8,8,13)

        ''' Ship Settings '''
        self.ship_speed = 1.5
        self.ship_limit = 2

        ''' Bullet Settings '''
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (83,192,255)
        self.bullets_allowed = 3

        ''' Star Settings '''
        self.NUMBER_STARS = 200

        ''' Alien Settings '''
        self.alien_speed = .75
        self.fleet_drop_speed = 10
        ## fleet direction of 1 = rigth, -1 = left
        self.fleet_direction = 1

        ''' Difficulty Increase Settings '''
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()
        self.score_scale = 1.5

        ''' Scoring Settings '''
        self.alien_points = 50

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_spreed = 3.0
        self.alien_speed = 1.0
        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)