import pygame
import random
from pygame.locals import *

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

# Define colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (126, 126, 126)

# Define initial circle properties
circle_pos = [320, 240]
circle_radius = 20

# Define shape properties
shape_types = ['circle', 'rectangle', 'triangle']
current_shape = 'circle'
shape_pos = [random.randint(50, 590), random.randint(50, 430)]
shape_size = 40

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        circle_pos[0] -= 5
    if keys[K_RIGHT]:
        circle_pos[0] += 5
    if keys[K_UP]:
        circle_pos[1] -= 5
    if keys[K_DOWN]:
        circle_pos[1] += 5

    # Check for collision
    if current_shape == 'circle':
        distance = ((circle_pos[0] - shape_pos[0]) ** 2 + (circle_pos[1] - shape_pos[1]) ** 2) ** 0.5
        if distance < circle_radius + shape_size / 2:
            current_shape = random.choice(shape_types)
            shape_pos = [random.randint(50, 590), random.randint(50, 430)]
    elif current_shape == 'rectangle':
        rect = pygame.Rect(shape_pos[0] - shape_size / 2, shape_pos[1] - shape_size / 2, shape_size, shape_size)
        if rect.collidepoint(circle_pos):
            current_shape = random.choice(shape_types)
            shape_pos = [random.randint(50, 590), random.randint(50, 430)]
    elif current_shape == 'triangle':
        triangle_points = [
            (shape_pos[0], shape_pos[1] - shape_size / 2),
            (shape_pos[0] - shape_size / 2, shape_pos[1] + shape_size / 2),
            (shape_pos[0] + shape_size / 2, shape_pos[1] + shape_size / 2)
        ]
        if pygame.draw.polygon(screen, BLUE, triangle_points).collidepoint(circle_pos):
            current_shape = random.choice(shape_types)
            shape_pos = [random.randint(50, 590), random.randint(50, 430)]

    # Draw everything
    screen.fill(GRAY)
    if current_shape == 'circle':
        pygame.draw.circle(screen, RED, circle_pos, circle_radius)
    elif current_shape == 'rectangle':
        pygame.draw.rect(screen, RED, (circle_pos[0] - shape_size / 2, circle_pos[1] - shape_size / 2, shape_size, shape_size))
    elif current_shape == 'triangle':
        pygame.draw.polygon(screen, RED, [
            (circle_pos[0], circle_pos[1] - shape_size / 2),
            (circle_pos[0] - shape_size / 2, circle_pos[1] + shape_size / 2),
            (circle_pos[0] + shape_size / 2, circle_pos[1] + shape_size / 2)
        ])
    pygame.draw.circle(screen, BLUE, shape_pos, shape_size // 2)
    pygame.display.update()
    clock.tick(30)

pygame.quit()