import random


class Enemy(object):
    def __init__(self, sw, sh, image):
        # Initialize enemy properties
        self.img = image  # Image of the enemy
        self.w = self.img.get_width()  # Width of the enemy image
        self.h = self.img.get_height()  # Height of the enemy image

        # Generate a random starting point for the enemy
        self.ranPoint = random.choice([(random.randrange(0, sw - self.w), random.choice([-1 * self.h - 5, sh + 5])),
                                       (random.choice([-1 * self.w - 5, sw + 5]), random.randrange(0, sh - self.h))])
        self.x, self.y = self.ranPoint  # Current position of the enemy
        # Determine the direction of movement based on starting point
        if self.x < sw // 2:
            self.x_dir = 1  # Move right if starting point is on the left half of the screen
        else:
            self.x_dir = -1  # Move left if starting point is on the right half of the screen
        if self.y < sh // 2:
            self.y_dir = 1  # Move down if starting point is on the top half of the screen
        else:
            self.y_dir = -1  # Move up if starting point is on the bottom half of the screen
        self.xv = self.x_dir * 2  # Horizontal velocity of the enemy
        self.yv = self.y_dir * 2  # Vertical velocity of the enemy

    def draw(self, win):
        # Draw the enemy on the screen
        win.blit(self.img, (self.x, self.y))
