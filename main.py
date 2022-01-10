import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Denno Runner')
clock = pygame.time.Clock()

sky_surface = pygame.image.load('assets/graphics/sky.png')
ground_surface = pygame.image.load('assets/graphics/ground.png')


while True:
    # Draw and update all elementes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    
    pygame.display.update()
    clock.tick(60) 