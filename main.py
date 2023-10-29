

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

# def build_map(surface, map):
#     limits = []
#     fruits = []
#     doors = []
#     x = 0
#     y = 0

#     for line in map:
#         for baldoza in line:
#             if baldoza == "M":
#                 limits.append([baldoza_wall, pygame.Rect(x, y, *BALDOZA)])
#             elif baldoza == "S":
#                 limits.append([baldoza_water, pygame.Rect(x, y, *BALDOZA)])
#             elif baldoza == "A":
#                 limits.append([baldoza_tree, pygame.Rect(x, y, *BALDOZA)])
#             elif baldoza == "F":
#                 fruits.append([baldoza_apple, pygame.Rect(x + 20, y + 20, *BALDOZA_APPLE)])
#             elif baldoza == "P":
#                 doors.append([baldoza_door, pygame.Rect(x, y, *BALDOZA)])
#             x += 80
#         x = 0
#         y += 80
#     return limits, fruits, doors

# ventana
screen = pygame.display.set_mode((WIDTH, HEIGHT))



# images
# background_image = pygame.transform.scale(pygame.image.load("images/fondo_negro.png").convert_alpha(), (WIDTH, HEIGHT))

# baldoza_wall = pygame.image.load("images/muro_ladrillos.png").convert_alpha()
# baldoza_wall = pygame.transform.scale(baldoza_wall, (WIDTH / 16.5, HEIGHT / 11.2))

# baldoza_water = pygame.image.load("images/agua.png").convert()
# baldoza_water = pygame.transform.scale(baldoza_water, (WIDTH / 15, HEIGHT / 10))

# baldoza_tree = pygame.image.load("images/arbol.png").convert_alpha()
# baldoza_tree = pygame.transform.scale(baldoza_tree, (WIDTH / 18, HEIGHT / 10))

# baldoza_door = pygame.image.load("images/puerta.png").convert_alpha()
# baldoza_door = pygame.transform.scale(baldoza_door, (WIDTH / 20, HEIGHT / 10))

# baldoza_apple = pygame.image.load("images/manzana.png").convert_alpha()
# baldoza_apple = pygame.transform.scale(baldoza_apple, (40, 40))


# player_backwards = pygame.transform.scale(pygame.image.load("images/muneco_blanco_espalda.png"), (WIDTH / 40, HEIGHT / 15)).convert_alpha()

# player_forward = pygame.transform.scale(pygame.image.load("images/muneco_blanco_frente.png"), (WIDTH / 40, HEIGHT / 15)).convert_alpha()

# player_walking_forward_00 = pygame.transform.scale(pygame.image.load("images/muneco_blanco_frente.png"), (WIDTH / 40, HEIGHT / 15)).convert_alpha()

# player_walking_forward_01 = pygame.transform.scale(pygame.image.load("images/muneco_blanco_camina_frente_01.png"), (WIDTH / 40, HEIGHT / 15)).convert_alpha()

# player_walking_forward_02 = pygame.transform.scale(pygame.image.load("images/muneco_blanco_frente.png"), (WIDTH / 40, HEIGHT / 15)).convert_alpha()

# player_walking_forward_03 = pygame.transform.scale(pygame.image.load("images/muneco_blanco_camina_frente_02.png"), (WIDTH / 40, HEIGHT / 15)).convert_alpha()

# player_walking_away_00 = pygame.transform.scale(pygame.image.load("images/muneco_blanco_espalda.png"), (WIDTH / 40, HEIGHT / 15)).convert_alpha()

# player_walking_away_01 = pygame.transform.scale(pygame.image.load("images/muneco_blanco_camina_espalda_01.png"), (WIDTH / 40, HEIGHT / 15)).convert_alpha()

# player_walking_away_02 = pygame.transform.scale(pygame.image.load("images/muneco_blanco_espalda.png"), (WIDTH / 40, HEIGHT / 15)).convert_alpha()

# player_walking_away_03 = pygame.transform.scale(pygame.image.load("images/muneco_blanco_camina_espalda_02.png"), (WIDTH / 40, HEIGHT / 15)).convert_alpha()

player_image = player_forward # el juego empieza con el jugador de frente

# textos
font_score = pygame.font.Font(None, 36)
text_count_score = 0

# datos
room_01 = build_map(screen, map_01)
room_02 = build_map(screen, map_02)

room = room_01 # el juego empieza en la habitacion 1

player_rect = player_image.get_rect()
player_rect.x = 100
player_rect.y = 300
player_speed_x = 0
player_speed_y = 0
frames_player = 0

moving_right = False
moving_left = False
moving_up = False
moving_down = False
not_moving_down = True
not_moving_up = True
count_score = 0

wolf_sound = pygame.mixer.music.load("sound/mixkit-wolves-at-scary-forest-2485.wav")
wolf_sound = pygame.mixer.music.play(1)
wolf_sound = pygame.mixer.music.set_volume(0.5)

list_intro_house = [image_intro_house_01, image_intro_house_02]
list_intro_ready_player = [image_intro_ready_player_01, image_intro_ready_player_02]
current_image = 0
image_display_time = 0.5
last_image_time = time.time()

intro_ready_player = False
show_intro_images(list_intro_house, screen, image_display_time, WIDTH, HEIGHT)

# bucle principal
inicio = True
while inicio:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inicio = False

    # eventos

        if event.type == pygame.KEYDOWN:
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

    if intro_ready_player == True:
        pass
    else:
        backup_sound = pygame.mixer.music.load("sound/mixkit-horror-ambience-2482.wav")
        backup_sound = pygame.mixer.music.play(-1)
        backup_sound = pygame.mixer.music.set_volume(1)
        print("space")
        show_intro_images(list_intro_ready_player, screen, 0.5, WIDTH, HEIGHT)


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

    for fruit in room[1][:]:
        if fruit[1].collidepoint(player_center):
            room[1].remove(fruit)
            text_count_score += 1

    for door in room[2]:
        if door[1].collidepoint(player_center):
            if room == room_01:
                room = room_02
                player_rect.x = 400
                player_rect.y = 600
            else:
                room = room_01
                player_rect.x = 560
                player_rect.y = 620

    text_score = font_score.render("Score: {0}".format(text_count_score), True, WHITE)

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
    # pygame.draw.rect(screen, "blue", player_rect, 3)

    for apple in fruit[1]:
        pygame.draw.rect(screen, "red", fruit[1], 3)

    # dibujar texto
    screen.blit(text_score, (WIDTH / 2, 50))

    # actualizar
    pygame.display.flip()

    pygame.display.update()

    # FPS
    clock.tick(FPS)


# salir

pygame.quit()

