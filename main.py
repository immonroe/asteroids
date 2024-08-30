import pygame
from constants import *

def main():
    # game initialization
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0

    # game loop
    while True:
        screen.fill(0)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # "delta time" - time passed since the last frame was drawn
        dt =clock.tick(60) / 1000


if __name__ == "__main__":
    main()