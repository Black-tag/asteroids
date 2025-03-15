import pygame
from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape





class Asteroid(CircleShape):


    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        # pygame.sprite.sprite,__init(self)

        self.velocity = pygame.Vector2(0,0)


    def draw(self,screen):
        pygame.draw.circle(screen, (200, 200, 200), self.position, self.radius, 2)

    def update(self,dt):
        self.position += self.velocity * dt