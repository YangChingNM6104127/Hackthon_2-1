from enemy import *
from player import *
from item import *
from settings import *
from view import *
import pygame


class Model(pygame.sprite.Sprite):
    def __init__(self):
        self.all_sprites = pygame.sprite.Group()  # 這個sprite.group是pygame內建的東西，下面update跟draw可以把畫面顯示出來
        self.enemies = pygame.sprite.Group()      # 創建enemy的group，把所有新增的敵人存入
        self.bullets = pygame.sprite.Group()      # 創建bullet的group，把所有新增的子彈存起來，要有shoot的動作才會新增子彈
        self.items = pygame.sprite.Group() 