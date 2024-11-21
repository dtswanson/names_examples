import pygame
from pygame.locals import *

# Define some colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (126, 126, 126)
BLUE = (0, 0, 255)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))

# Make the RECT INIT
rect = pygame.Rect(100, 100, 200, 150)
resizing = False
resize_start = (0, 0)
moving = False
resize_dir = None

# Function to draw words on the screen
def draw_text(text, pos):
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, (255, 255, 255))
    screen.blit(text_surface, pos)

pts = ('topleft', 'topright', 'bottomleft', 'bottomright',
       'midtop', 'midright', 'midbottom', 'midleft', 'center')

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                moving = True
                resize_start = event.pos
            else:
                for pt in pts:
                    if pygame.Rect(eval('rect.' + pt), (10, 10)).collidepoint(event.pos):
                        resizing = True
                        resize_dir = pt
                        resize_start = event.pos
                        break

        elif event.type == MOUSEBUTTONUP:
            moving = False
            resizing = False

        elif event.type == MOUSEMOTION:
            if moving:
                rect.move_ip(event.rel)
            elif resizing:
                dx = event.pos[0] - resize_start[0]
                dy = event.pos[1] - resize_start[1]
                if 'left' in resize_dir:
                    rect.x += dx
                    rect.width -= dx
                if 'right' in resize_dir:
                    rect.width += dx
                if 'top' in resize_dir:
                    rect.y += dy
                    rect.height -= dy
                if 'bottom' in resize_dir:
                    rect.height += dy
                resize_start = event.pos

    screen.fill(GRAY)
    pygame.draw.rect(screen, RED, rect)
    if moving or resizing:
        pygame.draw.rect(screen, BLUE, rect, 4)
    for pt in pts:
        pos = eval('rect.' + pt)
        draw_text(pt, pos)
        pygame.draw.circle(screen, GREEN, pos, 3)

    pygame.display.flip()

pygame.quit()