import pygame
import sys

pygame.init()

width = 800
height = 600

screen = pygame.display.set_mode((width, height))

image1 = pygame.image.load("images/casa_embrujada_murci_01.jpg")
image2 = pygame.image.load("images/casa_embrujada_murci_02.jpg")

image3 = pygame.image.load("images/ready_player_one_800x640_blanco_01.jpg")
image4 = pygame.image.load("images/ready_player_one_800x640_blanco_02.jpg")

image_display_time = 0.4  # 2 segundos por imagen

show_images = False
last_image_time = 0
lapse_time = 3000 #en milisegundos
def show_images_at_start(image1, image2, lapse_time, image_display_time, width, height):
    
    global show_images, last_image_time
    current_time = pygame.time.get_ticks()

    if current_time - last_image_time > image_display_time * 1000:
        last_image_time = current_time
        show_images = not show_images
        print(last_image_time)

    if show_images:
        screen.blit(image1, (0, 0))
    elif last_image_time >= lapse_time:
        exit()
    else:
        screen.blit(image2, (0, 0))

show_images_at_start(image1, image2,lapse_time ,image_display_time, width, height)

inicio = True
while inicio:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inicio = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                show_images = False

    show_images_at_start(image1, image2,lapse_time ,image_display_time, width, height)
    pygame.display.flip()

pygame.quit()
sys.exit()
