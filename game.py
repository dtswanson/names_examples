import pygame
import random

pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
PLAYER_SIZE = 50
OBJECT_SIZE = 30
SPEED = 5

# Colors for the Game
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Setting the display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Mr. Swanson's Game")


# Player Class
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = BLUE
        self.score = 0

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= SPEED
        if keys[pygame.K_RIGHT] and self.x < WINDOW_WIDTH - PLAYER_SIZE:
            self.x += SPEED
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= SPEED
        if keys[pygame.K_DOWN] and self.y < WINDOW_HEIGHT - PLAYER_SIZE:
            self.y += SPEED

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, PLAYER_SIZE, PLAYER_SIZE))


# Item to be collected class
class Collectible:
    def __init__(self):
        self.x = random.randint(0, WINDOW_WIDTH - OBJECT_SIZE)
        self.y = random.randint(0, WINDOW_HEIGHT - OBJECT_SIZE)
        self.color = GREEN

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, OBJECT_SIZE, OBJECT_SIZE))

    def check_collision(self, player):
        player_rect = pygame.Rect(player.x, player.y, PLAYER_SIZE, PLAYER_SIZE)
        object_rect = pygame.Rect(self.x, self.y, OBJECT_SIZE, OBJECT_SIZE)
        return player_rect.colliderect(object_rect)


# Game Objects
player = Player(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
collectible = Collectible()

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game logic
    player.move()

    if collectible.check_collision(player):
        player.score += 1
        collectible = Collectible()

    # Drawing
    screen.fill(WHITE)
    player.draw()
    collectible.draw()

    # Display score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f'Score: {player.score}', True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()