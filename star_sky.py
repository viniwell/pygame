import pygame
from pygame.sprite import Sprite
import sys
class Star(Sprite):
    def __init__(self, ss_game):
        '''Ініціалізує прибульця'''
        super().__init__()
        self.screen=ss_game.screen 
        #завантаження зображення прибульця та призначення атр rect
        self.image=pygame.image.load('star.png')
        self.rect=self.image.get_rect()
        #Кожен новий прибулець з'являється у лів верхньому куті
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        #збереження точної горизонтальної позиції
        self.x=float(self.rect.x)
    def update(self):
        self.rect.x=self.x
class Star_sky:
    def __init__(self):
        self.screen = pygame.display.set_mode((1200, 800))
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Star sky')
        self.stars=pygame.sprite.Group()
        self.create_stars()
    def create_stars(self):
        star = Star(self)
        alien_width, alien_height = star.rect.size
        available_space_x = self.screen_width
        number_aliens_x = available_space_x // alien_width

        # Визначення кількості рядів
        available_space_y = self.screen_height
        number_rows = available_space_y // alien_height

        # Створення флоту прибульців
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)  
    def _create_alien(self, alien_number, row_number):
        # Створення прибульця та розміщення його в ряду
        star=Star(self)
        alien_width, alien_height = star.rect.size
        star.x = alien_width + 2 * alien_width * alien_number
        star.rect.x = star.x
        star.rect.y = alien_height + 2 * alien_height * row_number
        self.stars.add(star)
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
            self.stars.update()
            self.update_screen()
    def update_screen(self):
        self.screen.fill((230, 230, 230))
        self.stars.draw(self.screen)
        pygame.display.flip()
ss=Star_sky()
ss.run_game()