import random

def is_collided(obj1, obj2):
    circles1 = obj1.get_collision_circles()
    circles2 = obj2.get_collision_circles()
    for circle1 in circles1:
        for circle2 in circles2:
            if circle1.is_collided_with(circle2):
                return True
    return False

def rotate_point(p, degree):
    angle = radians(degree)
    r_cos = cos(angle)
    r_sin = sin(angle)
    
    p_x = p[0]*r_cos - p[1]*r_sin
    p_y = p[0]*r_sin + p[1]*r_cos

    return p_x, p_y
