import pygame
import random
from star import Star
from planet import Planet

pygame.init()
myfont = pygame.font.SysFont("Consolas", 15)

screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Solar System Model")

clock = pygame.time.Clock()
center = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
running = True

SCROLL_SPEED = 5
SCROLL_SPEED_SLOW = 1

MIN_ZOOM = 0.2
MAX_ZOOM = 3
CURRENT_ZOOM = 1
ZOOM_FACTOR = 0.1

sun_world_x = center.x
sun_world_y = center.y

camera_x = 0
camera_y = 0
camera_x_star = 0
camera_y_star = 0

# Create stars
stars = []
for i in range(1500):
    posX = random.randint(0, 8000)
    posY = random.randint(0, 8000)
    size = random.randint(1, 4)
    stars.append(Star("lightgray", size, posX, posY))

planets = [
    Planet("Mercury", "gray", 5, 110, 0.02),
    Planet("Venus", "orange", 8, 170, 0.015),
    Planet("Earth", "blue", 10, 230, 0.01),
    Planet("Mars", "red", 7, 300, 0.008),
    Planet("Jupiter", "brown", 20, 410, 0.005),
    Planet("Saturn", "yellow", 18, 520, 0.003),
    Planet("Uranus", "lightblue", 15, 640, 0.002),
    Planet("Neptune", "darkblue", 15, 760, 0.001)
]


# Main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEWHEEL:
            CURRENT_ZOOM += event.y * ZOOM_FACTOR
            CURRENT_ZOOM = max(MIN_ZOOM, min(MAX_ZOOM, CURRENT_ZOOM))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        camera_y -= SCROLL_SPEED
        camera_y_star -= SCROLL_SPEED_SLOW

    if keys[pygame.K_s]:
        camera_y += SCROLL_SPEED
        camera_y_star += SCROLL_SPEED_SLOW

    if keys[pygame.K_a]:
        camera_x -= SCROLL_SPEED
        camera_x_star -= SCROLL_SPEED_SLOW

    if keys[pygame.K_d]:
        camera_x += SCROLL_SPEED
        camera_x_star += SCROLL_SPEED_SLOW

    screen.fill("black")

    for star in stars:
        star.draw(screen, camera_x_star, camera_y_star)

    screen_x = sun_world_x - camera_x
    screen_y = sun_world_y - camera_y

    pygame.draw.circle(screen, "yellow", (screen_x, screen_y), 75*CURRENT_ZOOM)

    for planet in planets:
        planet.draw(screen, sun_world_x, sun_world_y, CURRENT_ZOOM, camera_x, camera_y)
        label = myfont.render(planet.name, True, "white")
        label_rect = label.get_rect(center=(planet.screen_x, planet.screen_y - 20))
        screen.blit(label, label_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()