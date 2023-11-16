# import pygame
# import sys

# # Inicializar Pygame
# pygame.init()

# # Definir colores
# BLACK = (0, 0, 0)
# GREEN = (0, 255, 0)

# # Configuración de la pantalla
# width, height = 400, 400
# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption('Movimiento de Rectángulos')

# # Definir rectángulo 1
# rect_position_01 = [0, 100]
# image_01_right = pygame.transform.scale(pygame.image.load("images/bat_der_01.png"), (60, 60))
# image_01_left = pygame.transform.flip(image_01_right, True, False)  # Voltear horizontalmente
# speed_rect_01 = 2
# direction_x_rect_01 = 1

# # Definir rectángulo 2
# rect_position_02 = [0, 300]
# image_02_right = pygame.transform.scale(pygame.image.load("images/craneo_derecha_02.png"), (60, 60))
# image_02_left = pygame.transform.flip(image_02_right, True, False)  # Voltear horizontalmente
# speed_rect_02 = 3
# direction_x_rect_02 = 1

# def create_rect_movements(rect, direction_x, speed):
#     # Actualizar posición del rectángulo
#     rect[0] += speed * direction_x

#     # Cambiar dirección cuando alcanza ciertas coordenadas
#     if rect[0] >= width - 60 and direction_x == 1:
#         direction_x = -1
#     elif rect[0] <= 0 and direction_x == -1:
#         direction_x = 1

#     return rect, direction_x

# # Bucle principal
# clock = pygame.time.Clock()

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#     # Actualizar rectángulo 1
#     rect_position_01, direction_x_rect_01 = create_rect_movements(
#         rect_position_01, direction_x_rect_01, speed_rect_01
#     )

#     # Actualizar rectángulo 2
#     rect_position_02, direction_x_rect_02 = create_rect_movements(
#         rect_position_02, direction_x_rect_02, speed_rect_02
#     )

#     # Limpiar pantalla
#     screen.fill(BLACK)

#     # Dibujar hitbox verde para rectángulo 1
#     pygame.draw.rect(screen, GREEN, rect_position_01 + [60, 60], 2)

#     # Dibujar rectángulo 1
#     if direction_x_rect_01 == 1:
#         screen.blit(image_01_right, rect_position_01)
#     else:
#         screen.blit(image_01_left, rect_position_01)

#     # Dibujar hitbox verde para rectángulo 2
#     pygame.draw.rect(screen, GREEN, rect_position_02 + [60, 60], 2)

#     # Dibujar rectángulo 2
#     if direction_x_rect_02 == 1:
#         screen.blit(image_02_right, rect_position_02)
#     else:
#         screen.blit(image_02_left, rect_position_02)

#     # Actualizar la pantalla
#     pygame.display.flip()

#     # Controlar la velocidad del bucle
#     clock.tick(60)


# import pygame
# import sys

# # Inicializar Pygame
# pygame.init()

# # Definir colores
# WHITE = (255, 255, 255)

# # Configuración de la ventana
# width, height = 400, 400
# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption("Mover Rectángulo")

# # Definir variables para el control del tiempo
# start_time = pygame.time.get_ticks()
# delay_time = 2000  # 2 segundos en milisegundos
# return_time = 3000  # 3 segundos en milisegundos

# def move_figure(current_position, target_position):
#     current_time = pygame.time.get_ticks()
#     elapsed_time = current_time - start_time

#     if elapsed_time >= delay_time and elapsed_time < return_time:
#         # Traslada el rectángulo a la nueva posición después de 2 segundos
#         rect.x, rect.y = target_position
#     elif elapsed_time >= return_time:
#         # Vuelve el rectángulo a la posición original después de 3 segundos
#         rect.x, rect.y = current_position

# # Definir el rectángulo inicial
# rect_size = (50, 50)
# rect_color = WHITE
# current_position = (100, 200)
# target_position = (300, 300)
# rect = pygame.Rect(current_position, rect_size)

# # Bucle principal del juego
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#     # Lógica del juego
#     move_figure(current_position, target_position)

#     # Dibujar en la pantalla
#     screen.fill((0, 0, 0))  # Limpia la pantalla
#     pygame.draw.rect(screen, rect_color, rect)  # Dibuja el rectángulo en la nueva posición

#     # Actualizar la pantalla
#     pygame.display.flip()

#     # Controlar la velocidad del bucle
#     pygame.time.Clock().tick(60)  # 60 fotogramas por segundo


import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Mover Rectángulo')

# Color
black = (0, 0, 0)
white = (255, 255, 255)

# Definir el rectángulo inicial
current_position = (-100, -200)
rect_width, rect_height = 50, 50
rect = pygame.Rect(current_position[0], current_position[1], rect_width, rect_height)

# move_time = 5000

def move_figures(current_position, new_position, move_time = 1000):
    # global rect
    if pygame.time.get_ticks() >= move_time:
        current_position = new_position
        move_time = pygame.time.get_ticks() + move_time

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Llamada a la función move_rect con la nueva posición (200, 300)
    new_position = (200, 300)
    move_figures(rect, new_position, 1000)

    # Dibujar en la pantalla
    screen.fill(black)
    pygame.draw.rect(screen, white, rect)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad del bucle
    pygame.time.Clock().tick(60)




