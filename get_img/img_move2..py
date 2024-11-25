import pygame
from pygame.locals import *

# Colors (R, G, B)
RED = (255, 0, 0)
GRAY = (150, 150, 150)

# Initialize Pygame
pygame.init()
w, h = 640, 240
screen = pygame.display.set_mode((w, h))
running = True

# Load the image
original_img = pygame.image.load('MIS_Logo.png')
original_img = original_img.convert_alpha()  # Use convert_alpha to preserve transparency
original_rect = original_img.get_rect()
original_rect.center = w // 2, h // 2

# Copy the original image and rect
img = original_img.copy()
rect = original_rect.copy()
moving = False
resizing = False
resize_dir = None

# Main loop
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                if abs(event.pos[0] - rect.left) < 10:
                    resizing = True
                    resize_dir = 'left'
                elif abs(event.pos[0] - rect.right) < 10:
                    resizing = True
                    resize_dir = 'right'
                elif abs(event.pos[1] - rect.top) < 10:
                    resizing = True
                    resize_dir = 'top'
                elif abs(event.pos[1] - rect.bottom) < 10:
                    resizing = True
                    resize_dir = 'bottom'
                else:
                    moving = True

        elif event.type == MOUSEBUTTONUP:
            moving = False
            resizing = False
            resize_dir = None


# Add resizing functionality
        elif event.type == MOUSEMOTION:
            if moving:
                rect.move_ip(event.rel)
            elif resizing:
                if resize_dir == 'left':
                    rect.width = max(1, rect.width - event.rel[0])
                    rect.left += event.rel[0]
                elif resize_dir == 'right':
                    rect.width = max(1, rect.width + event.rel[0])
                elif resize_dir == 'top':
                    rect.height = max(1, rect.height - event.rel[1])
                    rect.top += event.rel[1]
                elif resize_dir == 'bottom':
                    rect.height = max(1, rect.height + event.rel[1])
                img = pygame.transform.smoothscale(img, (rect.width, rect.height))
# Add keyboard control
        elif event.type == KEYDOWN:
            if event.key == K_w:
                rect.move_ip(0, -5)
            elif event.key == K_a:
                rect.move_ip(-5, 0)
            elif event.key == K_s:
                rect.move_ip(0, 5)
            elif event.key == K_d:
                rect.move_ip(5, 0)
    # Reset the image and rect to original state
            elif event.key == K_r:
                img = original_img.copy()
                rect = original_rect.copy()

    screen.fill(GRAY)
    screen.blit(img, rect)
    pygame.draw.rect(screen, RED, rect, 1)
    pygame.display.update()

pygame.quit()