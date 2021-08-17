from view import *
from control import *
from model import *
from player import *
from item import *
from settings import *
from enemy import *
from homepage import *
import pygame
import os
import time

class Game:
    def __init__(self):
        self.running = True
        self.round_alert = False
        self.passed = False
        self.dead = False

    def run(self):
        # initialization
        pygame.init()
        model = Model()
        player = Player()
        control = Control(model, player)
        game_view = GameView(model, player)

        model.all_sprites.add(player)
        control.generate_enemy(5)

        quit_game = False          
        while not quit_game:
            if self.running:
                # game_view.clock.tick(FPS)
                pygame.time.Clock().tick(FPS)
                # 取得輸入
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            player.shoot(model)

                # 判斷是否進入下一關
                self.running, self.round_alert, self.passed  = control.change_round()

                # 生成 Boss
                control.generate_boss()

                # 更新遊戲
                model.all_sprites.update()

                # 判斷敵人 子彈相撞
                control.collider_eb()

                # 判斷敵人 玩家相撞
                control.collider_ep()

                # 生成道具
                control.generate_item()

                # 判斷道具 玩家相撞
                control.collider_pi()

                # 死掉
                if player.lives == 0:
                    self.dead = True
                    self.running = False

                now = pygame.time.get_ticks()
                game_view.main(control.round)
                game_view.draw_player_health()
                game_view.draw_boss_health()
                game_view.draw_player_lives()
            elif self.round_alert:
                if pygame.time.get_ticks() - now > 5000:
                    self.running = True
                    self.round_alert = False
                else:
                    game_view.round_alert(control.round)
            elif self.passed:
                if pygame.time.get_ticks() - now > 3000:
                    quit_game = True
                else:
                    game_view.draw_gamepass()
            elif self.dead:
                if pygame.time.get_ticks() - now > 3000:
                    quit_game = True
                else:
                    game_view.draw_gameover()

            pygame.display.update()

        # pygame.quit()