import random
from settings import *
import pygame


ITEM_IMAGE = [GUN_IMAGE, VACCINE_IMAGE, MASK_IMAGE]


class Items(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(ITEM_IMAGE)
        self.image = self.type
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(30, WIDTH-30)
        self.rect.bottom = random.randrange(-100, -50)
        self.speedy = 5         # 道具下降速度

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:        # 如果道具超出螢幕，重置位置
            self.kill()

    def health_recover(self, player):
        player.health += 20
        if player.health > 100:
            player.health = 100

    def gunup(self, player):
        player.gun += 1
        player.gun_time = pygame.time.get_ticks()

    def attackbuff(self, player):
        player.damage += random.randrange(-8, 8)
        if player.damage <= 0:
            player.damage = 1
        elif player.damage >= 20:
            player.damage = 20
