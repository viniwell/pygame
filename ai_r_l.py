import sys
from pygame.sprite import Sprite
import pygame
class Ship:
    '''Управление кораблем'''
    def __init__(self, ai_game):
        '''инициализирует корабль и задает его начальную позицию'''
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()
        #Загружает изображение корабля и получает прямоугольник
        self.image=pygame.image.load('ship.bmp')
        self.rect=self.image.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана
        self.rect.midleft=self.screen_rect.midleft

        self.y=float(self.rect.y)
        #Флаг перемещения
        self.moving_right=False
        self.moving_left=False

    def update(self):
        '''Метод обновляет позицию корабля с учетом флага'''
        #Обновляется атрибут x
        if self.moving_right and self.rect.bottom<self.screen_rect.bottom:
            self.y+=5
        if self.moving_left and self.rect.top>0:
            self.y-=5
        #Обновление атрибута rect на основе self.x
        self.rect.y=self.y
    def blitme(self):
        '''Рисует корабль в текущей позиции'''
        self.screen.blit(self.image, self.rect)


class AlienInvasion:
    """Класс для управления ресурсами и поведением игры"""

    def __init__(self):
        """Инициализирует игру и слздает игровые ресурсы"""
        pygame.init()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    def _check_events(self):
        """Обрабатывает нажатия клавиш и события мыши"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)     

    def _check_keydown_events(self, event):
        """Реагирует на нажатие клавиш"""
        if event.key == pygame.K_DOWN:
            self.ship.moving_right = True
        elif event.key == pygame.K_UP:
            self.ship.moving_left = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        if event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Реагирует на отпускание клавиш"""
        if event.key == pygame.K_DOWN:
            self.ship.moving_right = False
        elif event.key == pygame.K_UP:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Создание нового снаряда и включение его в группу bullets"""
        if len(self.bullets)<3:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    def _update_bullets(self):
        """Обновляет позиции снарядлв и уничтожает старые снаряды"""
        self.bullets.update()
        #Удаление снарядов  вышедших за край
        for bullet in self.bullets.copy():  
           if bullet.rect.right>=self.screen.get_rect().right:
              self.bullets.remove(bullet)

    def _update_screen(self):
        """Обновляет изображения на экран е и отображает новый экран"""
        self.screen.fill((230, 230, 230))
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Отображение последнего прорисованного экрана
        pygame.display.flip()





class Bullet(Sprite):
    '''Класс для управления снарядами'''
    def __init__(self, ai_game):
        super().__init__()
        self.screen=ai_game.screen
        self.color=((0, 0, 250))

        #Создание снаряда в позиции 0:0 и назначение правильной позиции
        self.rect=pygame.Rect(0, 0, 15, 3)
        self.rect.midright=ai_game.ship.rect.midright

        #позиция снаряда хранится в вещ формате
        self.x=float(self.rect.x)

    def update(self):
        '''Пермещение снаряда'''
        self.x+=5
        self.rect.x=self.x
    def draw_bullet(self):
        '''Вывод снаряда на экран'''
        pygame.draw.rect(self.screen, self.color, self.rect)

if __name__ == '__main__':
    # Создание экземпляра и запуск игры
    ai = AlienInvasion()
    ai.run_game()