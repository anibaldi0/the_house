

import pygame
import time

from constants import *
from colors import *
from functions import *
from maps import *
from images import *

# inicializar
pygame.init()
pygame.mixer.init()


# reloj
clock = pygame.time.Clock()


# medidas in constant.py

# colores in colors.py

# mapas in maps.py

# funciones in functions.py

# ventana
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pumpkin = pygame.image.load("images/calabaza_01.png")
pygame.display.set_icon(pumpkin)
pygame.display.set_caption("The House")

# images

# datas
room_01 = build_map(screen, map_01)
room_02 = build_map(screen, map_02)

room = room_01 # el juego empieza en la habitacion 1

player_image = player_forward # el juego empieza con el jugador de frente

player_rect = player_image.get_rect()
player_rect.x = 100
player_rect.y = 100
player_speed_x = 0
player_speed_y = 0
frames_player = 0
frames_bat = 0
text_count_score = 0
text_count_key = 0
lives = 500

moving_right = False
moving_left = False
moving_up = False
moving_down = False
not_moving_pumpkin = True
intro_ready_player = False
collision_with_water = False
collision_with_door = False
collision_with_tree = False 

wolf_sound = pygame.mixer.music.load("sound/mixkit-wolves-at-scary-forest-2485.wav")
wolf_sound = pygame.mixer.music.play(1)
wolf_sound = pygame.mixer.music.set_volume(0.5)

pumpkin_sound = pygame.mixer.Sound("sound/mixkit-unlock-new-item-game-notification-254.wav")
close_door = pygame.mixer.Sound("sound/mixkit-arcade-retro-jump-223.wav")
open_door = pygame.mixer.Sound("sound/mixkit-arcade-game-complete-or-approved-mission-205.wav")

list_intro_house = [image_intro_house_01, image_intro_house_02]
list_intro_ready_player = [image_intro_ready_player_01, image_intro_ready_player_02]
current_image = 0
image_display_time = 0.5
last_image_time = time.time()

show_intro_images(list_intro_house, screen, image_display_time, WIDTH, HEIGHT)

if intro_ready_player == False:
    backup_sound = pygame.mixer.music.load("sound/mixkit-horror-ambience-2482.wav")
    backup_sound = pygame.mixer.music.play(1)
    backup_sound = pygame.mixer.music.set_volume(1)
    print("space")
    show_intro_images(list_intro_ready_player, screen, 0.5, WIDTH, HEIGHT)
else:
    intro_ready_player = True
    

# bucle principal
inicio = True
while inicio:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inicio = False

    # eventos
        if event.type == pygame.KEYDOWN:
            # if event.key == pygame.K_SPACE:
            #     intro_ready_player = True
            if event.key == pygame.K_d:
                # direction = "right"
                player_speed_x = 5
                moving_right = True
            if event.key == pygame.K_a:
                # direction = "left"
                player_speed_x = -5
                moving_left = True
            if event.key == pygame.K_w:
                # direction = "up"
                player_speed_y = -5
                moving_up = True
            if event.key == pygame.K_s:
                # direction = "down"
                player_speed_y = 5
                moving_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                #direction = "right"
                player_speed_x = 0
                moving_right = False
            if event.key == pygame.K_a:
                # direction = "left"
                player_speed_x = 0
                moving_left = False
            if event.key == pygame.K_w:
                #direction = "up"
                player_speed_y = 0
                moving_up = False
            if event.key == pygame.K_s:
                #direction = "down"
                player_speed_y = 0
                moving_down = False

    # logica
    player_rect.x += player_speed_x  # se actualiza las coordenadas del player
    player_rect.y += player_speed_y

    if player_rect.x >= WIDTH - 30:
        player_rect.x = WIDTH - 30
    if player_rect.x <= 0:
        player_rect.x = 0
    if player_rect.y >= HEIGHT - 60:
        player_rect.y = HEIGHT - 60
    if player_rect.y <= 0:
        player_rect.y = 0

    player_center = player_rect.center
    
    for limit in room[0]:
        if limit[1].colliderect(player_rect):
            player_rect.x -= player_speed_x
            player_rect.y -= player_speed_y
            if limit[0] == baldoza_tree:
                close_door.play()
                collision_with_tree = True
                lives -= 1
            if limit[0] == baldoza_water:
                close_door.play()
                collision_with_water = True
                lives -= 1
            elif limit[0] == baldoza_door:
                if text_count_key <= 0:
                    collision_with_door = True
                    lives -= 5

    for fruit in room[1][:]:
        if fruit[1].collidepoint(player_center):
            room[1].remove(fruit)
            text_count_score += 1
            pumpkin_sound.play()
            if lives < 500:
                lives += 50
            else:
                lives = 500

    text_count_key = check_key_collision(room[3], player_center, text_count_key)

        
    for door in room[2]:
        if door[1].collidepoint(player_center):
            if room == room_01:
                if text_count_key > 0:
                    open_door.play()
                    room = room_02
                    player_rect.x = 400
                    player_rect.y = 600
                    text_count_key -= 1
                else:
                    close_door.play()
                    collision_with_door = True
                    lives -= 5
                        

            elif room == room_02:
                if text_count_key > 0:
                    open_door.play()
                    room = room_01
                    player_rect.x = 560
                    player_rect.y = 580
                    text_count_key -= 1
                else:
                    close_door.play()
                    collision_with_door = True
                    lives -= 5

    # textos
    font_score = pygame.font.Font(None, 45)

    text_score = font_score.render("Score: {0}".format(text_count_score), True, WHITE)
    text_lives = font_score.render("Lives: {0}".format(lives), True, RED)
    text_key = font_score.render("Keys: {0}".format(text_count_key), True, ORANGE)

    # dibujos
    
    screen.blit(background_image, (0, 0))

    for element in room:
        for baldoza in element:
            screen.blit(baldoza[0], baldoza[1])

    if moving_right:
        frames_player += 1
        if frames_player >= 21:
            frames_player = 1
        if frames_player < 6:
            player_image = player_walking_forward_00
        elif frames_player < 11:
            player_image = player_walking_forward_01
        elif frames_player < 16:
            player_image = player_walking_forward_02
        elif frames_player < 21:
            player_image = player_walking_forward_03

        screen.blit(player_image, player_rect)

    elif moving_left:
        frames_player += 1
        if frames_player >= 21:
            frames_player = 1
        if frames_player < 6:
            player_image = player_walking_forward_00
        elif frames_player < 11:
            player_image = player_walking_forward_01
        elif frames_player < 16:
            player_image = player_walking_forward_02
        elif frames_player < 21:
            player_image = player_walking_forward_03

        screen.blit(player_image, player_rect)

    elif moving_up:
        frames_player += 1
        if frames_player >= 21:
            frames_player = 1
        if frames_player < 6:
            player_image = player_walking_away_00
        elif frames_player < 11:
            player_image = player_walking_away_01
        elif frames_player < 16:
            player_image = player_walking_away_02
        elif frames_player < 21:
            player_image = player_walking_away_03

        screen.blit(player_image, player_rect)

    elif moving_down:
        frames_player += 1
        if frames_player >= 21:
            frames_player = 1
        if frames_player < 6:
            player_image = player_walking_forward_00
        elif frames_player < 11:
            player_image = player_walking_forward_01
        elif frames_player < 16:
            player_image = player_walking_forward_02
        elif frames_player < 21:
            player_image = player_walking_forward_03

        screen.blit(player_image, player_rect)

    else:
        if player_speed_y < 0:
            player_image = player_backwards
        elif player_speed_y > 0:
            player_image = player_forward 

        screen.blit(player_image, player_rect)

    # hitbox

    # posicionar el texto para hacer un offset
    text_position_score = (550, 100)
    text_position_lives = (300, 100)
    text_position_key = (800, 100)

    # dibujar texto
    screen.blit(text_score, text_position_score)
    screen.blit(text_lives, text_position_lives)
    screen.blit(text_key, text_position_key)

    # actualizar
    pygame.display.flip()

    pygame.display.update()

    # FPS
    clock.tick(FPS)


# salir

pygame.quit()



