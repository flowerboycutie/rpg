import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.Surface((TILESIZE,TILESIZE))
        self.image.fill((0, 255, 0))

        # self.image = pygame.image.load('../graphics/test/rock.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0,-10)