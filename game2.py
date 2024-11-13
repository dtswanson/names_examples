import pygame
import random

# Initialize Pygame
pygame.init()
pygame.mixer.init()  # Initialize the mixer

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
INITIAL_PLAYER_WIDTH = 50
INITIAL_PLAYER_HEIGHT = 30
OBJECT_SIZE = 30
SPEED = 5
SIZE_INCREASE = 10
MAX_SIZE = 200
GAME_TIME = 30  # Game time in seconds

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (150, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Mr. Swanson's Game")

# Load and play background music
pygame.mixer.music.load('/Users/dswanson/PycharmProjects/Names/Run-Amok(chosic.com).mp3')  # Replace with your audio file
pygame.mixer.music.play(-1)  # Play the music in a loop

# Player class
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = INITIAL_PLAYER_WIDTH
        self.height = INITIAL_PLAYER_HEIGHT
        self.image = pygame.image.load('/Users/dswanson/PycharmProjects/Names/Swanson CIrcle.png')  # Replace with your player image path
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.score = 0
        self.color = BLUE

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= SPEED
        if keys[pygame.K_RIGHT] and self.x < WINDOW_WIDTH - self.width:
            self.x += SPEED
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= SPEED
        if keys[pygame.K_DOWN] and self.y < WINDOW_HEIGHT - self.height:
            self.y += SPEED

    def increase_size(self):
        if self.width + SIZE_INCREASE <= MAX_SIZE and self.height + SIZE_INCREASE <= MAX_SIZE:
            if self.x + self.width + SIZE_INCREASE > WINDOW_WIDTH:
                self.x = WINDOW_WIDTH - (self.width + SIZE_INCREASE)
            if self.y + self.height + SIZE_INCREASE > WINDOW_HEIGHT:
                self.y = WINDOW_HEIGHT - (self.height + SIZE_INCREASE)
            self.width += SIZE_INCREASE
            self.height += SIZE_INCREASE

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

# Collectible class
class Collectible:
    def __init__(self):
        self.x = random.randint(0, WINDOW_WIDTH - OBJECT_SIZE)
        self.y = random.randint(0, WINDOW_HEIGHT - OBJECT_SIZE)
        self.image = pygame.image.load('/Users/dswanson/PycharmProjects/Names/Swanson CIrcle.png')  # Replace with your collectible image path
        self.image = pygame.transform.scale(self.image, (OBJECT_SIZE, OBJECT_SIZE))

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def check_collision(self, player):
        player_rect = pygame.Rect(player.x, player.y, player.width, player.height)
        object_rect = pygame.Rect(self.x, self.y, OBJECT_SIZE, OBJECT_SIZE)
        return player_rect.colliderect(object_rect)
# Create game objects
player = Player(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
collectible = Collectible()

# Timer setup
start_ticks = pygame.time.get_ticks()  # Starter tick
game_over = False

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                player.increase_size()
            # Press SPACE to restart when game is over
            if event.key == pygame.K_SPACE and game_over:
                # Reset game
                player = Player(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
                collectible = Collectible()
                start_ticks = pygame.time.get_ticks()
                game_over = False
            # Press Q to quit when game is over
            if event.key == pygame.K_q and game_over:
                running = False

    # Calculate time remaining
    seconds_left = GAME_TIME - (pygame.time.get_ticks() - start_ticks) // 1000

    if seconds_left <= 0:
        game_over = True

    if not game_over:
        # Game logic
        player.move()

        if collectible.check_collision(player):
            player.score += 1
            collectible = Collectible()

    # Drawing
    screen.fill(WHITE)
    player.draw()
    collectible.draw()

    # Display score, size, and time
    font = pygame.font.Font(None, 36)
    score_text = font.render(f'Score: {player.score}', True, BLACK)
    size_text = font.render(f'Size: {player.width}x{player.height}', True, BLACK)
    time_text = font.render(f'Time: {max(0, seconds_left)}s', True, BLACK if seconds_left > 5 else RED)

    screen.blit(score_text, (10, 10))
    screen.blit(size_text, (10, 50))
    screen.blit(time_text, (10, 90))

    # Show game over message with both restart and quit options
    if game_over:
        game_over_font = pygame.font.Font(None, 74)
        regular_font = pygame.font.Font(None, 36)

        # Game Over text
        game_over_text = game_over_font.render('GAME OVER!', True, RED)
        game_over_rect = game_over_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50))

        # Final score text
        final_score_text = regular_font.render(f'Final Score: {player.score}', True, BLACK)
        final_score_rect = final_score_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 10))

        # Restart text
        restart_text = regular_font.render('Press SPACE to restart', True, BLACK)
        restart_rect = restart_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50))

        # Quit text
        quit_text = regular_font.render('Press Q to quit', True, BLACK)
        quit_rect = quit_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 90))

        # Draw all end screen elements
        screen.blit(game_over_text, game_over_rect)
        screen.blit(final_score_text, final_score_rect)
        screen.blit(restart_text, restart_rect)
        screen.blit(quit_text, quit_rect)

    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()