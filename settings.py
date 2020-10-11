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

        ''' Bullet Settings '''
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (83,192,255)
        self.bullets_allowed = 3

        ''' Star Settings '''
        self.NUMBER_STARS = 200

        ''' Alien Settings '''
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        ## fleet direction of 1 = rigth, -1 = left
        self.fleet_direction = 1