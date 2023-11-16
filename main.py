

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

def terminar():
    pygame.quit()
    exit()

def wait_user():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminar()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    terminar()
                return
            
def show_paused_text(surface, texto, fuente, coordenadas, color_fuente):
    paused_text = fuente.render(texto, True, color_fuente)
    rect_paused_text = paused_text.get_rect()
    rect_paused_text.center = coordenadas
    surface.blit(paused_text, rect_paused_text)
    pygame.display.flip()


# datas
room_01 = build_map(screen, map_01)
room_02 = build_map(screen, map_02)

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
bat_speed = 5
bat_direction_x = 1

#skull
skull_position = [500, 250]
skull_speed = 3
skull_direction_x = 1


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
                    if laser_state == "ready":
                        laser_sound.play()
                        laser_x = player_rect.x + player_rect.width  # Posiciona el láser a la derecha del jugador
                        laser_y = player_rect.y + 15
                        laser_state = "fired"
                if pygame.key.get_pressed()[pygame.K_d]:  # Verifica si K_UP y K_d están presionadas simultáneamente
                    if laser_state == "ready":
                        laser_sound.play()
                        laser_x = player_rect.x + player_rect.width # Posiciona el láser a la derecha del jugador
                        laser_y = player_rect.y + 15
                        laser_state = "fired"
                elif pygame.key.get_pressed()[pygame.K_a]:  # Verifica si K_UP y K_a están presionadas simultáneamente
                    if laser_state == "ready":
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
            elif limit[0] == baldoza_water:
                lives_down.play()
                collision_with_water = True
                lives -= 1
            elif limit[0] == baldoza_door:
                if text_count_key <= 0:
                    collision_with_door = True
                    lives -= 5

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
        lives -= 1
    elif player_rect.colliderect(pygame.Rect(skull_position, (60, 60))):
        lives_down.play()
        lives -= 1

    # Verificar colisión del láser con el bat
    if laser_state == "fired" and laser_rect.colliderect(pygame.Rect(bat_position, (60, 60))):
        text_count_score += 2
        bat_position = [-100, -100]
        # current_time = 0  # Reiniciar el temporizador aquí
        # Se ha producido una colisión entre el láser y el bat
        laser_state = "ready"  # Restablecer el estado del láser
    elif laser_state == "fired" and laser_rect.colliderect(pygame.Rect(skull_position, (60, 60))):
        text_count_score += 2
        skull_position = [-100, -100]
        # current_time = 0  # Reiniciar el temporizador aquí
        # Se ha producido una colisión entre el láser y el bat
        laser_state = "ready"  # Restablecer el estado del láser
        # Aquí puedes agregar más lógica, como restar puntos al bat, reproducir un sonido, etc.
        
    # Incrementar el tiempo transcurrido
    current_time = pygame.time.get_ticks()
    if current_time - ultima_actualizacion >= interval:
        frame += 1
        if bat_position == [-100, -100] and frame >= interval:
            bat_position = [80, 100]
            frame = 0
        elif skull_position == [-100, -100] and frame >= interval:
            skull_position = [500, 250]
            frame = 0
        elif text_count_key == 1 and frame >= interval:
            text_count_key -= 1
            room[3].append([baldoza_key, pygame.Rect(1050, 160, *BALDOZA_KEY)])
            print(text_count_key)
        print(bat_position, frame)
        ultima_actualizacion = current_time

    text_count_key = check_key_collision(room[3], player_center, text_count_key)
    print(text_count_key)
    if text_count_key == 1 and current_time > 5000 * 1000:
        text_count_key -= 1
        room[3].append([baldoza_key, pygame.Rect(1050, 160, *BALDOZA_KEY)])
        print(text_count_key)

    for fruit in room[1][:]:
        if fruit[1].collidepoint(player_center):
            room[1].remove(fruit)
            text_count_score += 1
            pumpkin_sound.play()
            if lives < 500:
                lives += 50
            else:
                lives = 500
        

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
                    lives_down.play()
                    collision_with_door = True
                    lives -= 5
                        

            elif room == room_02:
                if text_count_key > 0:
                    open_door.play()
                    screen.blit(win_game_text, win_game_rect)
                    pygame.display.flip()
                    pygame.time.delay(2000)
                else:
                    lives_down.play()
                    collision_with_door = True
                    lives -= 5

    # textos
    font_score = pygame.font.Font(None, 45)

    text_score = font_score.render("Score: {0}".format(text_count_score), True, WHITE)
    text_lives = font_score.render("Lives: {0}".format(lives), True, RED)
    text_key = font_score.render("Keys: {0}".format(text_count_key), True, ORANGE)

    # dibujos
    screen.blit(background_image, (0, 0))

        # posicionar el texto para hacer un offset
    text_position_score = (550, 100)
    text_position_lives = (300, 100)
    text_position_key = (800, 100)
    paused_position_text = (550, 500)
    


    # dibujar texto
    screen.blit(text_score, text_position_score)
    screen.blit(text_lives, text_position_lives)
    screen.blit(text_key, text_position_key)

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

    # Lógica del movimiento del láser
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

    # if paused == True:
    #     show_paused_text(screen, "PAUSED", font_score, (WIDTH / 2, HEIGHT / 2), RED)

    # hitbox

    # actualizar
    pygame.display.flip()

    pygame.display.update()

    # FPS
    clock.tick(FPS)


# salir

terminar()



