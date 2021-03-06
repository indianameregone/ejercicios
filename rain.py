import pygame, sys, random

pygame.init()

negro = (0,0,0)
blanco = (255, 255,255)
azul = (0,0,255)

size = (800,500)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

coor_list = []
for i in range(60):
        x = random.randint(0,800)
        y = random.randint(0,500)
        coor_list.append([x,y])

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
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                speed_x = 0
            if event.key == pygame.K_RIGHT:
                speed_x = 0

    screen.fill(negro)
    coor_x += speed_x
    pygame.draw.rect(screen,azul, (coor_x,coor_y,100,100))
    for coor in coor_list:
        x = coor[0]
        y = coor[1]
        pygame.draw.circle(screen,blanco,(x, y), 2)
        coor[1] += 1
        if coor[1] > 500:
            coor[1] = 0
    pygame.mouse.set_visible(0) #hace el mouse invisible
    '''mouse = pygame.mouse.get_pos() #Mueve la figura con el mouse
    x = mouse[0]
    y = mouse[1]
    pygame.draw.rect(screen,azul, (x,y,100,100))'''

    
    pygame.display.flip()
    clock.tick(60)