
import pygame
from constants import *
from images import baldoza_wall, baldoza_water, baldoza_tree, baldoza_door, baldoza_apple_01, baldoza_key
import time
import sys
from colors import *
import random

# Variables del láser
laser_width = 20
laser_height = 20
laser_color = RED
laser_speed = 5
laser_state = "ready"  # Puede estar "ready" o "fire"
laser_direction_x = 1
# laser_direction_y = 1
laser_x = 0
laser_y = 0

def build_map(surface, map):
    limits = []
    waters = []
    fruits = []
    doors = []
    keys = []
    x = 0
    y = 0

    for line in map:
        for baldoza in line:
            if baldoza == "M":
                limits.append([baldoza_wall, pygame.Rect(x, y, *BALDOZA)])
            elif baldoza == "S":
                waters.append([baldoza_water, pygame.Rect(x, y, *BALDOZA)])
            elif baldoza == "A":
                limits.append([baldoza_tree, pygame.Rect(x, y, *BALDOZA)])
            elif baldoza == "F":
                fruits.append([baldoza_apple_01, pygame.Rect(x + 20, y + 20, *BALDOZA_APPLE)])
            elif baldoza == "P":
                doors.append([baldoza_door, pygame.Rect(x, y, *BALDOZA)])
            elif baldoza == "K":
                keys.append([baldoza_key, pygame.Rect(x + 10, y + 10, *BALDOZA_KEY)])
            x += 80
        x = 0
        y += 80
    return limits, fruits, doors, keys, waters


def attancking_skull(surface, ):
    pass

def finish():
    pygame.quit()
    sys.exit()


def show_intro_images(intro_images_list, screen, display_time, width, height):

    current_image = 0
    last_image_time = time.time()
    show_images = True

        # Bucle principal

    while True:

        if show_images:
            if time.time() - last_image_time > display_time:
                current_image = (current_image + 1) % len(intro_images_list)
                last_image_time = time.time()
            scaled_image = pygame.transform.scale(intro_images_list[current_image], (width, height))
            screen.blit(scaled_image, (0, 0))
            pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    finish()
                if event.key == pygame.K_SPACE:
                    #print("K_SPACE")
                    show_images = False
                if event.key == pygame.K_a:
                    show_images = False
                    print("a")
                return
            
def create_laser(screen, x, y):
    pygame.draw.rect(screen, laser_color, [x, y, laser_width, laser_height])


def check_key_collision(keys, player_center, text_count_key):
    key_sound = pygame.mixer.Sound("sound/mixkit-arcade-score-interface-217.wav")
    for key in keys[:]:
        if key[1].collidepoint(player_center):
            key_sound.play()
            keys.remove(key)
            text_count_key += 1
    return text_count_key

def create_monsters_movements(position, direction, speed, direction_limit):
    # Desempaquetar las coordenadas x e y
    x, y = position

    # Actualizar la posición basada en la dirección y la velocidad
    x += speed * direction

    # Verificar los límites y cambiar la dirección si es necesario
    if x < direction_limit[0] or x > direction_limit[1]:
        direction *= -1

    # Devolver las nuevas coordenadas y la dirección actualizada
    return [x, y], direction





