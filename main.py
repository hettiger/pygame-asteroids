import sys
import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot


def main():
    print(
        "Starting Asteroids!",
        f"Screen width: {SCREEN_WIDTH}",
        f"Screen height: {SCREEN_HEIGHT}",
        sep="\n"
    )
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)

    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)
    AsteroidField()

    Shot.containers = (shots, updatable, drawable)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color=(0, 0, 0))
        updatable.update(dt)
        for a in asteroids:
            for s in shots:
                if a.collides_with(s):
                    a.kill()
                    s.kill()
            if a.collides_with(player):
                print("Game over!")
                sys.exit(0)
        for d in drawable:
            d.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1_000

if __name__ == "__main__":
    main()