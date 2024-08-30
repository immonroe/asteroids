import pygame
from constants import *

def main():
    
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        screen.fill(0)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return



if __name__ == "__main__":
    main()