import random


class Virus(object):
    def __init__(self, sw, sh, rank, images):
        """
        Initialize a virus object.

        Args:
            sw (int): Screen width.
            sh (int): Screen height.
            rank (int): Rank of the virus.
            images (list): List of images for different ranks of the virus.
        """
        self.rank = rank
        # Select image based on virus rank
        if self.rank == 1:
            self.image = images[0]
        elif self.rank == 2:
            self.image = images[1]
        else:
            self.image = images[2]

        # Set width and height based on virus rank
        self.w = 50 * rank
        self.h = 50 * rank

        # Randomize initial position
        self.ranPoint = random.choice([(random.randrange(0, sw - self.w), random.choice([-1 * self.h - 5, sh + 5])),
                                       (random.choice([-1 * self.w - 5, sw + 5]), random.randrange(0, sh - self.h))])
        self.x, self.y = self.ranPoint

        # Determine initial direction based on position
        if self.x < sw // 2:
            self.x_dir = 1
        else:
            self.x_dir = -1
        if self.y < sh // 2:
            self.y_dir = 1
        else:
            self.y_dir = -1

        # Set random velocities
        self.xv = self.x_dir * random.randrange(1, 3)
        self.yv = self.y_dir * random.randrange(1, 3)

    def draw(self, win):
        """
        Draw the virus on the window.

        Args:
            win: Pygame window surface.
        """
        win.blit(self.image, (self.x, self.y))
