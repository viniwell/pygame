import pygame
import sys
class Rocket:
    '''Управление кораблем'''
    def __init__(self, screen):
        '''инициализирует корабль и задает его начальную позицию'''
        self.screen=screen
        self.screen_rect=screen.get_rect()
        #Загружает изображение корабля и получает прямоугольник
        self.image=pygame.image.load('rocket.png')
        self.rect=self.image.get_rect()
        self.rect.midbottom=self.screen_rect.midbottom
        self.x=float(self.rect.x)
        self.y=float(self.rect.y)
        self.moving_right=False
        self.moving_left=False
        self.moving_top=False
        self.moving_down=False
    def blitme(self):
        '''Рисует корабль в текущей позиции'''
        self.screen.blit(self.image, self.rect)
    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.x+=1
        if self.moving_left and self.rect.left>0:
            self.x-=1
        if self.moving_top and self.y>0:
            self.y-=1
        if self.moving_down and self.rect.bottom<self.screen_rect.bottom:
            self.y+=1
        
        self.rect.x=self.x
        self.rect.y=self.y
class Adventure:
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((1200, 800))
        self.rocket=Rocket(self.screen)
    def run_g(self):
        while True:
            self._check_events()
            self.rocket.update()
            self._update_screen()
    def _update_screen(self):
        self.screen.fill((238, 238, 238))
        self.rocket.blitme()
        pygame.display.flip()
    def _check_events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                self._check_k_d_events(event)
            elif event.type==pygame.KEYUP:
                self._check_k_up_events(event)
    def _check_k_d_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key==pygame.K_UP:
            self.rocket.moving_top=True
        elif event.key==pygame.K_DOWN:
            self.rocket.moving_down=True
    def _check_k_up_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        elif event.key==pygame.K_UP:
            self.rocket.moving_top=False
        elif event.key==pygame.K_DOWN:
            self.rocket.moving_down=False
batman=Adventure()
batman.run_g()
        
