import random

from pygame.surface import Surface

from src.object import GameObject


class Cell(GameObject):
    def __init__(self, sw: int, sh: int, image: Surface):
        super().__init__(sw, sh, image)

        # Generate a random starting point for the cell
        self.ranPoint = random.choice(
            [
                (
                    random.randrange(0, sw - self.w),
                    random.choice([-1 * self.h - 5, sh + 5]),
                ),
                (
                    random.choice([-1 * self.w - 5, sw + 5]),
                    random.randrange(0, sh - self.h),
                ),
            ]
        )
        self.x, self.y = self.ranPoint  # Current position of the cell
        # Determine the direction of movement based on starting point
        if self.x < sw // 2:
            self.x_dir = (
                1  # Move right if starting point is on the left half of the screen
            )
        else:
            self.x_dir = (
                -1
            )  # Move left if starting point is on the right half of the screen
        if self.y < sh // 2:
            self.y_dir = (
                1  # Move down if starting point is on the top half of the screen
            )
        else:
            self.y_dir = (
                -1
            )  # Move up if starting point is on the bottom half of the screen
        self.xv = self.x_dir * 2  # Horizontal velocity of the cell
        self.yv = self.y_dir * 2  # Vertical velocity of the cell

    def draw(self, win: Surface) -> None:
        """Draw the cell on the screen.

        Args:
            win: target window.
        """
        win.blit(self.img, (self.x, self.y))
