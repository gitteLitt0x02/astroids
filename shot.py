import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, PLAYER_SHOT_SPEED
from player import Player

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)


    def draw(self, screen):
        pygame.draw.circle(screen,'grey',(self.position),SHOT_RADIUS)
    
    def update(self, dt):
        self.position += PLAYER_SHOT_SPEED * dt
        