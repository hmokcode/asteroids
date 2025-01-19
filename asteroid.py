import pygame
import random
from circleshape import *
from constants import *

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

    def split(self):
        """Split asteroids into smaller asteroids (and remove bullets),
            otherwise remove smallest asteroids"""
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)
        velocity_aste1 = self.velocity.rotate(random_angle)
        velocity_aste2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        aste1 = Asteroid(self.position.x, self.position.y, new_radius)
        aste2 = Asteroid(self.position.x, self.position.y, new_radius)
        aste1.velocity = velocity_aste1 * 1.2
        aste2.velocity = velocity_aste2 * 1.2
