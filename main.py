import pygame

from constants import *

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
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color=(0, 0, 0))
        pygame.display.flip()
        dt = clock.tick(60) / 1_000

if __name__ == "__main__":
    main()