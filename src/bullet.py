import pygame
from pygame.surface import Surface

from src.player import Player


class Bullet:
    def __init__(self, sw: float, sh: float, player: Player) -> None:
        self.sw = sw  # Screen width
        self.sh = sh  # Screen height
        self.point = (
            player.head
        )  # Bullet starting point (same as player's head position)
        self.x, self.y = self.point  # Current position of the bullet
        self.w = 20  # Width of the bullet
        self.h = 20  # Height of the bullet
        self.c = (
            player.cosine
        )  # Cosine of the player's angle (used for bullet's horizontal velocity)
        self.s = (
            player.sine
        )  # Sine of the player's angle (used for bullet's vertical velocity)
        self.xv = self.c * 10  # Horizontal velocity of the bullet
        self.yv = self.s * 10  # Vertical velocity of the bullet

    def move(self) -> None:
        """Move the bullet according to its velocity."""
        self.x += self.xv
        self.y -= self.yv  # Subtracting yv since y-axis is inverted in pygame

    def draw(self, win: Surface) -> None:
        # Draw the bullet on the screen
        pygame.draw.circle(
            win,
            (255, 255, 255),
            (self.x + self.w // 2, self.y + self.h // 2),
            self.w // 2,
        )
        # Draw a circle representing the bullet with white color

    def checkOffScreen(self) -> bool:
        """Check if the bullet is off the screen.

        Returns:
            True if bullet is off the screen.
        """
        if self.x < -50 or self.x > self.sw or self.y > self.sh or self.y < -50:
            return True
        return False
