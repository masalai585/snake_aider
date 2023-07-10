import streamlit as st
import pygame
import random

# Initialize the game
pygame.init()

# Set up the display
WIDTH = 800
HEIGHT = 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define the snake class
class Snake:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 20
        self.height = 20
        self.vel = 20
        self.direction = "right"
        self.body = [(self.x, self.y)]

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(win, GREEN, (segment[0], segment[1], self.width, self.height))

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.direction != "right":
            self.direction = "left"
        elif keys[pygame.K_RIGHT] and self.direction != "left":
            self.direction = "right"
        elif keys[pygame.K_UP] and self.direction != "down":
            self.direction = "up"
        elif keys[pygame.K_DOWN] and self.direction != "up":
            self.direction = "down"

        if self.direction == "left":
            self.x -= self.vel
        elif self.direction == "right":
            self.x += self.vel
        elif self.direction == "up":
            self.y -= self.vel
        elif self.direction == "down":
            self.y += self.vel

        self.body.append((self.x, self.y))
        self.body = self.body[-1:]

    def check_collision(self):
        if self.x < 0 or self.x >= WIDTH or self.y < 0 or self.y >= HEIGHT:
            return True
        return False

# Define the game loop
def game_loop():
    snake = Snake()
    clock = pygame.time.Clock()
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        snake.move()

        if snake.check_collision():
            game_over = True

        win.fill(BLACK)
        snake.draw()
        pygame.display.update()
        clock.tick(10)

    pygame.quit()

# Run the game loop
if __name__ == "__main__":
    game_loop()
