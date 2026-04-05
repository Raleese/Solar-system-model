import pygame
import math

class Planet:
    def __init__(self, name, color, radius, distance_from_sun, orbital_period):
        self.name = name
        self.color = color
        self.radius = radius
        self.distance_from_sun = distance_from_sun
        self.orbital_period = orbital_period

        self.angle = 0

    def draw(self, screen, sun_world_x, sun_world_y, camera_x=0, camera_y=0):
        self.angle += self.orbital_period
        planet_world_x = sun_world_x + math.cos(self.angle) * self.distance_from_sun
        planet_world_y = sun_world_y + math.sin(self.angle) * self.distance_from_sun

        planet_screen_x = planet_world_x - camera_x
        planet_screen_y = planet_world_y - camera_y
        
        sun_screen_x = sun_world_x - camera_x
        sun_screen_y = sun_world_y - camera_y

        pygame.draw.circle(
            screen,
            "gray",
            (int(sun_screen_x), int(sun_screen_y)),
            self.distance_from_sun,
            1
        )
        pygame.draw.circle(screen, self.color, (int(planet_screen_x), int(planet_screen_y)), self.radius)
