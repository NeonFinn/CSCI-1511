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

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)
            self.ship.blit_me()

            pygame.display.flip()
            self.clock.tick(self.settings.frame_rate)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()