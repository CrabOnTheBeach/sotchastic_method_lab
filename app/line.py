import math
from abc import ABC, abstractmethod

class Line(ABC):
    def __init__(self, move_x=0, move_y=0, rotation=0):
        self.move_x = move_x
        self.move_y = move_y
        self.rotation = rotation
        self.sin = math.sin(rotation)
        self.cos = math.cos(rotation)

    def transform(self, x, y):
        return (x * self.cos - y * self.sin + self.move_x, x * self.sin + y * self.cos + self.move_y)

    def back_transform(self, x, y):
        return (
            (x - self.move_x) * self.cos + (y - self.move_y) * self.sin,
            (x - self.move_x) * (-1) * self.sin + (y - self.move_y) * self.cos
            )

    def is_inside(self, x, y):
        x, y = self.back_transform(x, y)
        return self.y(x) < y

    @abstractmethod
    def y(self, x):
        raise NotImplemented

    def transformed_point(self, x):
        return self.transform(x, self.y(x))