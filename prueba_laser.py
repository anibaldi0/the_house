import pygame
import sys

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Disparo de láser")

# Colores
white = (255, 255, 255)
red = (255, 0, 0)

# Jugador
player_size = 50
player_x = (screen_width - player_size) // 2
player_y = screen_height - player_size - 10

# Láser
laser_width = 5
laser_height = 20
laser_color = red
laser_speed = 5

def draw_player(x, y):
    pygame.draw.rect(screen, white, [x, y, player_size, player_size])

def draw_laser(x, y):
    pygame.draw.rect(screen, laser_color, [x, y, laser_width, laser_height])

# Game Loop
clock = pygame.time.Clock()

laser_x = 0
laser_y = 0
laser_state = "ready"  # Puede estar "ready" o "fire"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if laser_state == "ready":
            laser_x = player_x + (player_size // 2) - (laser_width // 2)
            laser_y = player_y
            laser_state = "fire"

    screen.fill((0, 0, 0))

    if laser_state == "fire":
        draw_laser(laser_x, laser_y)
        laser_y -= laser_speed
        if laser_y < 0:
            laser_state = "ready"

    draw_player(player_x, player_y)

    pygame.display.flip()
    clock.tick(60)
