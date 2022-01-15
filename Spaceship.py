class Spaceship():
    def __init__(self):
        self.pos_x = 400
        self.pos_y = 600
        self.size_x = 20
        self.size_y = 30
        self.speed = 0
        self.angle = 0
    
    def rotate_point(self, p, degree):
        angle = radians(degree)
        r_cos = cos(angle)
        r_sin = sin(angle)
        
        p_x = p[0]*r_cos - p[1]*r_sin
        p_y = p[0]*r_sin + p[1]*r_cos

        return p_x, p_y

    def increase_speed(self, speed):
        self.speed += speed
    
    def get_draw_coord(self):
        self.pos_y += self.speed
        return self.pos_x+0, self.pos_y-self.size_y, self.pos_x-self.size_x, self.pos_y+self.size_y, self.pos_x+self.size_x, self.pos_y+self.size_y
        
        
