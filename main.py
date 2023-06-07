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

BGI2 = pygame.image.load("BG2.png")
BG2 = pygame.transform.scale(BGI2, (WIDTH, HEIGHT))

Player_W = 100
Player_H = 120

player_image = pygame.image.load("space-ship1.png")
player_image = pygame.transform.scale(player_image, (100, 130))

LEVEL = 1

unlocked_ships = [1]

asteroid_image = pygame.image.load("meteorite1.png").convert_alpha()
asteroid_image = pygame.transform.scale(asteroid_image, (70, 70))

PLAYER_VEL = 20
STAR_WIDTH = 20
STAR_HEIGHT = 30
STAR_VEL = 18

FONT = pygame.font.SysFont("comicsans", 30)

def draw(player, elapsed_time, stars, lives, choice):
    WINDOW.blit(BG, (0, 0))
    if choice == 1:
        player_image = pygame.image.load("space-ship1.png")
        player_image = pygame.transform.scale(player_image, (100, 120))
        player_image_x = player.x + (Player_W - player_image.get_width()) // 2
        player_image_y = player.y + (Player_H - player_image.get_height()) // 2

        WINDOW.blit(player_image, (player_image_x, player_image_y))
    if choice == 2:
        player_image = pygame.image.load("spaceship2.png")
        player_image = pygame.transform.scale(player_image, (100, 120))
        player_image_x = player.x + (Player_W - player_image.get_width()) // 2
        player_image_y = player.y + (Player_H - player_image.get_height()) // 2

        WINDOW.blit(player_image, (player_image_x, player_image_y))
    if choice == 3:
        player_image = pygame.image.load("space-ship3.png")
        player_image = pygame.transform.scale(player_image, (100, 120))
        player_image_x = player.x + (Player_W - player_image.get_width()) // 2
        player_image_y = player.y + (Player_H - player_image.get_height()) // 2

        WINDOW.blit(player_image, (player_image_x, player_image_y))
    if choice == 4:
        player_image = pygame.image.load("spaceship4.png")
        player_image = pygame.transform.scale(player_image, (100, 120))     
        player_image_x = player.x + (Player_W - player_image.get_width()) // 2
        player_image_y = player.y + (Player_H - player_image.get_height()) // 2

        WINDOW.blit(player_image, (player_image_x, player_image_y))
    if choice == 5:
        player_image = pygame.image.load("spaceship5.png")
        player_image = pygame.transform.scale(player_image, (100, 120))
        player_image_x = player.x + (Player_W - player_image.get_width()) // 2
        player_image_y = player.y + (Player_H - player_image.get_height()) // 2

        WINDOW.blit(player_image, (player_image_x, player_image_y))
    if choice == 6:
        player_image = pygame.image.load("spaceship6.png")
        player_image = pygame.transform.scale(player_image, (100, 120))
        player_image_x = player.x + (Player_W - player_image.get_width()) // 2
        player_image_y = player.y + (Player_H - player_image.get_height()) // 2

        WINDOW.blit(player_image, (player_image_x, player_image_y))
    if choice == 7:
        player_image = pygame.image.load("spaceship7.png")
        player_image = pygame.transform.scale(player_image, (100, 120))
        player_image_x = player.x + (Player_W - player_image.get_width()) // 2
        player_image_y = player.y + (Player_H - player_image.get_height()) // 2

        WINDOW.blit(player_image, (player_image_x, player_image_y))
    if choice == 8:
        player_image = pygame.image.load("spaceship8.png")
        player_image = pygame.transform.scale(player_image, (100, 120))
        player_image_x = player.x + (Player_W - player_image.get_width()) // 2
        player_image_y = player.y + (Player_H - player_image.get_height()) // 2

        WINDOW.blit(player_image, (player_image_x, player_image_y))
    if choice == 9:
        player_image = pygame.image.load("tractor.png")
        player_image = pygame.transform.scale(player_image, (100, 110))
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
    ship_image = pygame.image.load("hamburger (2).png").convert_alpha()
    ship_image = pygame.transform.scale(ship_image, (100, 100))
    ship_button = play_image.get_rect(center=(WIDTH/2 + 20, HEIGHT/2 + 220))
    WINDOW.blit(ship_image, ship_button)
    pygame.display.update()
    
def draw_youlost():
    lost_text = FONT.render("You Lost!", 1, "white")
    WINDOW.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
    pygame.display.update()

def draw_level_completed():
    level_completed_text = FONT.render("Level completed!", 1, "white")
    WINDOW.blit(level_completed_text, (WIDTH/2 - level_completed_text.get_width()/2, HEIGHT/2 - level_completed_text.get_height()/2))
    pygame.display.update()

def draw_level(LEVEL):
    WINDOW.blit(BG, (0, 0))
    text_level = FONT.render(f" Level: {LEVEL}", 1, "white")
    WINDOW.blit(text_level, (WIDTH/2 - text_level.get_width()/2, HEIGHT/2 - text_level.get_height()/2))
    pygame.display.update()
def draw_locker():
    WINDOW.blit(BG2, (0, 0))
    ship_image1 = pygame.image.load("space-ship1.png").convert_alpha()
    ship_image1 = pygame.transform.scale(ship_image1, (100, 120))
    ship_button1 = ship_image1.get_rect(center=(100, 120))
    WINDOW.blit(ship_image1, ship_button1)
    ship_image2 = pygame.image.load("spaceship2.png").convert_alpha()
    ship_image2 = pygame.transform.scale(ship_image2, (100, 120))
    ship_button2 = ship_image2.get_rect(center=(200, 120))
    WINDOW.blit(ship_image2, ship_button2)
    ship_image3 = pygame.image.load("space-ship3.png").convert_alpha()
    ship_image3 = pygame.transform.scale(ship_image3, (100, 120))
    ship_button3 = ship_image3.get_rect(center=(300, 120))
    WINDOW.blit(ship_image3, ship_button3)
    ship_image4 = pygame.image.load("spaceship4.png").convert_alpha()
    ship_image4 = pygame.transform.scale(ship_image4, (100, 120))
    ship_button4 = ship_image4.get_rect(center=(400, 120))
    WINDOW.blit(ship_image4, ship_button4)
    ship_image5 = pygame.image.load("spaceship5.png").convert_alpha()
    ship_image5 = pygame.transform.scale(ship_image5, (100, 120))
    ship_button5 = ship_image5.get_rect(center=(500, 120))
    WINDOW.blit(ship_image5, ship_button5)
    ship_image6 = pygame.image.load("spaceship6.png").convert_alpha()
    ship_image6 = pygame.transform.scale(ship_image6, (100, 120))
    ship_button6 = ship_image6.get_rect(center=(600, 120))
    WINDOW.blit(ship_image6, ship_button6)
    ship_image7 = pygame.image.load("spaceship7.png").convert_alpha()
    ship_image7 = pygame.transform.scale(ship_image7, (100, 120))
    ship_button7 = ship_image7.get_rect(center=(700, 120))
    WINDOW.blit(ship_image7, ship_button7)
    ship_image8 = pygame.image.load("spaceship8.png").convert_alpha()
    ship_image8 = pygame.transform.scale(ship_image8, (100, 120))
    ship_button8 = ship_image8.get_rect(center=(800, 120))
    WINDOW.blit(ship_image8, ship_button8)
    tractor_image = pygame.image.load("tractor.png").convert_alpha()
    tractor_image = pygame.transform.scale(tractor_image, (100, 120))
    tractor_button = tractor_image.get_rect(center=(900, 110))
    WINDOW.blit(tractor_image, tractor_button)
    return_image = pygame.image.load("return-button.png").convert_alpha()
    return_image = pygame.transform.scale(return_image, (100, 100))
    return_button = return_image.get_rect(center=(WIDTH/2 + 150, HEIGHT/2 + 300))
    WINDOW.blit(return_image, return_button)
    pygame.display.update()
def draw_winner():
    WINDOW.blit(BG, (0, 0))
    trophy_image = pygame.image.load("trophy.png").convert_alpha()
    trophy_image = pygame.transform.scale(trophy_image, (400, 430))
    trophy_button = trophy_image.get_rect(center=(WIDTH/2 , HEIGHT/2))
    WINDOW.blit(trophy_image, trophy_button)
    quit_image = pygame.image.load("quit.png").convert_alpha()
    quit_image = pygame.transform.scale(quit_image, (100, 100))
    quit_button = quit_image.get_rect(center=(WIDTH/2, HEIGHT/2 + 300))
    WINDOW.blit(quit_image, quit_button)
    return_image = pygame.image.load("return-button.png").convert_alpha()
    return_image = pygame.transform.scale(return_image, (100, 100))
    return_button = return_image.get_rect(center=(WIDTH/2 + 150, HEIGHT/2 + 300))
    WINDOW.blit(return_image, return_button)
    pygame.display.update()
def main():
    player = pygame.Rect(200, HEIGHT - Player_H, Player_W, Player_H)
    clock = pygame.time.Clock()
    start_time = time.time() - 3
    elapsed_time = 0
    pause_start_time = 0

    level = 5
    LIVES = 3
    choice = 1
    STAR_VEL = 10

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
            hit = False
            player.x = 200
            player.y = HEIGHT - Player_H
            stars.clear()
            start_time = time.time()
            elapsed_time = 0
            star_add_increment = 1000
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    play_button = pygame.Rect(WIDTH/2 - 75, HEIGHT/2 - 65, 150, 130)
                    quit_button = pygame.Rect(WIDTH/2 - 50, HEIGHT/2 + 35, 100, 100)
                    ship_button = pygame.Rect(WIDTH/2 - 20, HEIGHT/2 + 100, 100, 100)
                    if play_button.collidepoint(mouse_pos):
                        game_state = GameState.LEVEL_STATE
                    if quit_button.collidepoint(mouse_pos):
                        pygame.quit()
                    if ship_button.collidepoint(mouse_pos):
                        game_state = GameState.LOCKER
                        
        if game_state == GameState.LOCKER:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                ship_button1 = pygame.Rect(100, 120, 100, 120)
                ship_button2 = pygame.Rect(200, 120, 100, 120)
                ship_button3 = pygame.Rect(300, 120, 100, 120)
                ship_button4 = pygame.Rect(400, 120, 100, 120)
                ship_button5 = pygame.Rect(500, 120, 100, 120)
                ship_button6 = pygame.Rect(600, 120, 100, 120)
                ship_button7 = pygame.Rect(700, 120, 100, 120)
                ship_button8 = pygame.Rect(800, 120, 100, 120)
                tractor_button = pygame.Rect(900, 110, 100, 120)
                return_button = pygame.Rect(WIDTH/2 + 100, HEIGHT/2 + 250, 100, 100)
                if ship_button1.collidepoint(mouse_pos):
                    player_image = pygame.image.load("space-ship1.png")
                    player_image = pygame.transform.scale(player_image, (100, 130))
                    choice = 1
                    game_state = GameState.MENU

                if ship_button2.collidepoint(mouse_pos):
                    player_image = pygame.image.load("spaceship2.png")
                    player_image = pygame.transform.scale(player_image, (100, 130))
                    choice = 2 
                    game_state = GameState.MENU

                if ship_button3.collidepoint(mouse_pos):
                    player_image = pygame.image.load("space-ship3.png")
                    player_image = pygame.transform.scale(player_image, (100, 130)) 
                    choice = 3
                    game_state = GameState.MENU

                if ship_button4.collidepoint(mouse_pos):
                    player_image = pygame.image.load("spaceship4.png")
                    player_image = pygame.transform.scale(player_image, (100, 130))
                    choice = 4 
                    game_state = GameState.MENU 

                if ship_button5.collidepoint(mouse_pos):
                    player_image = pygame.image.load("spaceship5.png")
                    player_image = pygame.transform.scale(player_image, (100, 130))
                    choice = 5
                    game_state = GameState.MENU

                if ship_button6.collidepoint(mouse_pos):
                    player_image = pygame.image.load("spaceship6.png")
                    player_image = pygame.transform.scale(player_image, (100, 130))
                    choice = 6
                    game_state = GameState.MENU

                if ship_button7.collidepoint(mouse_pos):
                    player_image = pygame.image.load("spaceship7.png")
                    player_image = pygame.transform.scale(player_image, (100, 130))
                    choice = 7
                    game_state = GameState.MENU

                if ship_button8.collidepoint(mouse_pos):
                    player_image = pygame.image.load("spaceship8.png")
                    player_image = pygame.transform.scale(player_image, (100, 130))
                    choice = 8
                    game_state = GameState.MENU

                if tractor_button.collidepoint(mouse_pos):
                    player_image = pygame.image.load("tractor.png")
                    player_image = pygame.transform.scale(player_image, (100, 110))
                    choice = 9
                    game_state = GameState.MENU

                if return_button.collidepoint(mouse_pos):
                    game_state = GameState.MENU

        if game_state == GameState.LEVEL_STATE:
            draw_level(level)
            time.sleep(3)
            game_state = GameState.PLAYING
            start_time = time.time()

        if game_state == GameState.PLAYING:
            clock.tick(144)
            elapsed_transition_time = time.time() - transition_start_time
            if elapsed_transition_time >= 3:
                star_count += clock.get_rawtime()
                elapsed_time = time.time() - start_time

                if star_count > star_add_increment:
                    for _ in range(3):
                        star_x = random.randint(0, WIDTH - STAR_WIDTH)
                        star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                        stars.append(star)

                    star_add_increment = max(500, star_add_increment - 25)
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
                transition_start_time = time.time()
                LIVES -= 1
                game_state = GameState.DEAD
                pause_start_time = time.time()
                if LIVES <= 0:
                    draw_youlost()
                    elapsed_transition_time = time.time() - transition_start_time
                    if elapsed_transition_time >= 5:
                        pygame.quit()
                    

            if elapsed_time >= level * 1:
                game_state = GameState.LEVEL_COMPLETED


            draw(player, elapsed_time, stars, LIVES, choice)

        if game_state == GameState.LEVEL_COMPLETED:
            draw_level_completed()
            level += 1
            STAR_VEL += 2
            time.sleep(3)
            if level >= 6:
                game_state = GameState.WINNER
            else:    
                game_state = GameState.MENU

        if game_state == GameState.LOCKER:
            draw_locker()

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

        if game_state == GameState.DEAD:
            draw_youlost()
            elapsed_pause_time = time.time() - pause_start_time 
            if elapsed_pause_time >= 3:
                game_state = GameState.MENU

        if game_state == GameState.WINNER:
            draw_winner()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    quit_button = pygame.Rect(WIDTH/2 - 50, HEIGHT/2 + 250, 100, 100)
                    return_button = pygame.Rect(WIDTH/2 + 100, HEIGHT/2 + 250, 100, 100)
                    if quit_button.collidepoint(mouse_pos):
                        pygame.quit()
                    if return_button.collidepoint(mouse_pos):
                        level = 1
                        game_state = GameState.MENU

if __name__ == "__main__":
    main()