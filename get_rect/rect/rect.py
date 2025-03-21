import pygame
from pygame.locals import *

# Define some colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (127, 127, 127)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((640, 240))

# Variables to store the rectangle's start position, size, and drawing state
start = (0, 0)
size = (0, 0)
drawing = False
rect_list = []

# Main loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == MOUSEBUTTONDOWN:
            start = event.pos
            size = 0, 0
            drawing = True

        elif event.type == MOUSEBUTTONUP:
            end = event.pos
            size = end[0] - start[0], end[1] - start[1]
            rect = pygame.Rect(start, size)
            rect_list.append(rect)
            drawing = False

        elif event.type == MOUSEMOTION and drawing:
            end = event.pos
            size = end[0] - start[0], end[1] - start[1]
# Draw the screen
    screen.fill(GRAY)
    for rect in rect_list:
        pygame.draw.rect(screen, RED, rect, 3)
    pygame.draw.rect(screen, BLUE, (start, size), 1)
    pygame.display.update()
# Quit Pygame
pygame.quit()