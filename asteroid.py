import pygame
from circleshape import *

class Asteroid(CircleShape):
    """A circular object that moves in a straight line"""
    def __init__(self, x, y, radius):
        """Create a new asteroid at specified position"""
        super().__init__(x, y, radius)

    def draw(self, screen):
        """Draw the asteroid"""
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        """Update the asteroid's position base on its velocity"""
        self.position += self.velocity * dt


