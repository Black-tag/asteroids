import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField






def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()


    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    updatable.add(player)
    drawable.add(player)

    
    Asteroid.containers = (asteroid, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    while (1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)        
        screen.fill(0, rect=None, special_flags=0)
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        # clock.tick(60)
        dt = clock.tick(60) / 1000
        
        
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    












if __name__ == "__main__":
    main()
