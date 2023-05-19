import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption('Cross the street')
clock = pygame.time.Clock()
font = pygame.font.Font('font/Pixeltype.ttf', 60)

# pygame.image.load('bilder/Hintergrund.png').convert()
ground_surf = pygame.Surface((1000, 1000))
ground_surf.fill('green')
# pygame.image.load('bilder/Player.png').convert()
player_surf = pygame.Surface((50, 50))
player_surf.fill('red')
# pygame.image.load('bilder/Street.png').convert()
street_surf = pygame.Surface((1000, 80))
street_surf.fill('blue')
# pygame.image.load('bilder/Car1.png').convert_alpha()
car_surf = pygame.Surface((50, 50))
car_x_pos = 950
text_surf = font.render('Was geht?', False, 'black')
straßen = 1000
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(ground_surf, (0, 0))
    screen.blit(player_surf, (500, 950))
    screen.blit(text_surf, (500, 200))
    for x in range(0, 1000, 166):
        screen.blit(street_surf, (0, x))

    screen.blit(car_surf, (car_x_pos, 850))
    car_x_pos -= 8
    if car_x_pos < 0:
        car_x_pos = 1000
    pygame.display.update()
    clock.tick(60)
