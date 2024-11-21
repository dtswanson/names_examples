import pygame
from pygame.locals import *

# Define some colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (126, 126, 126)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))

# Define a rectangle for demonstration purposes
rect = pygame.Rect(100, 100, 200, 150)
resizing = False
resize_start = (0, 0)

# Function to draw text on the screen
def draw_text(text, pos):
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, (255, 255, 255))
    screen.blit(text_surface, pos)

pts = ('topleft', 'topright', 'bottomleft', 'bottomright',
       'midtop', 'midright', 'midbottom', 'midleft', 'center')

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                resizing = True
                resize_start = event.pos

        elif event.type == MOUSEBUTTONUP:
            resizing = False

        elif event.type == MOUSEMOTION and resizing:
            dx = event.pos[0] - resize_start[0]
            dy = event.pos[1] - resize_start[1]
            rect.width += dx
            rect.height += dy
            resize_start = event.pos

    screen.fill(GRAY)
    pygame.draw.rect(screen, GREEN, rect, 4)
    for pt in pts:
        pos = eval('rect.' + pt)
        draw_text(pt, pos)
        pygame.draw.circle(screen, RED, pos, 3)

    pygame.display.flip()

pygame.quit()