import random

def test_print(name):
    print('my name is ', name)
    
def init_asteroids():
    asteroidy = []
    asteroidx = []
    xspeed = []
    yspeed = []
    for i in range(15):
        asteroidy.append(random.randint(-200, 1200))
        asteroidx.append(random.randint(-200,1000))
        xspeed.append(random.randint(-3, 3))
        yspeed.append(random.randint(-3, 3))
    return asteroidx, asteroidy, xspeed, yspeed

def is_collided(obj1, obj2):
    circles1 = obj1.get_collision_circles()
    circles2 = obj2.get_collision_circles()
    for circle1 in circles1:
        for circle2 in circles2:
            if circle1.is_collided_with(circle2):
                return True
    return False
