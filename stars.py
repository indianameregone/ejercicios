import pygame

screen = pygame.display.set_mode([600,600])
clock = pygame.time.Clock()

done = False

background = pygame.image.load("space.jpg").convert()
player = pygame.image.load("x-wing.png").convert()
player.set_colorkey([0,0,0])

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done =True


    mouse_pos = pygame.mouse.get_pos()
    
    screen.blit(background,[0,0])

    x = mouse_pos[0]
    y = mouse_pos[1]

    screen.blit(player, [x,y])
    pygame.mouse.set_visible(0)

    pygame.display.flip()
    clock.tick(60)
pygame.quit() 