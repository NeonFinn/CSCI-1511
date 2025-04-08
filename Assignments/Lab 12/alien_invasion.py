import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(self.settings.resolution)
        self.clock = pygame.time.Clock()
        self.ship = Ship(self)
        pygame.display.set_caption(self.settings.game_name)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_w or event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_w or event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)

        self.ship.blit_me()

        pygame.display.flip()

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(self.settings.frame_rate)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()