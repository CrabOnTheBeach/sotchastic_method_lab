import line

class Parabola(line.Line):
    def __init__(self, a=1, move_x=0, move_y=0, rotation=0):
        super().__init__(move_x, move_y, rotation)
        self.a = a
    
    def y(self, x):
        return self.a * x**2
        