class Spaceship():
    def __init__(self):
        self.pos_x = 400
        self.pos_y = 600
        self.size_x = 20
        self.size_y = 30
        self.speed = 0
        self.angle = 30
    
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
        # self.pos_y += self.speed
        p1 = self.rotate_point((0, -self.size_y), self.angle)
        p2 = self.rotate_point((-self.size_x, self.size_y), self.angle)
        p3 = self.rotate_point((self.size_x, self.size_y), self.angle)
        
        next_pos1 = (self.pos_x + p1[0], self.pos_y + p1[1])
        next_pos2 = (self.pos_x + p2[0], self.pos_y + p2[1])
        next_pos3 = (self.pos_x + p3[0], self.pos_y + p3[1])
        
        return next_pos1[0], next_pos1[1], next_pos2[0], next_pos2[1], next_pos3[0], next_pos3[1]
        
        
