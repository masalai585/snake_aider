import pygame
from pygame.locals import *
import pgzrun

# Set up the display
WIDTH = 800
HEIGHT = 600

# Define colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

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
            screen.draw.filled_rect(Rect(segment[0], segment[1], self.width, self.height), GREEN)

    def move(self):
        if keyboard.left and self.direction != "right":
            self.direction = "left"
        elif keyboard.right and self.direction != "left":
            self.direction = "right"
        elif keyboard.up and self.direction != "down":
            self.direction = "up"
        elif keyboard.down and self.direction != "up":
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
        if len(self.body) > 1:
            self.body = self.body[-1:]

    def check_collision(self):
        if self.x < 0 or self.x >= WIDTH or self.y < 0 or self.y >= HEIGHT:
            return True
        return False

# Define the game loop
def update():
    snake.move()

    if snake.check_collision():
        exit()

def draw():
    screen.fill(BLACK)
    snake.draw()

# Run the game loop
if __name__ == "__main__":
    snake = Snake()
    pgzrun.go()
