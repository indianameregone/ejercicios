import pygame, sys, random

pygame.init()

negro = (0,0,0)
blanco = (255, 255,255)
azul = (0,0,255)

size = (800,500)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

coor_x = 100
coor_y = 280

speed_x = 0
speed_y = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed_x = -3
            if event.key == pygame.K_RIGHT:
                speed_x = 3
            if event.key == pygame.K_UP:
                speed_y = -3
            if event.key == pygame.K_DOWN:
                speed_y = 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                speed_x = 0
            if event.key == pygame.K_RIGHT:
                speed_x = 0
            if event.key == pygame.K_UP:
                speed_y = 0
            if event.key == pygame.K_DOWN:
                speed_y = 0

    screen.fill(negro)  
                  
    coor_x += speed_x
    coor_y += speed_y
    pygame.draw.rect(screen,azul, (coor_x,coor_y,100,100))

    pygame.display.flip()
    clock.tick(60)