

import pygame
import time

from constants import *
from colors import *
from functions import *
from maps import *
from images import *

# inicializar
pygame.init()
# pygame.mixer.init()


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

player_name, previous_score = load_score()

def terminar():
    """
    Esta función no toma parametros.

    Parámetros:
    sale del juego.

    Devuelve:
    None.
    """
    pygame.quit()
    exit()

def wait_user():
    """
    Esta función no toma parametros.

    Parámetros:
    entra en bucle infinito para agregar una pausa al juego.

    Devuelve:
    return para salir del bucle
    """
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminar()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    terminar()
                return
            
def show_paused_text(surface, texto, fuente, coordenadas, color_fuente):
    """
    Muestra un texto de pausa en la superficie especificada.

    Parametros:
    - surface: La superficie en la que se mostrara el texto de pausa.
    - texto: El texto que se mostrará.
    - fuente: El objeto de fuente utilizado para renderizar el texto.
    - coordenadas: La posición central donde se mostrará el texto.
    - color_fuente: El color del texto.

    No devuelve nada. Simplemente muestra el texto en la superficie especificada.
    """
    paused_text = fuente.render(texto, True, color_fuente)
    rect_paused_text = paused_text.get_rect()
    rect_paused_text.center = coordenadas
    surface.blit(paused_text, rect_paused_text)
    pygame.display.flip()


# datas
room_01 = build_map(map_01)
room_02 = build_map(map_02)

# el juego empieza en la habitacion 1
room = room_01

font_win_game = pygame.font.Font(None, 72)
win_game_text = font_win_game.render("You win the game!", True, WHITE)
win_game_rect = win_game_text.get_rect()
win_game_rect.center = (WIDTH // 2, HEIGHT // 2)

# el juego empieza con el jugador de frente
player_image = player_forward 

player_rect = player_image.get_rect()
player_rect.x = 100
player_rect.y = 170
player_speed_x = 0
player_speed_y = 0
player_speed = 3
frames_player = 0
# frames_bat = 0
text_count_score = 0
text_count_key = 0
lives = 500

# time
current_time = 0

# bat
bat_position = [80, 100]
bat_speed = 3
bat_direction_x = 1
bat_hidden = False

#skull
skull_position = [500, 250]
skull_speed = 3
skull_direction_x = 1
skull_hidden = False


moving_right = False
moving_left = False
moving_up = False
moving_down = False
not_moving_pumpkin = True
intro_ready_player = False
collision_with_water = False
collision_with_door = False
collision_with_tree = False
paused = False
playing_music = True
laser_ready = False


wolf_sound = pygame.mixer.music.load("sound/mixkit-wolves-at-scary-forest-2485.wav")
wolf_sound = pygame.mixer.music.play(1)
wolf_sound = pygame.mixer.music.set_volume(0.5)

pumpkin_sound = pygame.mixer.Sound("sound/mixkit-unlock-new-item-game-notification-254.wav")
pumpkin_sound.set_volume(0.4)
lives_down = pygame.mixer.Sound("sound/mixkit-arcade-retro-jump-223.wav")
lives_down.set_volume(0.2)
open_door = pygame.mixer.Sound("sound/mixkit-arcade-game-complete-or-approved-mission-205.wav")
laser_sound = pygame.mixer.Sound("sound/blaster-2-81267.mp3")
laser_sound.set_volume(0.1)


list_intro_house = [image_intro_house_01, image_intro_house_02]
list_intro_ready_player = [image_intro_ready_player_01, image_intro_ready_player_02]
current_image = 0
image_display_time = 0.5
last_image_time = time.time()

# Variables para el temporizador
start_time = pygame.time.get_ticks()
delay = 3000
bat_hidden = False

show_intro_images(list_intro_house, screen, image_display_time, WIDTH, HEIGHT)

if intro_ready_player == False:
    backup_sound = pygame.mixer.music.load("sound/mixkit-horror-ambience-2482.wav")
    backup_sound = pygame.mixer.music.play(1)
    backup_sound = pygame.mixer.music.set_volume(1)
    print("space")
    show_intro_images(list_intro_ready_player, screen, 0.5, WIDTH, HEIGHT)
else:
    intro_ready_player = True

ultima_actualizacion = pygame.time.get_ticks()
interval = 100
frame = 0
    
# bucle principal
inicio = True
while inicio:

    elapsed_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inicio = False

    # eventos
        if event.type == pygame.KEYDOWN:
            # if event.key == pygame.K_SPACE:
            #     intro_ready_player = True
            if event.key == pygame.K_d:
                # direction = "right"
                player_speed_x = player_speed
                moving_right = True
            if event.key == pygame.K_a:
                # direction = "left"
                player_speed_x = -player_speed
                moving_left = True
            if event.key == pygame.K_w:
                # direction = "up"
                player_speed_y = -player_speed
                moving_up = True
            if event.key == pygame.K_s:
                # direction = "down"
                player_speed_y = player_speed
                moving_down = True
            if event.key == pygame.K_UP:
                # shoot
                if event.key == pygame.K_UP:
                    if laser_state == "ready" and laser_ready == True:
                        laser_sound.play()
                        laser_x = player_rect.x + player_rect.width  # Posiciona el láser a la derecha del jugador
                        laser_y = player_rect.y + 15
                        laser_state = "fired"
                if pygame.key.get_pressed()[pygame.K_d]:  # Verifica si K_UP y K_d están presionadas simultáneamente
                    if laser_state == "ready" and laser_ready == True:
                        laser_sound.play()
                        laser_x = player_rect.x + player_rect.width # Posiciona el láser a la derecha del jugador
                        laser_y = player_rect.y + 15
                        laser_state = "fired"
                elif pygame.key.get_pressed()[pygame.K_a]:  # Verifica si K_UP y K_a están presionadas simultáneamente
                    if laser_state == "ready" and laser_ready == True:
                        laser_sound.play()
                        laser_x = player_rect.x - laser_width # Posiciona el láser a la izquierda del jugador
                        laser_y = player_rect.y + 15
                        laser_state = "fired"
            if event.key == pygame.K_p:
                if playing_music:
                    pygame.mixer.music.pause()
                show_paused_text(screen, "PAUSED", font_score, (WIDTH / 2, HEIGHT / 2), RED)
                wait_user()
                if playing_music:
                    pygame.mixer.music.unpause()
                

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
                lives_down.play()
                collision_with_tree = True
                lives -= 1
            elif limit[0] == baldoza_door:
                if text_count_key <= 0:
                    collision_with_door = True
                    lives -= 5

    for water in room[4]:
        if water[1].colliderect(player_rect):
            if water[0] == baldoza_water:
                lives_down.play()
                collision_with_water = True
                lives -= 1
                player_rect.x += player_speed_x
                # player_rect.y += player_speed_y

    # Crear un rectángulo para el láser
    if laser_state == "fired":
        laser_x += laser_speed * laser_direction_x
        # laser_y += laser_speed * laser_direction_y
        laser_rect = pygame.Rect(laser_x, laser_y, laser_width, laser_height)
            
        # Verificar colisión con las paredes
        for wall in room[0]:
            if wall[1].colliderect(laser_rect):
                laser_state = "ready"
                # Puedes hacer más cosas aquí, como reproducir un sonido de impacto, etc.

        # Verificar colisión laser con baldoza_water
        for water in room[0]:
            if water[1].colliderect(laser_rect) and water[0] == baldoza_water:
                # Si colisiona con baldoza_water, continúa moviéndose
                continue

    # verificar colision entre player y bat
    if player_rect.colliderect(pygame.Rect(bat_position, (60, 60))):
        lives_down.play()
        lives -= 500
    elif player_rect.colliderect(pygame.Rect(skull_position, (60, 60))):
        lives_down.play()
        lives -= 500

    # Verificar colisión del láser con el bat
    if laser_state == "fired" and laser_rect.colliderect(pygame.Rect(bat_position, (60, 60))):
        text_count_score += 2
        bat_position = [-100, -100]
        laser_ready = False
        save_score(player_name, text_count_score)
        laser_state = "ready"
        bat_hidden = True
        start_time = pygame.time.get_ticks()

    elif laser_state == "fired" and laser_rect.colliderect(pygame.Rect(skull_position, (60, 60))):
        text_count_score += 2
        skull_position = [-100, -100]
        laser_ready = False
        save_score(player_name, text_count_score)
        laser_state = "ready"
        skull_hidden = True  # Indicar que el bat está oculto
        start_time = pygame.time.get_ticks()

    # Verificar si el tiempo de espera ha transcurrido (3 segundos)
    if bat_hidden and pygame.time.get_ticks() - start_time >= delay:
        bat_position = [80, 100]
        bat_hidden = False 
        hide_bat_time = 0
    if skull_hidden and pygame.time.get_ticks() - start_time >= delay:
        skull_position = [500, 250]
        skull_hidden = False 
        hide_bat_time = 0

    text_count_key = check_key_collision(room[3], player_center, text_count_key)
    print(text_count_key)

    for fruit in room[1][:]:
        if fruit[1].collidepoint(player_center):
            room[1].remove(fruit)
            text_count_score += 1
            pumpkin_sound.play()
            laser_ready = True
            if lives < 500:
                lives += 50
            else:
                lives = 500
            
        

    for door in room[2]:
        if door[1].collidepoint(player_center):
            if room == room_01:
                # if text_count_key > 0:
                #     bat_position = [-200, -100]
                #     skull_position = [-200, -100]
                #     open_door.play()
                #     room = room_02
                #     player_rect.x = 400
                #     player_rect.y = 600
                #     text_count_key -= 1
                # else:
                #     lives_down.play()
                #     collision_with_door = True
                #     lives -= 5
                        

            # elif room == room_02:
                if text_count_key > 0:
                    open_door.play()
                    pygame.mixer.music.pause()
                    show_paused_text(screen, "YOU WIN", font_score, (WIDTH / 2, HEIGHT /2), WHITE)
                    player_name = input_name()  # Pedir el nombre del jugador
                    save_score(player_name, text_count_score)
                    wait_user()
                else:
                    lives_down.play()
                    collision_with_door = True
                    lives -= 5

    # textos
    font_score = pygame.font.Font(None, 45)
    font_best_score = pygame.font.Font(None, 25)

    text_score = font_score.render("Score: {0}".format(text_count_score), True, WHITE)
    text_lives = font_score.render("Lives: {0}".format(lives), True, RED)
    text_key = font_score.render("Keys: {0}".format(text_count_key), True, ORANGE)
    player_name_text = font_score.render("{0}".format(player_name), True, GRAY)
    previous_score_text = font_score.render("{0}".format(previous_score), True, GRAY)
    best_score = font_best_score.render("Best Score", True, GREEN)
    # laser_ready = font_best_score.render("Laser: {0}".format(text_laser_ready), True, WHITE)

    # dibujos
    screen.blit(background_image, (0, 0))

        # posicionar el texto para hacer un offset
    text_position_score = (550, 100)
    text_position_lives = (300, 100)
    text_position_key = (800, 100)
    player_name_position = (100, 110)
    previous_score_position = (170, 110)
    best_score_position = (100, 90)
    # laser_ready_position = (1000, 110)

    # dibujar texto
    screen.blit(text_score, text_position_score)
    screen.blit(text_lives, text_position_lives)
    screen.blit(text_key, text_position_key)
    screen.blit(player_name_text, player_name_position)
    screen.blit(previous_score_text, previous_score_position)
    screen.blit(best_score, best_score_position)
    # screen.blit(laser_ready, laser_ready_position)

    # screen.blit(paused_text, paused_position_text)

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

    #Lógica del movimiento del láser
    if laser_state == "fired":
        laser_x += laser_speed * laser_direction_x

        # Verificar los límites y cambiar el estado del láser si es necesario
        if laser_x >= WIDTH or laser_x <= 0 or laser_y >= HEIGHT or laser_y <= 0:
            laser_state = "ready"

        # Crear un rectángulo para el láser
        laser_rect = pygame.Rect(laser_x, laser_y, laser_width, laser_height)

    # Eventos para cambiar la dirección del láser
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and laser_state == "ready":
        laser_direction_x = -1
        laser_direction_y = 0
    if keys[pygame.K_d] and laser_state == "ready":
        laser_direction_x = 1
        laser_direction_y = 0

    # Dibujar láser si está en estado "fired"
    if laser_state == "fired":
        create_laser(screen, laser_x, laser_y)

    # Dibujar láser si está en estado "fired"
    if laser_state == "fired":
        pygame.draw.rect(screen, GREEN, laser_rect, 2)

    # Actualizar rectángulo 1 (bat)
    bat_position, bat_direction_x = create_monsters_movements(bat_position, bat_direction_x, bat_speed, (80, 1200 - 60))

    # Actualizar rectángulo 2 (skull)
    skull_position, skull_direction_x = create_monsters_movements(skull_position, skull_direction_x, skull_speed, (480, 960 - 60))


    # Dibujar hitbox verde para rectángulo 1
    # pygame.draw.rect(screen, GREEN, skull_position + [60, 60], 2)

    if lives <= 0:
        pygame.mixer.music.pause()
        show_paused_text(screen, "GAME OVER", font_score, (WIDTH / 2, HEIGHT / 2), RED)
        player_name = input_name()
        save_score(player_name, text_count_score)
        wait_user()
        
        


    # Dibujar rectángulo 1
    if bat_direction_x == 1:
        screen.blit(bat_right, bat_position)
    else:
        screen.blit(bat_left, bat_position)

    # Dibujar hitbox verde para rectángulo 2
    # pygame.draw.rect(screen, GREEN, skull_position + [60, 60], 2)

    # Dibujar rectángulo 2
    if skull_direction_x == 1:
        screen.blit(skull_right, skull_position)
    else:
        screen.blit(skull_left, skull_position)

    # hitbox

    # actualizar
    pygame.display.flip()

    pygame.display.update()

    # FPS
    clock.tick(FPS)


# salir

terminar()



