import pygame, sys

pygame.init()
screen = pygame.display.set_mode((576,1024))
clock = pygame.time.Clock()

bg_surface = pygame.image.load('').convert()
bg_surface = pygame.transform.scale2x(bg_surface)

floor_surface = pygame.image.load('base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.blit(bg_surface,(0,0))
    floor_x_pos += 1
    screen.blit(floor_surface,(floor_x_pos,900))

    pygame.display.update()
    clock.tick(120)

