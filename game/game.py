import pygame
import random
#pylint: disable=no-member

pygame.init()

screen = pygame.display.set_mode((800, 600))

backgroundImage = pygame.image.load("week9/background1.jpg")

done = False

playerImage = pygame.image.load("week9/player.png")
player_x = 400
player_y = 500

enemyImage = pygame.image.load("week9/enemy.png")
enemy_x = random.randint(0, 736)
enemy_y = random.randint(20, 50)
enemy_dx = 5
enemy_dy = 30

bulletImage = pygame.image.load("week9/bullet.png")
bullet_x = 420
bullet_y = 470
bullet_dx = 0
bullet_dy = 10
bul_pos = 0

def player(x, y):
    screen.blit(playerImage, (x, y))

def enemy(x, y):
    screen.blit(enemyImage, (x, y))

def background():
    screen.blit(backgroundImage, (0, 0))

def bullet(x, y):
    screen.blit(bulletImage, (x, y))

def collision(enemy_x, enemy_y, bullet_x, bullet_y):
    if bullet_x >= enemy_x and bullet_x <= enemy_x + 64 and bullet_y <= enemy_y + 64:
            return True
    return False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_LEFT]: player_x -= 3
    if pressed[pygame.K_RIGHT]: player_x += 3

    enemy_x += enemy_dx
    if enemy_x < 0 or enemy_x > 736:
        enemy_dx = -enemy_dx
        enemy_y += enemy_dy

    bullet_x = player_x + 20

    if bullet_x == player_x + 20 and bullet_y == 470:
        pos_pl_x = player_x

    if pressed[pygame.K_SPACE]: 
        bullet_x = pos_pl_x + 20
        bul_pos = bullet_y
        
    if bul_pos > 0:
        bullet_x = pos_pl_x + 20
        bullet_y -= bullet_dy

    if bullet_y == 0:
        bullet_dy = 0
        bullet_x = player_x + 20
        bullet_y = 470

    if pressed[pygame.K_SPACE]:
        bullet_dy = 5
        bullet_x = pos_pl_x + 20
        bullet_y -= bullet_dy

    coll = collision(enemy_x, enemy_y, bullet_x, bullet_y)
    if coll and bullet_y < 470:
        enemy_x = random.randint(0, 736)
        enemy_y = random.randint(20, 50)
        bullet_dy = 0
        bullet_x = player_x + 20

    screen.blit(backgroundImage, (0, 0))
    player(player_x, player_y)
    enemy(enemy_x, enemy_y)
    bullet(bullet_x, bullet_y)
    pygame.display.flip()