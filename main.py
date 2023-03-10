import pygame
from pygame. constants import QUIT

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 162, 232)
ball_color = WHITE
pygame.init()
screen = width, height = 800,600
main_surface = pygame.display.set_mode(screen)
ball = pygame.Surface((20, 20))
ball.fill(ball_color)
bal_rect = ball.get_rect()
ball_speed = [1, 1]
change_color = False
is_working = True

while is_working:
    for event in pygame.event.get():
        if event.type == QUIT:
           is_working = False
    bal_rect = bal_rect.move(ball_speed)
    if bal_rect.bottom >= height or bal_rect.top <=0:
        ball_speed [1] = - ball_speed[1]
        change_color = True
        
    if bal_rect.right >= width or bal_rect.left <ё=0:
        ball_speed [0] = - ball_speed[0]
        change_color = True
    if change_color: 
        change_color = False
        if ball_color == BLUE:
            ball_color = WHITE
        else:
            ball_color = BLUE
    main_surface.fill(BLACK)
    main_surface.blit(ball, bal_rect)
    ball.fill(ball_color)
    pygame.display.flip()

