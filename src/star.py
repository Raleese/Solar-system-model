import pygame

class Star:
    def __init__(self, color, radius, posX, posY):
        self.color = color
        self.radius = radius
        self.posX = posX
        self.posY = posY

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.posX, self.posY), self.radius)