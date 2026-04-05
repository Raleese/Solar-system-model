import pygame

class Star:
    def __init__(self, color, radius, posX, posY):
        self.color = color
        self.radius = radius
        self.posX = posX
        self.posY = posY

    def draw(self, screen, cam_x=0, cam_y=0):
        pygame.draw.circle(screen, self.color, (self.posX - cam_x, self.posY - cam_y), self.radius)