import math

import pygame


class EnemyBullet(object):
    def __init__(self, player, x, y):
        # Initialize enemy bullet properties
        self.x = x  # Initial x-coordinate of the bullet
        self.y = y  # Initial y-coordinate of the bullet
        self.w = 20  # Width of the bullet
        self.h = 20  # Height of the bullet

        # Calculate the direction towards the player
        self.dx, self.dy = player.x - self.x, player.y - self.y
        self.dist = math.hypot(self.dx, self.dy)  # Distance between bullet and player
        self.dx, self.dy = self.dx / self.dist, self.dy / self.dist  # Normalize the direction vector
        self.xv = self.dx * 5  # Horizontal velocity of the bullet
        self.yv = self.dy * 5  # Vertical velocity of the bullet

    def draw(self, win):
        # Draw the enemy bullet on the screen
        pygame.draw.circle(win, (255, 0, 0), (self.x + self.w // 2, self.y + self.h // 2), self.w // 2)
        # Draw a circle representing the bullet with red color
