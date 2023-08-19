# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 18:34:29 2023
Snake Game built using Python's Pygame library.
@author: Mosco
"""

# Initialize pygame
import pygame
import random
pygame.init()

# Define some constant colors
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Define screen dimensions and the size of each cell (or block) in the game grid
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
CELL_SIZE = 20

# Define possible movement directions for the snake
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


class Snake:
    """Represents the snake entity in our game."""
    
    def __init__(self):
        """Initialize a new snake object."""
        self.body = [(5, 5), (4, 5), (3, 5)]  # Snake's body segments
        self.direction = RIGHT  # Initial movement direction
        self.grow = False  # Flag to determine if snake should grow

    def move(self):
        """Move the snake in the current direction."""
        head_x, head_y = self.body[0]
        new_dir_x, new_dir_y = self.direction
        # Calculate new head position; wrap around screen if out of bounds
        new_head = ((head_x + new_dir_x) % (SCREEN_WIDTH // CELL_SIZE),
                    (head_y + new_dir_y) % (SCREEN_HEIGHT // CELL_SIZE))
        
        # Check if snake collides with itself
        if new_head in self.body[1:]:
            return False
        
        # Add new head to the snake's body
        self.body.insert(0, new_head)
        # Remove last segment if snake isn't growing
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

        return True

    def grow_snake(self):
        """Grow the snake by one segment."""
        self.grow = True

    def change_direction(self, new_direction):
        """Change snake's movement direction."""
        # Prevent reversing direction
        if (new_direction[0] + self.direction[0] == 0) and (new_direction[1] + self.direction[1] == 0):
            return
        self.direction = new_direction

    def draw(self, screen):
        """Draw the snake on the screen."""
        for segment in self.body:
            pygame.draw.rect(
                screen, GREEN, (segment[0]*CELL_SIZE, segment[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))


class Food:
    """Represents the food entity in our game."""

    def __init__(self):
        """Initialize food in a random position on the screen."""
        self.position = (random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1),
                          random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1))

    def randomize_position(self):
        """Place food in a new random position."""
        self.position = (random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1),
                          random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1))

    def draw(self, screen):
        """Draw food on the screen."""
        pygame.draw.rect(
            screen, RED, (self.position[0]*CELL_SIZE, self.position[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))


class Game:
    """Manages the main game mechanics and interactions."""

    def __init__(self, screen):
        """Initialize the game with default settings."""
        self.screen = screen
        self.snake = Snake()
        self.food = Food()
        self.score = 0  # Player's score
        self.level = 1  # Game level
        self.speed = 10  # Snake movement speed

    def check_collision(self):
        """Check if snake has collided with the food."""
        if self.snake.body[0] == self.food.position:
            self.snake.grow_snake()
            self.food.randomize_position()
            self.score += 10
            # Increase level every 100 points
            if self.score % 100 == 0:
                self.level_up()

    def level_up(self):
        """Increase the game difficulty."""
        self.level += 1
        self.speed += 3  # Make snake move faster

    def run(self):
        """Main game loop."""
        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    # Handle arrow key inputs to change snake direction
                    if event.key == pygame.K_UP:
                        self.snake.change_direction(UP)
                    elif event.key == pygame.K_DOWN:
                        self.snake.change_direction(DOWN)
                    elif event.key == pygame.K_LEFT:
                        self.snake.change_direction(LEFT)
                    elif event.key == pygame.K_RIGHT:
                        self.snake.change_direction(RIGHT)

            if not self.snake.move():
                # End game if snake collides with itself
                running = False

            self.check_collision()
            self.screen.fill(BLACK)  # Set background color
            self.snake.draw(self.screen)
            self.food.draw(self.screen)

            # Display score and level
            font = pygame.font.Font(None, 36)
            score_text = font.render(f'Score: {self.score}', True, WHITE)
            level_text = font.render(f'Level: {self.level}', True, WHITE)
            self.screen.blit(score_text, (10, 10))
            self.screen.blit(level_text, (10, 40))

            pygame.display.flip()
            clock.tick(self.speed)


if __name__ == "__main__":
    # Set up display and start game
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake Game")

    game = Game(screen)
    game.run()

    pygame.quit()
