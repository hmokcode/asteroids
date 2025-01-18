"""Base class for circular game objects with position and collision detection"""
import pygame
from player import *

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        """Create a new circular shape at the specified location"""
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def collisions(self, other):
        """Check for collisions between two circles"""
        distance = self.position.distance_to(other.position)
        if distance <= self.radius + other.radius:
            return True
        return False

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass