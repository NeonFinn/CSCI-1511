import pygame

class Ship:
    def __init__ (self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        original_image = pygame.image.load('resources/ship2(no bg).png')
        self.image = pygame.transform.rotate(original_image, -90)
        self.rect = self.image.get_rect()

        self.rect.midleft = self.screen_rect.midleft

        self.moving_up = False
        self.moving_down = False

        self.settings = ai_game.settings

        self.y = float(self.rect.y)

    def update(self):
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.ship_speed
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        self.rect.y = self.y

    def blit_me(self):
        self.screen.blit(self.image, self.rect)