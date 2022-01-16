from Circle import Circle

class Spaceship():
    def __init__(self):
        self.pos_x = 400
        self.pos_y = 600
        self.size_x = 20
        self.size_y = 30
        self.speed = 0
        self.angle = 0
        self.points = []
        
        self.col_areas_info = ((0, 0, 15), (0, 20, 25))
    
    def rotate_point(self, p, degree):
        angle = radians(degree)
        r_cos = cos(angle)
        r_sin = sin(angle)
        
        p_x = p[0]*r_cos - p[1]*r_sin
        p_y = p[0]*r_sin + p[1]*r_cos

        return p_x, p_y

    def increase_speed(self, speed):
        self.speed += speed
        
    def get_collision_circles(self):
        circles = []
        for col_circle in self.col_areas_info:
            rotated_col_circle = self.rotate_point((col_circle[0], col_circle[1]), self.angle)
            circles.append(Circle(self.pos_x + rotated_col_circle[0], self.pos_y + rotated_col_circle[1], col_circle[2]))
        return circles

    def get_draw_coord(self):
        p1 = self.rotate_point((0, -self.size_y), self.angle)
        p2 = self.rotate_point((-self.size_x, self.size_y), self.angle)
        p3 = self.rotate_point((self.size_x, self.size_y), self.angle)
        
        # Apply speed to the position
        speed = self.rotate_point((0, self.speed), self.angle)
        self.pos_x += speed[0]
        self.pos_y += speed[1]
        
        next_pos1 = (self.pos_x + p1[0], self.pos_y + p1[1])
        next_pos2 = (self.pos_x + p2[0], self.pos_y + p2[1])
        next_pos3 = (self.pos_x + p3[0], self.pos_y + p3[1])
        
        self.points = next_pos1[0], next_pos1[1], next_pos2[0], next_pos2[1], next_pos3[0], next_pos3[1]

    def is_out_of_screen(self):
        result = True
        if self.points[0] > 0 and self.points[0] < 1000 and self.points[1] > 0 and self.points[1] < 800:
            result = False

        if self.points[2] > 0 and self.points[2] < 1000 and self.points[3] > 0 and self.points[3] < 800:
            result = False
        
        if self.points[4] > 0 and self.points[4] < 1000 and self.points[5] > 0 and self.points[5] < 800:
            result = False

        return result
        
        
