import pygame
from pygame.locals import *

#Colors (R, G, B)
RED = (255, 0, 0)
GRAY = (150, 150, 150)

# Initialize Pygame
pygame.init()
w, h = 640, 240
screen = pygame.display.set_mode((w, h))
running = True

# Load the image
img = pygame.image.load('MIS_Logo.png')
img.convert()
rect = img.get_rect()
rect.center = w // 2, h // 2
moving = False

# Main loop
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                moving = True

        elif event.type == MOUSEBUTTONUP:
            moving = False

        elif event.type == MOUSEMOTION and moving:
            rect.move_ip(event.rel)

    screen.fill(GRAY)
    screen.blit(img, rect)
    pygame.draw.rect(screen, RED, rect, 1)
    pygame.display.update()

pygame.quit()