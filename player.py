import pygame
from circleshape import CircleShape
from constants import (PLAYER_RADIUS, PLAYER_TURN_SPEED, 
                       PLAYER_SPEED, SHOT_RADIUS, PLAYER_SHOT_SPEED)
from bullet import *

class Player(CircleShape):
    """The player controlled triangle ship"""
    def __init__(self, x, y):
        """Create a new player"""
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
    
    def triangle(self):
        """Calculate the three points that mak up the play triangle"""#I copied this one
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        """Draw the player as a triangle"""
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        """Rotate the player based on time passed"""
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        """Player input for moving/shooting"""
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        
    def move(self, dt):
        """Move the player in the direction they're facing"""
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        """Create a new bullet moving in the direction the player is facing"""
        bullet = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        velocity = pygame.Vector2(0, 1).rotate(self.rotation)
        velocity *= PLAYER_SHOT_SPEED
        bullet.velocity = velocity
