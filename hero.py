import pygame
import sys
class Hero:
    '''Управление кораблем'''
    def __init__(self, screen):
        '''инициализирует корабль и задает его начальную позицию'''
        self.screen=screen
        self.screen_rect=screen.get_rect()
        #Загружает изображение корабля и получает прямоугольник
        self.image=pygame.image.load('batman.bmp')
        self.rect=self.image.get_rect()
        self.rect.midbottom=self.screen_rect.midbottom
    def blitme(self):
        '''Рисует корабль в текущей позиции'''
        self.screen.blit(self.image, self.rect)
class Batman:
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((1200, 800))
        self.hero=Hero(self.screen)
    def run_g(self):
        while True:
            self._check_events()
            self._update_screen()
    def _update_screen(self):
        self.screen.fill((163, 163, 163))
        self.hero.blitme()
        pygame.display.flip()
    def _check_events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
batman=Batman()
batman.run_g()



