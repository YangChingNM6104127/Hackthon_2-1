from enemy import *
from player import *
from item import *
from settings import *
from view import *
from control import *
from model import *
import time
import pygame
import os


# 匯入字型
font_name = os.path.join("font.ttf")
BACKGROUND_IMAGE = [BACKGROUND1_IMAGE, BACKGROUND2_IMAGE, BACKGROUND3_IMAGE]
NEXTROUND_IMAGE = [NEXTROUND1_IMAGE, NEXTROUND2_IMAGE]


class GameView():
    # 遊戲初始化 and 創建視窗
    def __init__(self, model, player):
        pygame.display.set_caption("還敢群聚啊")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.font_name = os.path.join("font.ttf")
        self.__model = model
        self.__player = player

    def main(self, round):
        # self.screen.fill(WHITE)
        # pygame.draw.rect(self.screen, WHITE, [0, 0, 500, 40])
        self.screen.blit(BACKGROUND_IMAGE[round], (0, 0))
        self.__model.all_sprites.draw(self.screen)

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, RED)
        text_rect = text_surface.get_rect()
        text_rect.centerx = x
        text_rect.top = y
        self.screen.blit(text_surface, text_rect)

    def round_alert(self, round):
        pygame.draw.rect(self.screen, WHITE, [0, 0, 500, 40])
        self.screen.blit(NEXTROUND_IMAGE[round-1], (0, HEIGHT*1/3))
        self.__model.all_sprites.draw(self.screen)

    # def draw_score(self):
    #     font = pygame.font.Font(self.font_name, 18)
    #     text_surface = font.render(str(self.__player.score), True, BLACK)
    #     text_rect = text_surface.get_rect()
    #     text_rect.centerx = WIDTH / 2
    #     text_rect.top = 10
    #     self.screen.blit(text_surface, text_rect)

    def draw_player_health(self):
        if self.__player.health < 0:
            self.__player.health = 0
        BAR_LENGTH = 100
        BAR_HEIGHT = 10
        x = 5
        y = 15
        fill = (self.__player.health / 100) * BAR_LENGTH
        outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
        fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
        pygame.draw.rect(self.screen, GREEN, fill_rect)
        pygame.draw.rect(self.screen, BLACK, outline_rect, 2)
    
    def draw_player_lives(self):
        x = WIDTH - 100
        y = 15
        for i in range(self.__player.lives):
            img_rect = PLAYER_MINI_IMAGE.get_rect()
            img_rect.x = x + 32 * i
            img_rect.y = y
            self.screen.blit(PLAYER_MINI_IMAGE, img_rect)

    def draw_boss_health(self):
        for i in self.__model.enemies:
            BAR_LENGTH = 70
            BAR_HEIGHT = 10
            fill = (i.hp / i.max_hp) * BAR_LENGTH
            if isinstance(i, Boss):
                outline_rect = pygame.Rect(i.rect.x+13, i.rect.y, BAR_LENGTH, BAR_HEIGHT)
                fill_rect = pygame.Rect(i.rect.x+13, i.rect.y, fill, BAR_HEIGHT)
            else:
                outline_rect = pygame.Rect(i.rect.x-5, i.rect.y, BAR_LENGTH, BAR_HEIGHT)
                fill_rect = pygame.Rect(i.rect.x-5, i.rect.y, fill, BAR_HEIGHT)
            pygame.draw.rect(self.screen, GREEN, fill_rect)
            pygame.draw.rect(self.screen, BLACK, outline_rect, 2)

    def draw_gameover(self):
        self.screen.fill(WHITE)
        self.draw_text("GameOver", 50, WIDTH / 2, HEIGHT / 2)

    def draw_gamepass(self):
        self.screen.fill(WHITE)
        self.screen.blit(GAMEPASS_IMAGE, (0, 150))