import pygame
from constants import *
from player import *

def main():

    # game initialization
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0

    # Initialize groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # game loop
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # "delta time" - time passed since the last frame was drawn
        dt = clock.tick(60) / 1000

        screen.fill(0)

        for sprite in updatable:
            sprite.update(dt)

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
        
if __name__ == "__main__":
    main()