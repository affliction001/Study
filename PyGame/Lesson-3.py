import pygame
import time

MAX_X = 800
MAX_Y = 600
game_over = False
bg_color = (0, 0, 50)

pygame.init()
screen = pygame.display.set_mode((MAX_X, MAX_Y))  # set_mode((MAX_X, MAX_Y), pygame.FULLSCREEN)
pygame.display.set_caption("My first PyGame Game! :)")

img_width = 100
img_height = 100
myimage = pygame.image.load("intellogo.png").convert()
myimage = pygame.transform.scale(myimage, (img_width, img_height))

x = 300
y = 250
move_left = False
move_right = False
move_up = False
move_down = False
move_step = 1

while game_over == False:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_UP:
                move_up = True
            if event.key == pygame.K_DOWN:
                move_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_UP:
                move_up = False
            if event.key == pygame.K_DOWN:
                move_down = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            x = x - (img_width / 2)
            y = y - (img_height / 2)

    if move_left == True:
        x -= move_step
        if x < 0:
            x = 5
    if move_right == True:
        x += move_step
        if x > MAX_X - img_width:
            x = MAX_X - img_width - 5
    if move_up == True:
        y -= move_step
        if y < 0:
            y = 5
    if move_down == True:
        y += move_step
        if y > MAX_Y - img_height:
            y = MAX_Y - img_height - 5

    screen.fill(bg_color)
    screen.blit(myimage, (x, y))
    pygame.display.flip()
    time.sleep(0.005)
