import pygame, sys, random

pygame.init()

negro = (0,0,0)
blanco = (255, 255,255)

size = (800,500)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

coor_list = []
for i in range(60):
        x = random.randint(0,800)
        y = random.randint(0,500)
        coor_list.append([x,y])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(negro)
    for coor in coor_list:
        x = coor[0]
        y = coor[1]
        pygame.draw.circle(screen,blanco,(x, y), 2)
        coor[1] += 1
        if coor[1] > 500:
            coor[1] = 0

    
    pygame.display.flip()
    clock.tick(60)