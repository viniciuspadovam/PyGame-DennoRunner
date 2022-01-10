import pygame
from sys import builtin_module_names, exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Denno Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('assets/fonts/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('assets/graphics/sky.png')
ground_surface = pygame.image.load('assets/graphics/ground.png')
text_surface = test_font.render('My game', False, 'Black')

bullet_enemy_surface = pygame.image.load('assets/graphics/enemy.png')
bullet_x_pos = 600
while True:
    # Draw and update all elementes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))
    bullet_x_pos -= 3
    if bullet_x_pos < -100:
        bullet_x_pos = 805
    screen.blit(bullet_enemy_surface, (bullet_x_pos, 250))
    
    pygame.display.update()
    clock.tick(60) 