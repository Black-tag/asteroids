import pygame
from constants import SHOT_RADIUS,PLAYER_SHOOT_SPEED
from circleshape import CircleShape


class Shot(CircleShape):
    def __init__(self, x, y, rotation):
        super().__init__(x, y, SHOT_RADIUS)
        





    def draw(self,screen):
        pygame.draw.circle(screen, (200, 200, 200), self.position, self.radius, 2)

    def update(self,dt):
        self.position += self.velocity * dt