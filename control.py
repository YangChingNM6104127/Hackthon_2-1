import os
import pygame
from enemy import *
from player import *
from item import *
from settings import *
from view import *
from model import *


class Control():
    def __init__(self, model, player):
        self.__model = model
        self.__player = player
        self.running = True
        self.next_round = False
        self.round = 0
        # self.__item = item

    def generate_enemy(self, number = 1):
        for i in range (number):
            e = Enemy(self.round)
            self.__model.enemies.add(e)
            self.__model.all_sprites.add(e)

    def generate_boss(self):
        if self.__player.score >= 100:
            b = Boss(self.round)
            self.__model.enemies.add(b)
            self.__model.all_sprites.add(b)
            self.__player.score_cold = True
            self.__player.score = 0

    def generate_item(self):
        if self.__player.kill_count == 5:
            i = Items()
            self.__model.items.add(i)
            self.__model.all_sprites.add(i)
            self.__player.kill_count = 0

    def collider_eb(self):
        hits = pygame.sprite.groupcollide(self.__model.enemies, self.__model.bullets, False, pygame.sprite.collide_circle)
        for hit in hits:
            if hit.hp - self.__player.damage <= 0:
                if isinstance(hit, Boss):
                    self.__player.killed_boss = True
                if not self.__player.score_cold:
                    self.score_add(hit.enemyscore)
                self.__player.kill_count += 1
                self.__model.enemies.remove(hit)
                self.__model.all_sprites.remove(hit)
                self.generate_enemy()
            else:
                hit.hp -= self.__player.damage
    
    def collider_ep(self):
        hits = pygame.sprite.spritecollide(self.__player, self.__model.enemies, True, pygame.sprite.collide_circle)
        # Spite VS Group
        for hit in hits:
            self.generate_enemy()
            self.player_state(hit)

    def collider_pi(self):
        hits = pygame.sprite.spritecollide(self.__player, self.__model.items, True)
        for h in hits:
            if h.image == GUN_IMAGE:
                h.gunup(self.__player)
            elif h.image == VACCINE_IMAGE:
                h.health_recover(self.__player)
            elif h.image == MASK_IMAGE:
                h.attackbuff(self.__player)
    
    def player_state(self, hit):
        self.__player.health -= hit.radius * 2
        if self.__player.health <= 0:
            self.__player.lives -= 1
            self.__player.health = 100
            self.__player.hide()
    
    def score_add(self, enemyscore):
        self.__player.score += enemyscore

    def change_round(self):
        if self.round == 2 and self.__player.killed_boss == True:
            return False, False, True
        elif self.__player.killed_boss:
            running = False
            round_alert = True
            self.round += 1
            self.__model.bullets.empty()
            self.__model.enemies.empty()
            self.__model.all_sprites.empty()
            self.__model.all_sprites.add(self.__player)
            self.__player.killed_boss = False
            self.__player.score_cold = False
            self.generate_enemy(6)
            return False, True, False
        return True, False, False

    def game_pass(self):
        if self.round == 3:
            return False, True
        return True, False