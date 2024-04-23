import math
from enum import StrEnum

import pygame.image
from pygame.surface import Surface

from src.object import GameObject


class Direction(StrEnum):
    FORWARD = "forward"
    BACKWARD = "backward"
    LEFT = "left"
    RIGHT = "right"


class Player(GameObject):
    """The class representing a character controlled by the player."""

    def __init__(self, sw: int, sh: int, image: Surface) -> None:
        super().__init__(sw, sh, image)
        self.x: int = sw // 2  # Initial x-coordinate of the player (centered)
        self.y: int = sh // 2  # Initial y-coordinate of the player (centered)
        self.angle = 0  # Initial angle of rotation
        self.rotatedSurf = pygame.transform.rotate(
            self.img, self.angle
        )  # Rotated player image surface
        self.rotatedRect = (
            self.rotatedSurf.get_rect()
        )  # Rectangular area of the rotated player image
        self.rotatedRect.center = (self.x, self.y)  # Center of the rotated player image
        self.cosine = math.cos(
            math.radians(self.angle + 90)
        )  # Cosine of the angle (used for direction calculation)
        self.sine = math.sin(
            math.radians(self.angle + 90)
        )  # Sine of the angle (used for direction calculation)
        self.head = (
            self.x + self.cosine * self.w // 2,
            self.y - self.sine * self.h // 2,
        )  # Position of player head

    def draw(self, win: Surface) -> None:
        """Draw the player on the screen.

        Args:
            win: target window.
        """
        win.blit(self.rotatedSurf, self.rotatedRect)

    def rotate(self) -> None:
        """Rotate the player image surface and update the rectangular area and head position."""
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (
            self.x + self.cosine * self.w // 2,
            self.y - self.sine * self.h // 2,
        )

    def turn(self, direction: Direction) -> None:
        """Turn the player `left` or `right` by ``5`` degrees and update rotation.

        Args:
            direction: rotation direction.
        """
        if direction == Direction.LEFT:
            self.angle += 5
        elif direction == Direction.RIGHT:
            self.angle -= 5
        self.rotate()

    def move(self, direction: Direction) -> None:
        """Move the player `forward` or `backward` based on its direction and update rotation.

        Args:
            direction: movment direction.
        """
        if direction == Direction.FORWARD:
            self.x += int(self.cosine * 6)
            self.y -= int(self.sine * 6)
        elif direction == Direction.BACKWARD:
            self.x -= int(self.cosine * 6)
            self.y += int(self.sine * 6)
        self.rotate()

    def updateLocation(self) -> None:
        """Update player's location if it goes beyond screen boundaries."""
        if self.x > self.sw + 50:
            self.x = 0
        elif self.x < 0 - self.w:
            self.x = self.sw
        elif self.y < -50:
            self.y = self.sh
        elif self.y > self.sh + 50:
            self.y = 0
