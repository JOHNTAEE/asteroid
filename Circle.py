class Circle():
    def __init__(self, x, y, diameter):
        self.x = x
        self.y = y
        self.diameter = diameter

    def is_collided_with(self, cir):
        if (self.x - cir.x)**2 + (self.y - cir.y)**2 < ((self.diameter + cir.diameter)/2)**2:
            return True
        else:
            return False
