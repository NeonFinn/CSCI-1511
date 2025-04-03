import pygame
from settings import Settings

class Ship:
    def __init__ (self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('resources/ship2(no bg).png')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.moving_right = False
        self.moving_left = False

        self.settings = Settings()

        self.x = float(self.rect.x)

    def update(self):
        if self.moving_right:
            self.x += self.settings.ship_speed
        elif self.moving_left:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blit_me(self):
        self.screen.blit(self.image, self.rect)