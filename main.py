import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Denno Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('assets/fonts/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('assets/graphics/sky.png').convert()
ground_surface = pygame.image.load('assets/graphics/ground.png').convert()
text_surface = test_font.render('My game', False, 'Black').convert()

enemy_surface = pygame.image.load('assets/graphics/enemy.png').convert_alpha()
enemy_rect = enemy_surface.get_rect(topleft = (600, 250))

player_surface = pygame.image.load('assets/graphics/player/player_stand.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80, 300))

while True:
    # Draw and update all elementes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))
    enemy_rect.x -= 3
    if enemy_rect.left < -100: enemy_rect.left = 805
    screen.blit(enemy_surface, enemy_rect)
    screen.blit(player_surface, player_rect)

    if player_rect.colliderect(enemy_rect):
        print('collision')
    
    pygame.display.update()
    clock.tick(60)
