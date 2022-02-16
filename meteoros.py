import pygame,time,random

blanco  = (255,255,255)
negro   = (0,0,0)
alto    = 600
ancho   = 800

class Meteoro(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("meteor.png").convert()
        self.image.set_colorkey(negro)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 1

        if self.rect.y > alto:
            self.rect.y = -10
            self.rect.x = random.randrange(ancho)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("x-wing.png").convert()
        self.image.set_colorkey(negro)
        self.rect = self.image.get_rect()

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        player.rect.x = mouse_pos[0]
        player.rect.y = mouse_pos[1]


pygame.init()
screen  = pygame.display.set_mode([ancho,alto])
clock   = pygame.time.Clock()
done    = False
score   = 0

meteor_list     = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()


for i in range(50):
    meteor = Meteoro()
    meteor.rect.x = random.randrange(800)
    meteor.rect.y = random.randrange(600)
    meteor_list.add(meteor)
    all_sprite_list.add(meteor)

    

player = Player()
all_sprite_list.add(player)


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done =True

    all_sprite_list.update()

    meteor_hit = pygame.sprite.spritecollide(player,meteor_list,True)
    for meteor in meteor_hit:
        score += 1
        print(score)

    screen.fill(blanco)

    all_sprite_list.draw(screen)

    pygame.display.flip()
    clock.tick(60)
pygame.quit() 