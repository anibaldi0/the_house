
import pygame
from constants import *

pygame.display.set_mode((WIDTH, HEIGHT))

background_image = pygame.transform.scale(pygame.image.load("images/fondo_negro.png").convert_alpha(), (WIDTH, HEIGHT))

baldoza_wall = pygame.image.load("images/muro_ladrillos.png").convert_alpha()
baldoza_wall = pygame.transform.scale(baldoza_wall, (WIDTH / 12, HEIGHT / 9))

baldoza_water = pygame.image.load("images/agua.png").convert()
baldoza_water = pygame.transform.scale(baldoza_water, (WIDTH / 12, HEIGHT / 9))

baldoza_tree = pygame.image.load("images/arbol.png").convert_alpha()
baldoza_tree = pygame.transform.scale(baldoza_tree, (WIDTH / 18, HEIGHT / 10))

baldoza_door = pygame.image.load("images/puerta.png").convert_alpha()
baldoza_door = pygame.transform.scale(baldoza_door, (WIDTH / 12, HEIGHT / 9))

baldoza_apple = pygame.image.load("images/manzana.png").convert_alpha()
baldoza_apple = pygame.transform.scale(baldoza_apple, (40, 40))

# jugador quieto
player_backwards = pygame.transform.scale(pygame.image.load("images/muneco_blanco_espalda.png"), (WIDTH / 40, HEIGHT / 15)).convert_alpha()
player_forward = pygame.transform.scale(pygame.image.load("images/muneco_blanco_frente.png"), (WIDTH / 40, HEIGHT / 15)).convert_alpha()


# jugador bajando
player_walking_forward_00 = pygame.transform.scale(pygame.image.load("images/muneco_blanco_frente.png"), (WIDTH / 40, HEIGHT / 15)).convert_alpha()
player_walking_forward_01 = pygame.transform.scale(pygame.image.load("images/muneco_blanco_camina_frente_01.png"), (WIDTH / 40, HEIGHT / 15)).convert_alpha()
player_walking_forward_02 = pygame.transform.scale(pygame.image.load("images/muneco_blanco_frente.png"), (WIDTH / 40, HEIGHT / 15)).convert_alpha()
player_walking_forward_03 = pygame.transform.scale(pygame.image.load("images/muneco_blanco_camina_frente_02.png"), (WIDTH / 40, HEIGHT / 15)).convert_alpha()


# jugador subiendo
player_walking_away_00 = pygame.transform.scale(pygame.image.load("images/muneco_blanco_espalda.png"), (WIDTH / 40, HEIGHT / 15)).convert_alpha()
player_walking_away_01 = pygame.transform.scale(pygame.image.load("images/muneco_blanco_camina_espalda_01.png"), (WIDTH / 40, HEIGHT / 15)).convert_alpha()
player_walking_away_02 = pygame.transform.scale(pygame.image.load("images/muneco_blanco_espalda.png"), (WIDTH / 40, HEIGHT / 15)).convert_alpha()
player_walking_away_03 = pygame.transform.scale(pygame.image.load("images/muneco_blanco_camina_espalda_02.png"), (WIDTH / 40, HEIGHT / 15)).convert_alpha()


# craneos masticando
skull_right_00 = pygame.transform.scale(pygame.image.load("images/craneo_derecha_01.png"), (WIDTH / 40, HEIGHT / 15)).convert_alpha()
skull_right_01 = pygame.transform.scale(pygame.image.load("images/craneo_derecha_02.png"), (WIDTH / 40, HEIGHT / 15)).convert_alpha()

skull_left_02 = pygame.transform.scale(pygame.image.load("images/craneo_izquierda_01.png"), (WIDTH / 40, HEIGHT / 15)).convert_alpha()
skull_left_03 = pygame.transform.scale(pygame.image.load("images/craneo_izquierda_02.png"), (WIDTH / 40, HEIGHT / 15)).convert_alpha()

skull_front_01 = pygame.transform.scale(pygame.image.load("images/craneo_frente_01.png"), (WIDTH / 40, HEIGHT / 15)).convert_alpha()
skull_front_02 = pygame.transform.scale(pygame.image.load("images/craneo_frente_02.png"), (WIDTH / 40, HEIGHT / 15)).convert_alpha()


# intro casa
image_intro_house_01 = pygame.image.load("images/casa_embrujada_murci_01.jpg").convert()
image_intro_house_02 = pygame.image.load("images/casa_embrujada_murci_02.jpg").convert()


# intro ready player
image_intro_ready_player_01 = pygame.image.load("images/ready_player_one_800x640_blanco_01.jpg").convert()
image_intro_ready_player_02 = pygame.image.load("images/ready_player_one_800x640_blanco_02.jpg").convert()

