from msilib.schema import Class
import pygame,random

from meteoros import Player

alto    = 600
ancho   = 800
blanco  = (255,255,255)
negro   = (0,0,0)
done    = False

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("x-wing.png").convert()
        self.image.set_colorkey(negro)
        self.rect = self.image.get_rect()
    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        pass
        #player.rect.x = mouse_pos[0]
        #player.rect.y = mouse_pos[1]