from abc import ABC, abstractmethod

from pygame.surface import Surface


class GameObject(ABC):
    def __init__(self, sw: int, sh: int, image: Surface) -> None:
        super().__init__()
        self.sw = sw  # Screen width
        self.sh = sh  # Screen height
        self.img = image  # Object Image
        self.w = self.img.get_width()  # Image width
        self.h = self.img.get_height()  # Image height

    @abstractmethod
    def draw(self, win: Surface) -> None:
        pass
