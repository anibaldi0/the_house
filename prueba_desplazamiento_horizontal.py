import pygame
import sys

# Inicializar Pygame
pygame.init()

# Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Configuración de la pantalla
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncing Rectangles")

# Definir los rectángulos y sus hitboxes
rect_width = 50
rect_height = 30

rect1_pos = (80, 300)
rect1_x, rect1_y = rect1_pos
rect1_speed = 5

rect2_pos = (200, 400)
rect2_x, rect2_y = rect2_pos
rect2_speed = 3

# Función para manejar el rebote y movimiento de los rectángulos
def move_and_bounce(rect_x, rect_speed, x_limits):
    # Mover el rectángulo
    rect_x += rect_speed

    # Revisar los límites de la ventana
    if rect_x <= x_limits[0] or rect_x + rect_width >= x_limits[1]:
        rect_speed = -rect_speed  # Invertir la dirección al alcanzar los límites

    return rect_x, rect_speed

# Bucle principal
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Llamar a la función para mover y rebotar los rectángulos
    rect1_x, rect1_speed = move_and_bounce(rect1_x, rect1_speed, (80, 300))
    rect2_x, rect2_speed = move_and_bounce(rect2_x, rect2_speed, (200, 400))

    # Limpiar la pantalla
    screen.fill(BLACK)

    # Dibujar los rectángulos
    pygame.draw.rect(screen, WHITE, (rect1_x, rect1_y, rect_width, rect_height))
    pygame.draw.rect(screen, WHITE, (rect2_x, rect2_y, rect_width, rect_height))

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad del bucle
    clock.tick(60)
