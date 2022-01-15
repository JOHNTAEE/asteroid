import random

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
    
    def is_collide_with(self, p, rad):
        r_x = 295
        r_y = 225
        r_rad = 70
        distance = sqrt(pow((self.pos_x + r_x - p[0]), 2) + pow((self.pos_y + r_y - p[1]), 2))
        if distance < (r_rad + rad)/2:
            print('crahsed ------')
            return True
        return False
        
        
        
