import random
from settings import *
import pygame


ENEMY_IMAGE = [ENEMY_IMAGE1, ENEMY_IMAGE2, ENEMY_IMAGE3, # 0 ~ 2
               ENEMY_IMAGE4, ENEMY_IMAGE5, ENEMY_IMAGE6, # 3 ~ 5
               ENEMY_IMAGE7, ENEMY_IMAGE8, ENEMY_IMAGE9] # 6 ~ 8
ENEMY_SCORE = {ENEMY_IMAGE1: 5, ENEMY_IMAGE2: 10, ENEMY_IMAGE3:5,
               ENEMY_IMAGE4: 7, ENEMY_IMAGE5: 8, ENEMY_IMAGE6: 10,
               ENEMY_IMAGE7: 10, ENEMY_IMAGE8: 9, ENEMY_IMAGE9: 15}

ENEMY_HP = {ENEMY_IMAGE1: 10, ENEMY_IMAGE2: 20, ENEMY_IMAGE3: 10,
            ENEMY_IMAGE4: 20, ENEMY_IMAGE5: 25, ENEMY_IMAGE6: 30,
            ENEMY_IMAGE7: 30, ENEMY_IMAGE8: 20, ENEMY_IMAGE9: 40}

BOSS_IMAGE = [BOSS_IMAGE_1, BOSS_IMAGE_2, BOSS_IMAGE_3]
BOSS_HP = {BOSS_IMAGE_1: 100, BOSS_IMAGE_2: 150, BOSS_IMAGE_3: 450}


class Enemy(pygame.sprite.Sprite):
    def __init__(self, round):
        pygame.sprite.Sprite.__init__(self)
        self.image = ENEMY_IMAGE[random.randint(round*3, 2+round*3)] # Round0 0~2 Round1 3~5 Round2 6~8
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * 0.85 / 2)
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)  # 掉下隨機水平位置
        self.rect.y = random.randrange(-100, -40)  # 掉下隨機垂直位置
        self.speedx = random.randrange(-3, 3)  # 掉下隨機水平速度(負值是讓他不會只往右邊)
        self.speedy = random.randrange(2, 3)  # 掉下隨機垂直速度
        self.enemyscore = ENEMY_SCORE[self.image]
        self.max_hp = ENEMY_HP[self.image]
        self.hp = self.max_hp

    def update(self):
        self.rect.y += self.speedy  # 更新(y座標更新垂直速度位置)
        self.rect.x += self.speedx  # 更新(x座標更新垂直速度位置)
        if self.rect.top > HEIGHT or self.rect.left > WIDTH or self.rect.right < 0:  # 如果超過高度、寬度則重製掉下(不超出邊界)
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(2, 10)
            self.speedx = random.randrange(-3, 3)


class Boss(pygame.sprite.Sprite):
    def __init__(self, round):
        pygame.sprite.Sprite.__init__(self)
        self.image = BOSS_IMAGE[round]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * 0.85 / 2)
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)  # 隨機水平位置
        self.rect.y = HEIGHT*1/4  # 掉下隨機垂直位置
        self.speedx = 3  # 掉下隨機水平速度
        self.max_hp = BOSS_HP[self.image]
        self.hp = self.max_hp

    def update(self):
        self.rect.x += self.speedx  # 更新(x座標更新垂直速度位置)
        if self.rect.right > WIDTH or self.rect.left < 0:
            self.speedx = -(self.speedx)
