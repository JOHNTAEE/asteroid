class Spaceship():
    def __init__(self):
        self.pos_x = 400
        self.pos_y = 600
        self.speed_x = 0
        self.speed_y = 0
        self.angle = 0
        self.size_x = 20
        self.size_y = 30
        
    def increase_speed(self, x, y):
        self.speed_x += x
        self.speed_y += y
    
    def get_draw_coord(self):
        self.pos_x += self.speed_x
        self.pos_y += self.speed_y
        return self.pos_x+0, self.pos_y-self.size_y, self.pos_x-self.size_x, self.pos_y+self.size_y, self.pos_x+self.size_x, self.pos_y+self.size_y
        
        
