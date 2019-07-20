import pygame
import random
import time
import sys

MAX_X = 1920
MAX_Y = 1080
BIG_SNOWFLAKES = 80
MEDIUM_SNOWFLAKES = 300
SMALL_SNOWFLAKES = 800
BIG_SIZE = 25
MEDIUM_SIZE = 15
SMALL_SIZE = 8


def set_speed(size):
    speed = 0
    
    if size == SMALL_SIZE:
        speed = 2
    elif size == MEDIUM_SIZE:
        speed = 3
    elif size == BIG_SIZE:
        speed = 4

    return speed


class Snow():
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.speed = set_speed(self.size)
        self.img_num = random.randint(1, 5)
        self.img_filename = "img/" + str(self.img_num) + ".png"
        self.image = pygame.image.load(self.img_filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.size, self.size))

    def move_snow(self):
        self.y = self.y + self.speed
        if self.y > MAX_Y:
            self.y = 0 - self.size

        i = random.randint(1, 3)
        if i == 1:  # Move right
            self.x = self.x + 1
            if self.x > MAX_X:
                self.x = 0 - self.size
        elif i == 2:  # Move left
            self.x = self.x - 1
            if self.x < 0 - self.size:
                self.x = MAX_X

    def draw_snow(self):
        screen.blit(self.image, (self.x, self.y))
        


def initialize_snow(big, big_size, medium, medium_size, small, small_size, snowfall):
    for i in range(0, big):
        x_pos = random.randint(0, MAX_X)
        y_pos = random.randint(0, MAX_Y)
        snowfall.append(Snow(x_pos, y_pos, big_size))

    for i in range(0, medium):
        x_pos = random.randint(0, MAX_X)
        y_pos = random.randint(0, MAX_Y)
        snowfall.append(Snow(x_pos, y_pos, medium_size))

    for i in range(0, small):
        x_pos = random.randint(0, MAX_X)
        y_pos = random.randint(0, MAX_Y)
        snowfall.append(Snow(x_pos, y_pos, small_size))


def check_for_exit():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            sys.exit()


# ----- Main -----

pygame.init()
screen = pygame.display.set_mode((MAX_X, MAX_Y), pygame.FULLSCREEN)
bg_color = (0, 0, 0)
snowfall = []

initialize_snow(BIG_SNOWFLAKES, BIG_SIZE, MEDIUM_SNOWFLAKES, MEDIUM_SIZE, SMALL_SNOWFLAKES, SMALL_SIZE, snowfall)

while True:
    screen.fill(bg_color)
    check_for_exit()
    for i in snowfall:
        i.move_snow()
        i.draw_snow()
    pygame.display.flip()
    time.sleep(0.02)
