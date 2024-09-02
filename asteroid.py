import pygame
from circleshape import CircleShape

class Asteroid(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y, radius, velocity):

        CircleShape.__init__(self, x, y, radius)
        pygame.sprite.Sprite.__init__(self, self.containers)

        self.x = x
        self.y = y
        self.radius = radius
        self.velocity = velocity

    def draw(self,screen):
        position = (self.x, self.y)
        pygame.draw.circle(screen, "white", position, self.radius, 2)

    def update(self, dt):
        self.x += self.velocity.x * dt
        self.y += self.velocity.y * dt