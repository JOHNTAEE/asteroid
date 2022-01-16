from helpers import rotate_point
from Circle import Circle

class Bullet():
    def __init__(self, x, y, angle, speed):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = speed
        self.size = 10
        self.is_active = True
        
    def get_collision_circles(self):
        return [Circle(self.x, self.y, 10)]
    
    def update_move(self):
        speed = rotate_point((0, self.speed), self.angle)
        self.x += speed[0]
        self.y += speed[1]
        
        if self.is_out_of_screen():
            self.is_active = False
    
    def is_out_of_screen(self):
        result = True
        if self.x > 0 and self.x < width and self.y > 0 and self.y < height:
            result = False
        return result
