import pygame
from circleshape import *

class Shot(CircleShape):
    """A projectile that can be fired"""

    def __init__(self, x, y, radius):
        """Create a new shot"""
        super().__init__(x, y, radius)

    def draw(self, screen):
        """Draw the shot"""
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        """Update the shot's position base on it's velocity"""
        self.position += self.velocity * dt
        