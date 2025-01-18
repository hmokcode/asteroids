"""MAIN GAME FILE"""

import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from bullet import *

def main():
    """Initialize and run the game loop

    Sets up the game window, sprite groups, and handles the main game loop
    including updates, collision detection, and rendering."""
    #Initialize Pygame and create window
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Create sprite groups for game objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Set up container relationships for sprites
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    dt = 0  # Delta time for frame-rate independant movement

    # Create initial game objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()

    # Main game loop
    while True:
        # Handle quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update all game objects
        for obj in updatable:
            obj.update(dt)

        # Check for collisions with a player
        for obj in asteroids:
            if obj.collisions(player):
                print("Game over!")
                sys.exit()

        # Clear screen and draw all objects
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        # Update delta time
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()