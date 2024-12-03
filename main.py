# removes message printed by the pygame library
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init
    pygame.get_init

    clock = pygame.time.Clock() # setting game clock to limit fps 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    run = True
    dt = 0
    color = (0,0,0)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    #astroid = Asteroid()
    asteroidfield = AsteroidField()


    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color)

        dt=clock.tick(FPS)/1000
        #player.update(dt)
        #player.draw(screen)
        for each in updatable:
            each.update(dt)

        for item in drawable:
            item.draw(screen)
        #dt = pygame.time.Clock.get_time(clock) / 1000
        print(dt/1000)
        print(f"fps: {pygame.time.Clock.get_fps(clock)}")
        pygame.display.flip()
        




if __name__ == "__main__":
    main()