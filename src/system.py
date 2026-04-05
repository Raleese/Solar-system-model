import pygame
import random
from star import Star

pygame.init()

screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Solar System Model")

clock = pygame.time.Clock()
center = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

stars = []
for i in range(50):
    posX = random.randint(0, screen.get_width())
    posY = random.randint(0, screen.get_height())
    stars.append(Star("lightgray", 2, posX, posY))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    for star in stars:
        star.draw(screen)

    pygame.draw.circle(screen, "yellow", center, 25)

    mouse = pygame.mouse.get_pos()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()