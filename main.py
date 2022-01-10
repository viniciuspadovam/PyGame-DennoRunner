import pygame
from sys import exit, pycache_prefix
from pygame.constants import K_SPACE

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
player_gravity = 0

# Draw and update all elementes
while True:
    # --- EVENT LOOP ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom == 300:
            # if player_rect.collidepoint(event.pos): 
            player_gravity = -20
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                player_gravity = -20

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    pygame.draw.rect(screen, '#c0e8ec', score_rect)
    pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
    screen.blit(score_surface, score_rect)
    
    enemy_rect.x -= 3
    if enemy_rect.left < -100: enemy_rect.left = 805
    screen.blit(enemy_surface, enemy_rect)

    # --- Player ---
    player_gravity += 1
    player_rect.y += player_gravity
    if player_rect.bottom >= 300: player_rect.bottom = 300
    screen.blit(player_surface, player_rect)
    
    pygame.display.update()
    clock.tick(60)
