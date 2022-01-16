from helpers import rotate_point

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
