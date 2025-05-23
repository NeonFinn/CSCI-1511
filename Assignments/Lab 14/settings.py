class Settings:

    def __init__(self):
        self.game_name = "Alien Invasion"
        self.screen_width = 1200
        self.screen_height = 800
        self.resolution = (self.screen_width, self.screen_height)
        self.bg_color = (0, 0, 0)
        self.frame_rate = 60
        self.ship_speed = 3
        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 3
        self.alien_speed = 1.0
        self.fleet_direction = 1
        self.fleet_drop_speed = 10
        self.ship_limit = 3
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initalize_dynamic_settings()

    def initalize_dynamic_settings(self):
        self.ship_speed = 3
        self.bullet_speed = 2.5
        self.alien_speed = 2.0
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)