
import pygame
from constants import *
from images import *
import time
import sys
from colors import *

def build_map(surface, map):
    limits = []
    fruits = []
    doors = []
    x = 0
    y = 0

    for line in map:
        for baldoza in line:
            if baldoza == "M":
                limits.append([baldoza_wall, pygame.Rect(x, y, *BALDOZA)])
            elif baldoza == "S":
                limits.append([baldoza_water, pygame.Rect(x, y, *BALDOZA)])
            elif baldoza == "A":
                limits.append([baldoza_tree, pygame.Rect(x, y, *BALDOZA)])
            elif baldoza == "F":
                fruits.append([baldoza_apple, pygame.Rect(x + 20, y + 20, *BALDOZA_APPLE)])
            elif baldoza == "P":
                doors.append([baldoza_door, pygame.Rect(x, y, *BALDOZA)])
            x += 80
        x = 0
        y += 80
    return limits, fruits, doors


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
            


