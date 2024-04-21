import math

import pygame.image


class Player(object):
    def __init__(self, sw, sh, image):
        # Initialize player properties
        self.img = image  # Player image
        self.sw = sw  # Screen width
        self.sh = sh  # Screen height
        self.w = self.img.get_width()  # Width of the player image
        self.h = self.img.get_height()  # Height of the player image
        self.x = sw // 2  # Initial x-coordinate of the player (centered)
        self.y = sh // 2  # Initial y-coordinate of the player (centered)
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

    def draw(self, win):
        # Draw the player on the screen
        win.blit(self.rotatedSurf, self.rotatedRect)

    def rotate(self):
        # Rotate the player image surface and update the rectangular area and head position
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (
            self.x + self.cosine * self.w // 2,
            self.y - self.sine * self.h // 2,
        )

    def turn(self, direction):
        # Turn the player left or right by 5 degrees and update rotation
        if direction == "left":
            self.angle += 5
        elif direction == "right":
            self.angle -= 5
        self.rotate()

    def move(self, direction):
        # Move the player forward or backward based on its direction and update rotation
        if direction == "forward":
            self.x += self.cosine * 6
            self.y -= self.sine * 6
        elif direction == "backward":
            self.x -= self.cosine * 6
            self.y += self.sine * 6
        self.rotate()

    def updateLocation(self):
        # Update player's location if it goes beyond screen boundaries
        if self.x > self.sw + 50:
            self.x = 0
        elif self.x < 0 - self.w:
            self.x = self.sw
        elif self.y < -50:
            self.y = self.sh
        elif self.y > self.sh + 50:
            self.y = 0
