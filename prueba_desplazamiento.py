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

import pygame

def move_rect(rect, start_x, end_x, speed):
    # Verificar la dirección del movimiento
    if rect.x < end_x and rect.x + speed <= end_x:
        rect.x += speed
    else:
        rect.x -= speed


# Ejemplo de uso:
pygame.init()

# Configuración del rectángulo
rect = pygame.Rect(0, 0, 30, 30)
start_x = 100
end_x = 500
speed = 5

# Bucle principal
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600, 400))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Lógica de movimiento del rectángulo
    move_rect(rect, start_x, end_x, speed)

    # Dibujar el rectángulo y actualizar la pantalla
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 255), rect)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()



