# removes message printed by the pygame library
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init
    pygame.get_init

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game = True
    color = (0,0,0)
    while game == True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color)
        pygame.display.flip()




if __name__ == "__main__":
    main()