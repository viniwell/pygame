import pygame
import sys
    
def check_events():
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_k_d_events(event)
def check_k_d_events(event):
    if event.key == pygame.K_ESCAPE:
        sys.exit()
    else:
        print(event.key)
pygame.init()  
screen=pygame.display.set_mode((1200, 800))
while True:
    check_events()
    pygame.display.flip()