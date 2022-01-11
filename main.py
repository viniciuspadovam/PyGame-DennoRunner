import pygame
from random import randint
from sys import exit
from pygame.constants import K_SPACE

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = test_font.render(f'score: {current_time}', False, (64, 64, 64))
    score_rect = score_surface.get_rect(center = (400, 50))
    screen.blit(score_surface, score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300: screen.blit(chicken_surface, obstacle_rect)
            else: screen.blit(bullet_surface, obstacle_rect)
        
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    else: return []

def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): return False
    return True

def player_animation():
    global player_surface, player_index

    if player_rect.bottom < 300:
        player_surface = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk): player_index = 0
        player_surface = player_walk[int(player_index)]

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Pixel Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('assets/fonts/Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0

sky_surface = pygame.image.load('assets/graphics/sky.png').convert()
ground_surface = pygame.image.load('assets/graphics/ground.png').convert()
# score_surface = test_font.render('My game', False, (64, 64, 64))
# score_rect = score_surface.get_rect(midtop = (int(screen.get_width() / 2), 50))

# --- Chicken ---
chicken_frame_1 = pygame.image.load('assets/graphics/Chicken/chicken1.png').convert_alpha()
chicken_frame_2 = pygame.image.load('assets/graphics/Chicken/chicken2.png').convert_alpha()
chicken_frame_3 = pygame.image.load('assets/graphics/Chicken/chicken3.png').convert_alpha()
chicken_frames = [chicken_frame_1, chicken_frame_2, chicken_frame_3]
chicken_frame_index = 0
chicken_surface = chicken_frames[chicken_frame_index]

# --- Bullet ---
bullet_frame_1 = pygame.image.load('assets/graphics/Bullet/bullet_1.png').convert_alpha()
bullet_frame_2 = pygame.image.load('assets/graphics/Bullet/bullet_2.png').convert_alpha()
bullet_frame_3 = pygame.image.load('assets/graphics/Bullet/bullet_3.png').convert_alpha()
bullet_frames = [bullet_frame_1, bullet_frame_2, bullet_frame_3]
bullet_frame_index = 0
bullet_surface = bullet_frames[bullet_frame_index]

obstacle_rect_list = []

# --- Player ---
player_walk_1 = pygame.image.load('assets/graphics/player/player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load('assets/graphics/player/player_walk_2.png').convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_jump = pygame.image.load('assets/graphics/player/player_jump.png').convert_alpha()

player_surface = player_walk[player_index]
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

# --- Timer ---
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

chicken_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(chicken_animation_timer, 180)

bullet_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(bullet_animation_timer, 380)


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
            
            if event.type == obstacle_timer:
                if randint(0, 2):
                    obstacle_rect_list.append(chicken_surface.get_rect(bottomleft = (randint(900, 1100), 300)))
                else:
                    obstacle_rect_list.append(bullet_surface.get_rect(bottomleft = (randint(900, 1100), 150)))

            if event.type == chicken_animation_timer:
                if chicken_frame_index == 0: chicken_frame_index = 1
                elif chicken_frame_index == 1: chicken_frame_index = 2
                else: chicken_frame_index = 0
                chicken_surface = chicken_frames[chicken_frame_index]

            if event.type == bullet_animation_timer:
                if bullet_frame_index == 0: bullet_frame_index = 1
                elif bullet_frame_index == 1: bullet_frame_index = 2
                else: bullet_frame_index = 0
                bullet_surface = bullet_frames[bullet_frame_index]

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        # pygame.draw.rect(screen, '#c0e8ec', score_rect)
        # pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
        # screen.blit(score_surface, score_rect)
        score = display_score()
        
        # enemy_rect.x -= 5
        # if enemy_rect.left < -100: enemy_rect.left = 805
        # screen.blit(bullet_surface, enemy_rect)

        # --- Player ---
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300
        player_animation()
        screen.blit(player_surface, player_rect)

        # --- Enemy Movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # --- Collisions ---
        game_active = collisions(player_rect, obstacle_rect_list)
        
    else:
        screen.fill((94, 129, 162))
        screen.blit(name_txt, name_txt_rect)
        screen.blit(player_stand, player_stand_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80, 300)
        player_gravity = 0

        score_txt = test_font.render(f'Your Score: {score}', False, (111, 196, 169))
        score_txt_rect = score_txt.get_rect(center = (400, 350))
        if score == 0: screen.blit(instruction_txt, instruction_txt_rect)
        else: screen.blit(score_txt, score_txt_rect)

    pygame.display.update()
    clock.tick(60)
