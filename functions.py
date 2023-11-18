
import pygame
from constants import *
from images import baldoza_wall, baldoza_water, baldoza_tree, baldoza_door, baldoza_apple_01, baldoza_key, baldoza_book
import time
import sys
from colors import *
import random
import math

# Definir variables
timer_active = False
timer_start_time = 0
timer_duration = 2000

# Variables del láser
laser_width = 20
laser_height = 20
laser_color = RED
laser_speed = 10
laser_state = "ready"  # Puede estar "ready" o "fire"
laser_direction_x = 1
# laser_direction_y = 1
laser_x = 0
laser_y = 0

def build_map(map) -> list:
    """
    funcion que crea los mapas del juego

    parametros:
    surface: screen
    map que se importa de maps.py

    retorna las listas de baldosas creadas en el mapa
    """
    books = []
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
            elif baldoza == "B":
                books.append([baldoza_book, pygame.Rect(x + 10, y + 10, *BALDOZA_KEY)])
            x += 80
        x = 0
        y += 80
    return limits, fruits, doors, keys, waters, books

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
    """
    funcion que crea el rectangulo del laser del player

    parametros:
    la surface screen, posicion x e y del laser

    no devuelve nada, solo crea el rectangulo de colision del laser
    """
    pygame.draw.rect(screen, laser_color, [x, y, laser_width, laser_height])


def check_key_collision(keys, player_center, text_count_key):
    """
    esta funcion registra si hubo colision con la llave,
    quita la llave de la lista llaves y agrega un 1 al contador

    parametros:
    - llave
    - player_center: centro del player con lo que hace colision
    con la llave 
    - contador de llaves

    retorna contador de llaves
    
    """
    key_sound = pygame.mixer.Sound("sound/mixkit-arcade-score-interface-217.wav")
    for key in keys[:]:
        if key[1].collidepoint(player_center):
            key_sound.play()
            keys.remove(key)
            text_count_key += 1
    return text_count_key

def create_monsters_movements(position, direction, speed, position_limit):
    """
    esta funcion cambia la direccion de los monstruos al llegar a la posicion entrada por parametro

    parametros: 
    - posicion inicial de la figura
    - direccion de la figura
    - velocidad de la figura
    - posicion final de la figura

    retorna nueva posicion y direccion
    
    """
    # Desempaquetar las coordenadas x e y
    x, y = position

    # Actualizar la posición basada en la dirección y la velocidad
    x += speed * direction

    # Verificar los límites y cambiar la dirección si es necesario
    if x < position_limit[0] or x > position_limit[1]:
        direction *= -1

    # Devolver las nuevas coordenadas y la dirección actualizada
    return [x, y], direction

def save_score(player_name, score):
    """
    esta funcion recibe 2 parametros y guarda el nombre y mayor score.
    maneja 3 excepciones, uno para buscar y abrir el archivo donde se guardaran los datos, 
    otra para evaluar valores enteros y la otra para evaluar los indices de la lista 
    para acceder a los elementos del archivo.
    Por ultimo se compara el nuevo score con el previo y se guarda el nuevo si es mayor

    parametros: 
    - player_name: nombre del jugador
    - score: mayor score

    retorna None
    """
    try:
        with open("score.txt", "r") as file:
            line = file.readline()
            if line:
                previous_score = int(line.split()[1])
            else:
                previous_score = 0
    except (FileNotFoundError, ValueError, IndexError):
        previous_score = 0

    if score > previous_score:
        with open("score.txt", "w") as file:
            file.write("{0} {1}\n".format(player_name, score))



def input_name():
    """
    Funcion sin parametros de entrada, maneja una excepcion para corroborar
    valores ingresados en el input y cuenta que no sean mas de tres valores.
    Luego de ingresar los valores termina el programa

    retorna None
    """
    max_attempts = 3
    current_attempt = 0

    while current_attempt < max_attempts:
        try:
            player_name = input("Enter your name (3 letters or digits only): \n")
            if len(player_name) == 3 and player_name.isalnum():
                return player_name
            else:
                raise ValueError("Invalid input. Please enter exactly 3 letters or digits.")
        except ValueError as exception:
            print(exception)
            current_attempt += 1

    print(f"Max attempts reached. Using default name.")
    exit()


def load_score():
    try:
        with open("score.txt", "r") as file:
            line = file.readline()
            if line:
                values = line.split()
                if len(values) == 2:
                    player_name, score = values
                    return player_name, int(score)
                else:
                    print("Invalid data format in score.txt. Using default values.")
                    return None, 0
            else:
                return None, 0
    except FileNotFoundError:
        return None, 0

# funcion para persecucion
def persecution(a, b, distance):
    return (math.sqrt(((b.x - a.x) ** 2) + ((b.y - a.y) ** 2))) < distance




