import pygame 
pygame.init()

negro           = (0,0,0)
blanco          = (255,255,255)
pw              = 15
ph              = 90
screen_size     = (800,600)
screen          = pygame.display.set_mode(screen_size)
clock           = pygame.time.Clock()

player_1_x      = 50
player_1_y      = 255
player_1_sp     = 0

player_2_x      = 750
player_2_y      = 255
player_2_sp     = 0

ball_x          = 400
ball_y          = 265
ball_speed_x    = 3
ball_speed_y    = 3

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type ==  pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_1_sp -= 3
            if event.key == pygame.K_s:
                player_1_sp += 3

        if event.type ==  pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_2_sp -= 3
            if event.key == pygame.K_DOWN:
                player_2_sp += 3

        if event.type ==  pygame.KEYUP:
            if event.key == pygame.K_w:
                player_1_sp = 0
            if event.key == pygame.K_s:
                player_1_sp = 0

        if event.type ==  pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_2_sp = 0
            if event.key == pygame.K_DOWN:
                player_2_sp = 0
    
    if ball_y > 590 or ball_y < 10:
        ball_speed_y *= -1
    if ball_x > 790 or ball_x < 10:
        ball_speed_x *= -1

    player_1_y += player_1_sp
    player_2_y += player_2_sp 

    ball_x     += ball_speed_x
    ball_y     += ball_speed_y

    screen.fill(negro)
    player_1 = pygame.draw.rect(screen,blanco,(player_1_x,player_1_y,pw,ph))
    player_2 = pygame.draw.rect(screen,blanco,(player_2_x,player_2_y,pw,ph))

    ball     = pygame.draw.circle(screen,blanco,(ball_x,ball_y),10)

    if ball.colliderect(player_1) or ball.colliderect(player_2):
        ball_speed_x *= -1

    pygame.display.flip()
    clock.tick(60)
pygame.quit()