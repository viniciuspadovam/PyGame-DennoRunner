import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Denno Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('assets/fonts/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('assets/graphics/sky.png').convert()
ground_surface = pygame.image.load('assets/graphics/ground.png').convert()
score_surface = test_font.render('My game', False, (64, 64, 64))
score_rect = score_surface.get_rect(midtop = (int(screen.get_width() / 2), 50))

enemy_surface = pygame.image.load('assets/graphics/enemy.png').convert_alpha()
enemy_rect = enemy_surface.get_rect(topleft = (600, 250))

player_surface = pygame.image.load('assets/graphics/player/player_stand.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80, 300))

# Draw and update all elementes
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos): print('collision')

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    pygame.draw.rect(screen, '#c0e8ec', score_rect)
    pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
    screen.blit(score_surface, score_rect)
    
    enemy_rect.x -= 3
    if enemy_rect.left < -100: enemy_rect.left = 805
    screen.blit(enemy_surface, enemy_rect)

    screen.blit(player_surface, player_rect)

    # if player_rect.colliderect(enemy_rect):
    #     print('collision')

    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     print('collision')
    
    pygame.display.update()
    clock.tick(60)
