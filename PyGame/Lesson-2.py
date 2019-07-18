import pygame

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

while game_over == False:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True
            if event.key == pygame.K_LEFT:
                x -= 10
            if event.key == pygame.K_RIGHT:
                x += 10
            if event.key == pygame.K_UP:
                y -= 10
            if event.key == pygame.K_DOWN:
                y += 10

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            x = x - (img_width / 2)
            y = y - (img_height / 2)
            
    screen.fill(bg_color)
    screen.blit(myimage, (x, y))
    pygame.display.flip()
