import pygame
from random import randint, choice
from sys import exit
from pygame.constants import K_SPACE

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load('assets/graphics/player/player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load('assets/graphics/player/player_walk_2.png').convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load('assets/graphics/player/player_jump.png').convert_alpha()

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80, 300))
        self.gravity = 0
    
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20

    def aplly_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk): self.player_index = 0
            self.image = self.player_walk[int(self.player_index)] 

    def update(self):
        self.player_input()
        self.aplly_gravity()
        self.animation_state()

class Obstacles(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == 'chicken':
            chicken_1 = pygame.image.load('assets/graphics/Chicken/chicken1.png').convert_alpha()
            chicken_2 = pygame.image.load('assets/graphics/Chicken/chicken2.png').convert_alpha()
            chicken_3 = pygame.image.load('assets/graphics/Chicken/chicken3.png').convert_alpha()
            self.frames = [chicken_1, chicken_2, chicken_3]
            y_pos = 300
        else:
            bullet_1 = pygame.image.load('assets/graphics/Bullet/bullet_1.png').convert_alpha()
            bullet_2 = pygame.image.load('assets/graphics/Bullet/bullet_2.png').convert_alpha()
            bullet_3 = pygame.image.load('assets/graphics/Bullet/bullet_3.png').convert_alpha()
            self.frames = [bullet_1, bullet_2, bullet_3]
            y_pos = 150

        self.animation_index = 0

        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900, 1100), y_pos))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames): self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100: self.kill()

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = test_font.render(f'score: {current_time}', False, (64, 64, 64))
    score_rect = score_surface.get_rect(center = (400, 50))
    screen.blit(score_surface, score_rect)
    return current_time

def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        return False
    else: return True

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Pixel Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('assets/fonts/Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0

# --- Groups ---
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()

sky_surface = pygame.image.load('assets/graphics/sky.png').convert()
ground_surface = pygame.image.load('assets/graphics/ground.png').convert()

# --- Intro Screen ---
player_stand = pygame.image.load('assets/graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.scale2x(player_stand)
player_stand_rect = player_stand.get_rect(center = (400, 200))

name_txt = test_font.render('Pixel Runner', False, (111, 196, 169))
name_txt_rect = name_txt.get_rect(center = (400, 50))

instruction_txt = test_font.render('Press Space to Start', False, (111, 196, 169))
instruction_txt_rect = instruction_txt.get_rect(center = (400, 350))

# --- Timer ---
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

# Draw and update all elementes
while True:
    # --- EVENT LOOP ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacles(choice(['chicken', 'chicken', 'chicken', 'bullet'])))
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))

        score = display_score()

        player.draw(screen)
        player.update()

        obstacle_group.draw(screen)
        obstacle_group.update()

        # --- Collisions ---
        game_active = collision_sprite()
        
    else:
        screen.fill((94, 129, 162))
        screen.blit(name_txt, name_txt_rect)
        screen.blit(player_stand, player_stand_rect)
        player_gravity = 0

        score_txt = test_font.render(f'Your Score: {score}', False, (111, 196, 169))
        score_txt_rect = score_txt.get_rect(center = (400, 350))
        if score == 0: screen.blit(instruction_txt, instruction_txt_rect)
        else: screen.blit(score_txt, score_txt_rect)

    pygame.display.update()
    clock.tick(60)
