import pygame
from sys import exit
from pygame.constants import K_SPACE

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = test_font.render(f'score: {current_time}', False, (64, 64, 64))
    score_rect = score_surface.get_rect(center = (400, 50))
    screen.blit(score_surface, score_rect)
    return current_time

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Pixel Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('assets/fonts/Pixeltype.ttf', 50)
game_active = True
start_time = 0
score = 0

sky_surface = pygame.image.load('assets/graphics/sky.png').convert()
ground_surface = pygame.image.load('assets/graphics/ground.png').convert()
# score_surface = test_font.render('My game', False, (64, 64, 64))
# score_rect = score_surface.get_rect(midtop = (int(screen.get_width() / 2), 50))

enemy_surface = pygame.image.load('assets/graphics/enemy.png').convert_alpha()
enemy_rect = enemy_surface.get_rect(topleft = (600, 250))

player_surface = pygame.image.load('assets/graphics/player/player_stand.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80, 300))
player_gravity = 0

# --- Intro Screen ---
player_stand = pygame.image.load('assets/graphics/player/player_stand.png').convert_alpha()
# player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand = pygame.transform.scale2x(player_stand)
player_stand_rect = player_stand.get_rect(center = (400, 200))

name_txt = test_font.render('Pixel Runner', False, (111, 196, 169))
name_txt_rect = name_txt.get_rect(center = (400, 50))

instruction_txt = test_font.render('Press Space to Start', False, (111, 196, 169))
instruction_txt_rect = instruction_txt.get_rect(center = (400, 350))

# Draw and update all elementes
while True:
    # --- EVENT LOOP ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom == 300:
                # if player_rect.collidepoint(event.pos): 
                player_gravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                enemy_rect.left = 805
                start_time = int(pygame.time.get_ticks() / 1000)

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        # pygame.draw.rect(screen, '#c0e8ec', score_rect)
        # pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
        # screen.blit(score_surface, score_rect)
        score = display_score()
        
        enemy_rect.x -= 5
        if enemy_rect.left < -100: enemy_rect.left = 805
        screen.blit(enemy_surface, enemy_rect)

        # --- Player ---
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(player_surface, player_rect)
        
        # --- Collision ---
        if enemy_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill((94, 129, 162))
        screen.blit(name_txt, name_txt_rect)
        screen.blit(player_stand, player_stand_rect)

        score_txt = test_font.render(f'Your Score: {score}', False, (111, 196, 169))
        score_txt_rect = score_txt.get_rect(center = (400, 350))
        if score == 0: screen.blit(instruction_txt, instruction_txt_rect)
        else: screen.blit(score_txt, score_txt_rect)

    pygame.display.update()
    clock.tick(60)
