import pygame
import os
from settings import *
from control import *
from game import *
from view import *

pygame.init()


class Homepage():
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

    def run(self): 
        run = True
        clock = pygame.time.Clock()
        self.screen.blit(BACKGROUND0_IMAGE,(0,0))
        self.draw_text(self.screen, '還敢群聚阿', 64, WIDTH / 2, HEIGHT / 4)
        self.draw_text(self.screen, '← →移動警察 使用空白鍵發射子彈', 22, WIDTH / 2, HEIGHT / 2)
        self.draw_text(self.screen, '按任意鍵開始遊戲!', 18, WIDTH / 2, HEIGHT * 3 / 4)
        # self.play_music()
        while run:
            clock.tick(FPS)
            # 取得輸入
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYUP:
                    game = Game()
                    game.run()
                    run = False
            pygame.display.update()
        pygame.quit()

    def draw_text(self, surf, text, size, x, y):
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, BLACK)
        text_rect = text_surface.get_rect()
        text_rect.centerx = x
        text_rect.top = y
        surf.blit(text_surface, text_rect)
