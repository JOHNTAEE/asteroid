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
    
