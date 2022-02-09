
import pygame, sys

pygame.init()

negro = ( 0, 0, 0)
blanco = (255,255,255)
rojo = (255, 0, 0)
verde = (0, 255, 0)
azul = (0,0,255)


size = (800, 500)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

cord_x = 200
cord_y = 200

speed_x = 3
speed_y = 3

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if (cord_x > 720 or cord_x < 0):
        speed_x *= -1
    if (cord_y > 420 or cord_y < 0):
        speed_y *= -1

    screen.fill(blanco)
    #Zona de dibujo
    #pygame.draw.line(screen, azul, [0,100], [100,200], 5)
    #pygame.draw.rect(screen,verde,(100,100,80,80))
    #pygame.draw.circle(screen,rojo,(200,200),30)  

    cord_x += speed_x
    cord_y += speed_y

    pygame.draw.rect(screen,azul,(cord_x,cord_y,80,80))
    
    #zona de dibujo

    pygame.display.flip()
    clock.tick(60)