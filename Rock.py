import random
from Circle import Circle

class Rock():
    def __init__(self):
        self.pos_x = random.randint(-200, 1000)
        self.pos_y = random.randint(-200, 1200)
        self.speed_x = random.randint(-3, 3)
        self.speed_y = random.randint(-3, 3)
        
        while self.speed_x == 0 and self.speed_y == 0:
            self.speed_x = random.randint(-3, 3)
            self.speed_y = random.randint(-3, 3)
    
    def update_pos(self):
        self.pos_x += self.speed_x
        self.pos_y += self.speed_y
        
        if self.pos_x >= 1200:
            self.pos_x = -400
        if self.pos_x <= -500:
            self.pos_x = 1000
        if self.pos_y >= 1000:
            self.pos_y = -400
        if self.pos_y <= -500:
            self.pos_y = 800
    
    def get_collision_circles(self):
        offset_x = 295
        offset_y = 225
        diameter = 70
        return [Circle(self.pos_x + offset_x, self.pos_y + offset_y, diameter)]
        
        
