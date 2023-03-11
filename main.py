import random
from os import listdir
import pygame
from pygame. constants import QUIT,  K_DOWN, K_UP, K_LEFT, K_RIGHT

FPS = pygame.time.Clock()
pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (34, 177, 76)
ball_color = WHITE

font = pygame.font.SysFont('Verdana', 20)

screen = width, height = 800,600
main_surface = pygame.display.set_mode(screen)
# ball = pygame.Surface((20, 20))
# ball.fill(ball_color)
IMGS_PATH = 'goose'
ball_imgs = [pygame.image.load(IMGS_PATH + '/' + file).convert_alpha() for file in listdir(IMGS_PATH)]
ball = ball_imgs[0]
# ball = pygame.image.load('player.png').convert_alpha()
bal_rect = ball.get_rect()
ball_speed = 10

def create_enemy():
    enemy = pygame.image.load('enemy.png').convert_alpha()
    # enemy = pygame.Surface((20, 20))
    # enemy.fill(RED)
    enemy_rect = pygame.Rect(width, random.randint(40, height-40), *enemy.get_size())
    enemy_speed = random.randint(2, 5)
    return [enemy, enemy_rect, enemy_speed]
CREATE_EMEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_EMEMY, 1500)

def create_bonus():
    bonus = pygame.image.load('bonus.png').convert_alpha()
    # bonus = pygame.Surface((20, 20))
    # bonus.fill(GREEN)
    bonus_rect = pygame.Rect(random.randint(100, width-200), 0, *bonus.get_size())
    bonus_speed = random.randint(1, 4)
    return [bonus, bonus_rect, bonus_speed]
CREATE_BONUS = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_BONUS, 1500)

CHANGE_IMG = pygame.USEREVENT + 3
pygame.time.set_timer(CHANGE_IMG, 125)

bg = pygame.transform.scale(pygame.image.load('background.png').convert(), screen)
bgX = 0
bgX2 = bg.get_width()
bg_speed = 3
img_index = 0
scores = 0
enemies = []
bonuses = []

is_working = True
while is_working:
    FPS.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
           is_working = False
        if event.type == CREATE_EMEMY:
            enemies.append(create_enemy())
        if event.type == CREATE_BONUS:
            bonuses.append(create_bonus())
        if event.type == CHANGE_IMG:
            img_index += 1
            if img_index == len(ball_imgs):
                img_index = 0
            ball = ball_imgs[img_index]
            
    pressed_keys = pygame.key.get_pressed()
    
    # main_surface.fill(WHITE)

    # main_surface.blit(bg, (0, 0))
    bgX -= bg_speed
    bgX2 -= bg_speed 

    if bgX < -bg.get_width():
       bgX = bg.get_width()
    if bgX2 < -bg.get_width():
       bgX2 = bg.get_width() 
        
    main_surface.blit(bg, (bgX, 0))
    main_surface.blit(bg, (bgX2, 0))


    main_surface.blit(ball, bal_rect)

    main_surface.blit(font.render(str(scores), True, BLACK), (width-30, 0))
    for enemy in enemies:
        enemy[1] = enemy[1].move(-enemy[2], 0)
        main_surface.blit(enemy[0], enemy[1])
        if  enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))
        if bal_rect.colliderect(enemy[1]):
           is_working = False

    for bonus in bonuses:
        bonus[1] = bonus[1].move(0, bonus[2])
        main_surface.blit(bonus[0], bonus[1])
        if  bonus[1].bottom > height:
            bonuses.pop(bonuses.index(bonus))
        if bal_rect.colliderect(bonus[1]):
            bonuses.pop(bonuses.index(bonus))
            scores = scores + 1

    if pressed_keys[K_DOWN] and bal_rect.bottom <= height:
        bal_rect = bal_rect.move((0, ball_speed))
    if pressed_keys[K_UP] and bal_rect.top >= 0:
        bal_rect = bal_rect.move((0, -ball_speed))
    if pressed_keys[K_RIGHT] and bal_rect.right <= width:
        bal_rect = bal_rect.move((ball_speed, 0))
    if pressed_keys[K_LEFT] and bal_rect.left >= 0:
        bal_rect = bal_rect.move((-ball_speed, 0))
    
    
    # print(len(bonuses))

   # enemy_rect = enemy_rect.move(-enemy_speed, 0)
    # ball.fill(ball_color)
    pygame.display.flip()

