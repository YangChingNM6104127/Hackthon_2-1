from settings import *
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(PLAYER_IMAGE, (50, 50))
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect()
        self.radius = 20
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 8
        self.health = 100
        self.lives = 3
        self.hidden = False
        self.hide_time = 0
        self.gun = 1
        self.gun_time = 0
        self.score = 0
        self.killed_boss = False
        self.score_cold = False
        self.damage = 10
        self.kill_count = 0

    def update(self):
        if self.hidden and pygame.time.get_ticks() - self.hide_time > 1000:
            self.hidden = False
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT - 10

        now = pygame.time.get_ticks()
        if self.gun > 1 and now - self.gun_time > 5000:
            self.gun -= 1
            self.gun_time = now

        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            self.rect.x += self.speedx
        if key_pressed[pygame.K_LEFT]:
            self.rect.x -= self.speedx

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self, model):    # all_sprite為Argument, 這邊從主程式傳進來後，可開始射擊
        if not (self.hidden):
            if self.gun == 1:
                bullet = Bullet(self.rect.centerx, self.rect.top)           # 一開始只有一顆子彈，發射位置
                model.all_sprites.add(bullet)                                      # add回去那個all_sprites才能顯示出來
                model.bullets.add(bullet)
            elif self.gun >= 2:                                             # 吃到道具會讓射擊子彈變兩顆self.gun會變成2
                bullet1 = Bullet(self.rect.left, self.rect.centery)         # 2顆子彈發射的位置A
                bullet2 = Bullet(self.rect.right, self.rect.centery)        # 2顆子彈發射的位置B
                model.all_sprites.add(bullet1)
                model.all_sprites.add(bullet2)
                model.bullets.add(bullet1)
                model.bullets.add(bullet2)

    def hide(self):
        self.hidden = True
        self.hide_time = pygame.time.get_ticks()
        self.rect.center = (WIDTH / 2, HEIGHT + 500)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(BULLET_IMAGE, (8, 30))
        # self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -10         # 速度10往上飛

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()