import pygame
import time
import random
from pygame.locals import *
from gamestate import GameState

pygame.font.init()
pygame.init()

WIDTH, HEIGHT = 1000, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space dodge")

BGI = pygame.image.load("bg03.png")
BG = pygame.transform.scale(BGI, (WIDTH, HEIGHT))

Player_W = 100
Player_H = 120

player_image = pygame.image.load("space-ship1.png")
player_image = pygame.transform.scale(player_image, (100, 130))

asteroid_image = pygame.image.load("meteorite1.png").convert_alpha()
asteroid_image = pygame.transform.scale(asteroid_image, (70, 70))

PLAYER_VEL = 16
STAR_WIDTH = 20
STAR_HEIGHT = 30
STAR_VEL = 14

FONT = pygame.font.SysFont("comicsans", 30)

def draw(player, elapsed_time, stars, lives):
    WINDOW.blit(BG, (0, 0))

    player_image_x = player.x + (Player_W - player_image.get_width()) // 2
    player_image_y = player.y + (Player_H - player_image.get_height()) // 2

    WINDOW.blit(player_image, (player_image_x, player_image_y))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WINDOW.blit(time_text, (10, 10))

    lives_text = FONT.render(f"Lives left: {lives}", 1, "white")
    WINDOW.blit(lives_text, (10, 40))

    for star in stars:
        WINDOW.blit(asteroid_image, star)

    pygame.display.update()

def draw_menu():
    WINDOW.blit(BG, (0, 0))
    play_image = pygame.image.load("start.png").convert_alpha()
    play_image = pygame.transform.scale(play_image, (150, 130))
    play_button = play_image.get_rect(center=(WIDTH/2, HEIGHT/2))
    WINDOW.blit(play_image, play_button)
    quit_image = pygame.image.load("quit.png").convert_alpha()
    quit_image = pygame.transform.scale(quit_image, (100, 100))
    quit_button = quit_image.get_rect(center=(WIDTH/2, HEIGHT/2 + 100))
    WINDOW.blit(quit_image, quit_button)
    pygame.display.update()
    
def draw_youlost():
    lost_text = FONT.render("You Lost!", 1, "white")
    WINDOW.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
    pygame.display.update()

def draw_level_completed():
    level_completed_text = FONT.render("Level completed!", 1, "white")
    WINDOW.blit(level_completed_text, (WIDTH/2 - level_completed_text.get_width()/2, HEIGHT/2 - level_completed_text.get_height()/2))
    pygame.display.update()

def main():
    player = pygame.Rect(200, HEIGHT - Player_H, Player_W, Player_H)
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0
    LEVEL = 1
    LIVES = 3
    
    star_add_increment = 1000
    star_count = 0

    stars = []
    hit = False
    transition_start_time = 0
    game_state = GameState.MENU
    a = True
    while a:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        if game_state == GameState.MENU:
            draw_menu()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    play_button = pygame.Rect(WIDTH/2 - 75, HEIGHT/2 - 65, 150, 130)
                    quit_button = pygame.Rect(WIDTH/2 - 50, HEIGHT/2 + 35, 100, 100)
                    if play_button.collidepoint(mouse_pos):
                        game_state = GameState.PLAYING
                    if quit_button.collidepoint(mouse_pos):
                        pygame.quit()
                        return

        elif game_state == GameState.PLAYING:
            clock.tick(60)

            star_count += clock.get_rawtime()
            elapsed_time = time.time() - start_time

            if star_count > star_add_increment:
                for _ in range(3):
                    star_x = random.randint(0, WIDTH - STAR_WIDTH)
                    star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                    stars.append(star)

                star_add_increment = max(200, star_add_increment - 50)
                star_count = 0

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
                player.x -= PLAYER_VEL
            if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
                player.x += PLAYER_VEL

            for star in stars[:]:
                star.y += STAR_VEL
                if star.y > HEIGHT:
                    stars.remove(star)
                elif player.colliderect(star):
                    stars.remove(star)
                    hit = True
                    break

            if hit:
                game_state = GameState.TRANSITION
                transition_start_time = time.time()
                LIVES -= 1
                if LIVES <= 0:
                    game_state = GameState.MENU

            if elapsed_time >= LEVEL * 10:
                game_state = GameState.LEVEL_COMPLETED

            draw(player, elapsed_time, stars, LIVES)

        if game_state == GameState.TRANSITION:
            elapsed_transition_time = time.time() - transition_start_time
            if elapsed_transition_time >= 3: 
                if LIVES <= 0:
                    game_state = GameState.MENU
                else:
                    game_state = GameState.PLAYING
                    hit = False
                    player.x = 200
                    player.y = HEIGHT - Player_H
                    stars.clear()
                    start_time = time.time()
                    elapsed_time = 0

        if game_state == GameState.LEVEL_COMPLETED:
            draw_level_completed()
            elapsed_transition_time = time.time() - transition_start_time
            if elapsed_transition_time >= 3:
                game_state = GameState.MENU

if __name__ == "__main__":
    main()
