import pygame
import os

# Screen Size
WIDTH = 500
HEIGHT = 600
# Frame Rate
FPS = 60
# Color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
IronGray = (98, 91, 87)
Blue = (137, 207, 240)
PapayaWhip = (253, 245, 230)

# 圖片輸入-背景
BACKGROUND0_IMAGE = pygame.image.load(os.path.join("image", "background0.png"))
BACKGROUND0_IMAGE = pygame.transform.scale(BACKGROUND0_IMAGE, (WIDTH, HEIGHT))
BACKGROUND1_IMAGE = pygame.image.load(os.path.join("image", "background1.png"))
BACKGROUND1_IMAGE = pygame.transform.scale(BACKGROUND1_IMAGE, (WIDTH, HEIGHT))
BACKGROUND2_IMAGE = pygame.image.load(os.path.join("image", "background2.png"))
BACKGROUND2_IMAGE = pygame.transform.scale(BACKGROUND2_IMAGE, (WIDTH, HEIGHT))
BACKGROUND3_IMAGE = pygame.image.load(os.path.join("image", "background3.jpg"))
BACKGROUND3_IMAGE = pygame.transform.scale(BACKGROUND3_IMAGE, (WIDTH, HEIGHT))
# 圖片輸入-子彈
BULLET_IMAGE = pygame.image.load(os.path.join("image", "bullet.png"))
# 圖片輸入-玩家
PLAYER_IMAGE = pygame.image.load(os.path.join("image", "police.png"))    # 用來顯示剩餘復活次數
PLAYER_MINI_IMAGE = pygame.transform.scale(PLAYER_IMAGE, (25, 25))       # 標示小圖案
# 圖片輸入-敵人
ENEMY_IMAGE1 = pygame.image.load(os.path.join("image", "eating.png"))
ENEMY_IMAGE1 = pygame.transform.scale(ENEMY_IMAGE1, (60, 60))
ENEMY_IMAGE2 = pygame.image.load(os.path.join("image", "people2.png"))
ENEMY_IMAGE2 = pygame.transform.scale(ENEMY_IMAGE2, (60, 60))
ENEMY_IMAGE3 = pygame.image.load(os.path.join("image", "Mahjong.png"))
ENEMY_IMAGE3 = pygame.transform.scale(ENEMY_IMAGE3, (60, 60))

ENEMY_IMAGE4 = pygame.image.load(os.path.join("image", "travel.png"))
ENEMY_IMAGE4 = pygame.transform.scale(ENEMY_IMAGE4, (60, 60))
ENEMY_IMAGE5 = pygame.image.load(os.path.join("image", "train.png"))
ENEMY_IMAGE5 = pygame.transform.scale(ENEMY_IMAGE5, (60, 60))
ENEMY_IMAGE6 = pygame.image.load(os.path.join("image", "airplane.png"))
ENEMY_IMAGE6 = pygame.transform.scale(ENEMY_IMAGE6, (60, 60))

ENEMY_IMAGE7 = pygame.image.load(os.path.join("image", "drug1.png"))
ENEMY_IMAGE7 = pygame.transform.scale(ENEMY_IMAGE7, (60, 60))
ENEMY_IMAGE8 = pygame.image.load(os.path.join("image", "drug2.png"))
ENEMY_IMAGE8 = pygame.transform.scale(ENEMY_IMAGE8, (60, 60))
ENEMY_IMAGE9 = pygame.image.load(os.path.join("image", "drug3.png"))
ENEMY_IMAGE9 = pygame.transform.scale(ENEMY_IMAGE9, (60, 60))

# 圖片輸入-BOSS
BOSS_IMAGE_1 = pygame.image.load(os.path.join("image", "boss1.png"))
BOSS_IMAGE_1 = pygame.transform.scale(BOSS_IMAGE_1, (100, 100))
BOSS_IMAGE_2 = pygame.image.load(os.path.join("image", "boss2.jpg"))
BOSS_IMAGE_2 = pygame.transform.scale(BOSS_IMAGE_2, (100, 100))
BOSS_IMAGE_3 = pygame.image.load(os.path.join("image", "boss3.jpg"))
BOSS_IMAGE_3 = pygame.transform.scale(BOSS_IMAGE_3, (100, 100))

# 圖片輸入-道具
GUN_IMAGE = pygame.image.load(os.path.join("image", "gun.png"))
GUN_IMAGE = pygame.transform.scale(GUN_IMAGE, (30, 30))
VACCINE_IMAGE = pygame.image.load(os.path.join("image", "vaccine.png"))
VACCINE_IMAGE = pygame.transform.scale(VACCINE_IMAGE, (30, 30))
MASK_IMAGE = pygame.image.load(os.path.join("image", "mask.png"))
MASK_IMAGE = pygame.transform.scale(MASK_IMAGE, (30, 30))

# 圖片輸入-Boss

# 圖片輸入-NextRound
NEXTROUND1_IMAGE = pygame.image.load(os.path.join("image", "warning1.png"))
NEXTROUND1_IMAGE = pygame.transform.scale(NEXTROUND1_IMAGE, (WIDTH, 150))
NEXTROUND2_IMAGE = pygame.image.load(os.path.join("image", "warning2.png"))
NEXTROUND2_IMAGE = pygame.transform.scale(NEXTROUND2_IMAGE, (WIDTH, 150))


GAMEOVER_IMAGE = pygame.image.load(os.path.join("image", "warning3.png"))
GAMEOVER_IMAGE = pygame.transform.scale(GAMEOVER_IMAGE, (WIDTH, 150))

GAMEPASS_IMAGE = pygame.image.load(os.path.join("image", "pass.jpeg"))
GAMEPASS_IMAGE = pygame.transform.scale(GAMEPASS_IMAGE, (500, 300))